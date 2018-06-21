import config as cfg
from tinydb import TinyDB, Query
import smartypants
from operator import itemgetter
import arrow
import fetch
import re
import time

# ALL ABOUT THE DATA: ThIS MODULE TRANSFORMS DATA, DEALS WITH DATABASE

def parse_feed(items):
    # input a list of dicts (ie fetched data from an api, rss)
    posts = []
    for item in items:
        post = {}
        # post['title'] = x['title'].strip().translate(str.maketrans({"'": r"\'"}))
        post['title_api'] = smartypants.smartypants(item['title'].strip())
        # post['type'] = x['contentType'] # either ArticleStory or ArticleBlogpost
        post['asset_id'] = item['assetId']
        post['source_api'] = item['newsSource']
        post['tags_api'] = []
        if 'imageCaption' in item:
            post['caption_api'] = smartypants.smartypants(item['imageCaption'].strip())
        else:
            post['caption_api'] = ""
        # NOTE THIS FAILS IF NO SUBCATEGORIES, LIKE A STAFF STORY WITH JUST 'SPORTS'
        # USE CATEGORIES IN FEED INSTEAD?
        if 'categoriesSubCategories' in item:    
            post['categories_api'] = list(set([item for sublist in item['categoriesSubCategories'] for item in sublist.split('||')]))
        else:
            post['categories_api'] = ""
        post['desc_api'] = smartypants.smartypants(item['description'].strip())
        post['desc_api'] = " ".join(post['desc_api'].split())
        if item['contentType'] == 'ArticleBlogpost':
            post['link'] = 'https://www.thespec.com/blogs/post/' + item['assetId'] + '-' + item['titleAlias'] + '/'
        else:
            post['link'] = 'https://www.thespec.com/news-story/' + \
                item['assetId'] + '-' + item['titleAlias'] + '/'
        if 'superPortraitUrl' in item:
            post['img_api'] = item['superPortraitUrl']
        else:
            post['img_api'] = ""
        if 'image150x100Url' in item:
            post['img_api_thumb'] = item['image150x100Url']
        else:
            post['img_api_thumb'] = ""
        post['pubdate_api'] = item['publishFromDate']
        post['timestamp'] = (arrow.get(item['publishFromDate'])).format('MM-DD h:mm a')
        post['site_api'] = item['newspaperName']
        post['author_api'] = item['authorName']
        if item['rootCategory'] == "opinion":
            post['label_api'] = "OPINION"
        else:
            post['label_api'] = ""
        if post['label_api']:
            if post['author_api']:
                post['label_api'] += " | " + post['author_api']
            if post['source_api']:
                post['label_api'] += " | " + post['source_api']
            else:
                if post['site_api']:
                    post['label_api'] += " | " + post['site_api']
        else:
            if post['author_api']:
                post['label_api'] += post['author_api']
                if post['source_api']:
                    post['label_api'] += " | " + post['source_api']
                else:
                    if post['site_api']:
                        post['label_api'] += " | " + post['site_api']
            else:
                if post['source_api']:
                    post['label_api'] += post['source_api']
                else:
                    if post['site_api']:
                        post['label_api'] += post['site_api']
        post['label_api'] = post['label_api'].replace("The Hamilton Spectator", "The Spec").replace("Hamilton Spectator", "The Spec").replace("Toronto Star", "The Star")
        post['draft_api'] = False
        posts.append(post)
    # filter out duplicates (if dealing with multiple sources)
    unique_posts = list({v['asset_id']: v for v in posts}.values())
    # sorted_posts = sorted(unique_posts, key=itemgetter('dnn_pubdate'), reverse=True)
    return unique_posts


def filter_feed(items):
    new_list =[]
    m = re.compile('Ticats', flags=re.I)
    for item in items:
        # is 'Ticats' in 'categories_api'?
        if any(m.search(x) for x in item['categories_api']):
            # Yes. Add item to new_list
            new_list.append(item)
            # No. Is 'Ticats in 'title' OR 'description' OR 'caption'?
        elif any(m.search(x) for x in [item['title_api'], item['desc_api'], item['caption_api']]):
            # Yes. Add item to new_list
            new_list.append(item)
            # No. Set item to draft
        else:
            item['draft_api'] = True
            new_list.append(item)
    return new_list


def munge_feed(items):
    # input a list of dicts (ie fetched data from an api, rss)
    # filters are list of tuples, with key and value
    # all items filtered out will be set to 'draft'
    filters = cfg.config['munge']
    new_list = []
    if filters:
        for item in items:
            for key, test, the_match, action in filters:
                if test is 'contains':
                    m = re.compile(the_match)
                    if m.search(item[key]):
                        if action['action'] is 'set_key':
                            item[action['section']] = action['value']
                        if action['action'] is 'replace':
                            item[key] = re.sub(action['target'], action['sub'], item[key])

            new_list.append(item)
        return new_list
    else:
        return items


def db_insert(c_posts, check=True):
    # based on asset_id being the unique record for DNN-based content
    # must create record with defaults first with fields I won't want affected
    # c_posts may be many or 1, so convert to list
    # by upserting from whatever's in DNN feed
    # if check is True, we have to check if record exists in database
    # if check is False, we don't have to, use update method
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    if not isinstance(c_posts, list):
        c_posts = [c_posts]
    for post in c_posts:
        if check is True:
            # does record exist?
            result = db.search(Record.asset_id == post['asset_id'])
            # print(f"Result of search for record id is:\n{result}")
            # If not, insert with defaults
            if not result:
                new_post = cfg.config['db_fields_dflt'].copy()
                new_post['asset_id'] = post['asset_id']
                # print("+++++++++++\n")
                # print(f"Post title is: {post['title_api']}")
                # if munge has set draft_api to true
                # set default draft state to 1 (draft by algorithm)
                # print(f"Post draft_api is: {post['draft_api']}")
                if post['draft_api'] is True:
                    # print("Setting draft to 1 ...")
                    new_post['draft_user'] = 1
                # print("Defaults going in")
                # print(new_post)
                db.insert(new_post)
                # print("+++++++++++++++")
        # now update with all DNN fields
        db.update(post, Record.asset_id == post['asset_id'])
        print("Upserting the following post:")
        print(post)
    db.close()
    return


def get_new_data():
    print("++++++++++\nIn get_new_data module ...")
    for api in cfg.config['apis']:
        data = fetch.fetch_data(s_url=api['url'], l_filter=api['filter'])
        raw_posts = parse_feed(data)
        # posts = munge_feed(raw_posts)
        posts = filter_feed(raw_posts)
        db_insert(posts)
        time.sleep(1)


def get_lineup():
    # how do we deal when draft/rank conflict?
    # At the moment, a ranked item set to draft
    # shows up in Lineup (by rank) without draft, AND on drafts page
    # this each pages chooses items slightly differently
    # Assumption rank overrides draft?
    print("++++++++++++++\nIn get_lineup module ...")
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    # get records that are 1. not in draft 2. not in rank list
    # lineup = {} this not needed as we are returning list, not dict of lists
    # get any records with rank not equal to 0
    rank_list = sorted(db.search(Record.rank != 0), key=itemgetter('rank'))
    # print(f"rank list is: {rank_list}")
    # NOTE:
    published = [x for x in is_draft(db.all(), False) if x['rank'] == 0]
    # print(f"++++++++\nPublished list is:\n")
    # for z in published:
    # print(z['title_api'])
    lineup = [x for x in published][:18]
    # print(f"Lineup spec is: {lineup['spec']}")
    # need to insert items from rank list
    for item in rank_list:
        # what happens if items have same rank?
        # I think they get put in according to how list was sorted
        # so latest item with same rank is ahead of older item with same rank?
        idx = (item['rank'] - 1)
        lineup[idx:idx] = [item]
    db.close()
    # print("Records going into lineup:")
    # print(records)
    return lineup


def request_item(form_data, asset_id):
    fields = ["rank", "rank_time", "draft_user", "desc_user", "title_user"]
    post = {}
    post['asset_id'] = asset_id
    for field in fields:
        if form_data[field] != '':
            post[field] = form_data[field]
    return post


# def request_lineup(form_data):
#     fields = ["rank", "rank_time", "draft"]
#     for field in fields:
#         set_value(form_data[field], value)


def parse_form(form_data, kind="list"):
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    print("incoming form data:")
    # print(form_data)
    # print("converted to a dict")
    print(dict(form_data))
    # form data will have keys, values that may be lists or a single string.
    form_data_dict = dict(form_data)
    if kind == 'list':
        # form data is coming from the 'lineup' page,
        # which can have multiple changes on multiple assets
        for k, v in form_data_dict.items():
            if k != "action":
                if isinstance(v, list):
                    # it's a list of strings.
                    for item in v:
                        # check if empty string
                        if item:
                            asset_id, field, new_value = item.split('__')
                            print(f"++++++++\nSetting this item: {asset_id} to {field}: {new_value}\n++++++++")
                            db.update({field: int(new_value)}, Record.asset_id == asset_id)
                else:
                    # check if empty string
                    if v:
                        asset_id, field, new_value = v.split('__')
                        print(f"++++++++\nSetting this item: {asset_id} to {field}: {new_value}\n++++++++")
                        db.update({field: int(new_value)}, Record.asset_id == asset_id)
    else:
        # form data is coming from the 'item' page instead,
        # mutiple changes possible but only 1 asset affected
        post_update = {}
        asset_id = form_data_dict['asset_id'][0]
        for x in ['draft_user', 'rank', 'rank_time']:
            if form_data_dict[x][0] != '':
                post_update[x] = int(form_data_dict[x][0])
        for x in ['label_user', 'title_user', 'desc_user']:
            if form_data_dict[x][0] != '':
                post_update[x] = smartypants.smartypants(form_data_dict[x][0].strip())
        print("Data to update:")
        print(post_update)
        db.update(post_update, Record.asset_id == asset_id)
    db.close()
    return


def set_value(value_list, value):
    # we will be getting a list of rank values: record-id_new-rank
    # ['8605132_1', '8605133_0', '8605134_0',]
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    for item in value_list:
        if item:
            asset_id, new_value = item.split('__')
            db.update({value: int(new_value)}, Record.asset_id == asset_id)
            print(f"++++++++\nSetting this item: {asset_id} to {value}: {new_value}\n++++++++")
    db.close()
    return


def sort_by_latest(records):
    return sorted(records, key=itemgetter('pubdate_api'), reverse=True)


def is_draft(val, condition=True):
    # returns list if given list,
    # returns true/false if given record
    # 'condition' is boolean. True means we want items in 'draft
    if condition is True:
        records = [x for x in val if x['draft_user'] > 0]
        # print("+++++++++++\nThese items ARE in draft:")
        # for z in records:
        # print(z['title_api'])
    else:
        records = [x for x in val if x['draft_user'] == 0]
        # print("+++++++++++\nThese items are NOT in draft:")
        # for z in records:
        # print(z['title_'])
    return sorted(records, key=itemgetter('pubdate_api'), reverse=True)


def get_drafts():
    db = TinyDB(cfg.config['db_name'])
    # Record = Query()
    records = is_draft(db.all(), True)
    db.close()
    return records


def set_draft(ids, status=True):
    # Status: 0 -> publish, 1 -> draft_api, 2 -> draft
    # if status True, set to draft, else set to publish
    # given a list of asset_ids, set them to draft or publish depending on status
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    draft = 2 if status else 0
    for item_id in ids:
        if item_id:
            db.update({'draft_user': draft}, Record.asset_id == item_id)
            print(f"++++++++\nSetting this item: {item_id} to status: {draft}\n++++++++")
    db.close()
    return


def get_record(s_id):
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    record = db.search(Record.asset_id == s_id)
    db.close()
    return record
