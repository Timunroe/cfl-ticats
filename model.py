import config as cfg
from tinydb import TinyDB, Query
import smartypants
from operator import itemgetter
import fetch
import re
import datetime
import time

# ALL ABOUT THE DATA: ThIS MODULE TRANSFORMS DATA, DEALS WITH DATABASE


def parse_feed(items):
    # input a list of dicts (ie fetched data from an api, rss)
    # keys = [(post key1, feed key1, default if not found), ...]
    # dict .get() method handles if key not found in dict!
    keys = [
        ('asset_id', 'assetId', ''),
        ('title_api', 'title', ''),
        ('source_api', 'newsSource', ''),
        ('site_api', 'newspaperName', ''),
        ('author_api', 'authorName', ''),
        ('pubdate_api', 'publishFromDate', ''),
        # helpers
        ('desc_api', 'description', ''),
        ('caption_api', 'imageCaption', ''),
        # start of taxonomy: sections [DNN categories] > categories [DNN subcategories] > topics > tags
        ('sections_api', 'categories', []),
        ('categories_api', 'categoriesSubCategories', []),
        # images data
        ('img_api', 'superPortraitUrl', ''),
        ('img_api_thumb', 'image150x100Url', ''),
    ]
    posts = []
    for item in items:
        post = {}
        for field in keys:
            post[field[0]] = item.get(field[1], field[2])
        # new fields
        post['draft_api'] = False
        post['tags_api'] = []
        post['topics_api'] = []
        # synthesized fields
        # NEEDS REWRITE: DOMAIN NEEDS TO BE ADDED AT POINT OF PUBLISHING
        post['link'] = 'https://www.thespec.com/news-story/' + \
            item['assetId'] + '-' + item['titleAlias'] + '/'
        posts.append(post)
    # filter out duplicates (if dealing with multiple sources)
    # https://stackoverflow.com/questions/11092511/python-list-of-unique-dictionaries
    unique_posts = list({v['asset_id']: v for v in posts}.values())
    # print("++++++++++\nResult of parse_feed:")
    # print(unique_posts)
    return unique_posts


def filter_feed(items):
    new_list = []
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


def str_len_check(str):
    if len(str) > 0:
        return 1
    else:
        return 0


def munge_feed(items):
    print("++++++++++\nIn munge_feed module ...")
    for post in items:
        post['title_api'] = smartypants.smartypants(post['title_api'].strip())
        post['caption_api'] = smartypants.smartypants(post['caption_api'].strip())
        regex = re.compile(r"^.*\|\|", re.IGNORECASE)
        post['categories_api'] = list(set([regex.sub('', x) for x in post['categories_api']]))
        post['desc_api'] = smartypants.smartypants(post['desc_api'].strip())
        post['desc_api'] = " ".join(post['desc_api'].split())
        date_object = datetime.datetime.strptime(post['pubdate_api'], '%Y-%m-%dT%H:%M:%S')
        post['timestamp'] = date_object.strftime('%b %d %I:%M %p')
        post['timestamp'] = post['timestamp'].replace(' 0', ' ').replace('Jul', 'July').replace('Apr', 'April').replace('Mar', 'March').replace('Jun', "June").replace(':00', '')
        post['timestamp_epoch'] = int((date_object - datetime.datetime(1970, 1, 1)).total_seconds())
        if "opinion" in post['sections_api']:
            label_start = "OPINION"
        else:
            label_start = ""
        if post['source_api']:
            label_end = post['source_api']
        else:
            label_end = post['site_api']
        post['label_api'] = ((label_start + ' | ') * str_len_check(label_start)) + ((post['author_api'] + ' | ') * str_len_check(post['author_api'])) + label_end
        post['label_api'] = post['label_api'].replace("The Hamilton Spectator", "The Spec").replace("Hamilton Spectator", "The Spec").replace("Toronto Star", "The Star")
    return items


def db_insert(c_posts, check=True):
    # based on asset_id being the unique record for DNN-based content
    # must create record with defaults first with fields I won't want affected
    # c_posts may be many or 1, so convert to list
    # by upserting from whatever's in DNN feed
    # if check is True, we have to check if record exists in database
    # if check is False, we don't have to, use update method
    db = TinyDB('db.json')
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
                    new_post['draft_user'] = ['1']
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
        posts = munge_feed(raw_posts)
        # posts = filter_feed(raw_posts)
        db_insert(posts)
        time.sleep(1)
    expire()


def expire():
    # move old items from db to archives.json
    # get all items in db, check each timestamp, if old then
    # move to archives, delete from db
    # TODO: delete really old items from archives - 90 days?
    db = TinyDB('db.json')
    db_old = TinyDB('archives.json')
    Record = Query()
    age_limit = 30 * 24 * 60 * 60  # 30 days
    cutoff = ((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()) - age_limit
    expired_list = db.search(Record.timestamp_epoch < cutoff)
    if expired_list:
        for record in expired_list:
            db_old.insert(record)
            time.sleep(0.5)
            db.remove(Record.asset_id == record['asset_id'])


def get_posts(kind):
    # kind = "published|drafts|archived|cfl|nfl|fbs|usports|mlb|mls|nhl|nba"
    # +++++++++++++++++++++++++++++
    print("++++++++++++++\nIn get_lineup module ...")
    if kind == 'archives':
        db = TinyDB('archives.json')
        the_list = sorted(db.all(), key=itemgetter('pubdate_api'), reverse=True)
    else:
        db = TinyDB('db.json')
        Record = Query()
        # get records that are 1. not in draft 2. not in rank list
        # lineup = {} this not needed as we are returning list, not dict of lists
        # get any records with rank not equal to 0
        # rank_list = sorted(db.search(Record.rank != 0), key=itemgetter('rank'))
        # print(f"rank list is: {rank_list}")
        if kind == 'published':
            # get records that are not in draft
            # rank_list = sorted(db.search(Record.rank != 0), key=itemgetter('rank'))
            non_draft = db.search(Record.draft_user == ['0'])
            # non_draft = [x for x in db.all() if x['draft_user'] == ['0']]
            the_list = sorted(non_draft, key=itemgetter('pubdate_api'), reverse=True)
        if kind == "drafts":
            the_list = sorted(db.search(Record.draft_user != ['0']), key=itemgetter('pubdate_api'), reverse=True)
        # print("Records going into lineup:")
        # print(records)
    db.close()
    return the_list


def get_lineup(kind):
    # kind = "published|drafts|deleted"
    # +++++++++++++++++++++++++++++
    # how do we deal when draft/rank conflict?
    # At the moment, a ranked item set to draft
    # shows up in Lineup (by rank) without draft, AND on drafts page
    # this each pages chooses items slightly differently
    # Assumption rank overrides draft?
    print("++++++++++++++\nIn get_lineup module ...")
    db = TinyDB('db.json')
    Record = Query()
    # get records that are 1. not in draft 2. not in rank list
    # lineup = {} this not needed as we are returning list, not dict of lists
    # get any records with rank not equal to 0
    # rank_list = sorted(db.search(Record.rank != 0), key=itemgetter('rank'))
    # print(f"rank list is: {rank_list}")

    if kind == 'published':
        # rank_list = sorted(db.search(Record.rank != 0), key=itemgetter('rank'))
        non_draft = [x for x in db.all()
                     if x['draft_user'] == ['0']]
        non_rank_list = sorted([x for x in non_draft if x['rank'] == 0], key=itemgetter('pubdate_api'), reverse=True)
        rank_list = sorted([x for x in non_draft if x['rank'] != 0], key=itemgetter('rank'))
        the_list = non_rank_list[:18]
        # need to insert items from rank list
        for item in rank_list:
            # what happens if items have same rank?
            # I think they get put in according to how list was sorted
            # so latest item with same rank is ahead of older item with same rank?
            idx = (item['rank'] - 1)
            the_list[idx:idx] = [item]
    if kind == "drafts":
        # draft_sorted = sorted(draft, key=itemgetter('pubdate_api'), reverse=True)
        the_list = sorted(db.search(Record.draft_user != 0), key=itemgetter('pubdate_api'), reverse=True)
    db.close()
    # print("Records going into lineup:")
    # print(records)
    return the_list


def request_item(form_data, asset_id):
    fields = ["rank", "rank_time", "draft_user", "desc_user", "title_user"]
    post = {}
    post['asset_id'] = asset_id
    for field in fields:
        if form_data[field] != '':
            post[field] = form_data[field]
    return post


def parse_form(form_data, kind="list"):
    #  TODO: NEEDS TO BE REWRITTEN!!!
    #  TODO: Don't need param 'kind', won't everthing be a list?
    # EXAMPLE OF INCOMING FORM DATA, where I set a published item to draft, then added 2 topics
    # {'action': ['save'], 'draft': ['8805675__draft_user__2', '', ''], 'sections': ['', '', '', ''], 'topics': ['8805675__topics__AHL', '8805675__topics__NBA'], 'categories': ['', '']}
    # added 1 category, topic, tag
    # {'action': ['save'], 'draft': ['', '', ''], 'sections': ['', '', '', ''], 'categories': ['8805675__categories__Football', '', ''], 'topics': ['8805675__topics__CFL'], 'tags': ['8805675__tags__Ticats']}

    db = TinyDB('db.json')
    Record = Query()
    print("incoming form data:")
    # print(form_data)
    # print("converted to a dict")
    print(dict(form_data))
    # form data will have keys, values that may be lists or a single string.
    form_data_dict = dict(form_data)
    l = [x for k, v in form_data_dict.items() if k != 'action' for x in v if x]
    changes = []
    index = []
    for x in l:
        asset_id, field, value = x.split("__")
        if asset_id in index:
            d = next(item for item in changes if item["asset_id"] == asset_id)
            if field not in d:
                d[field] = [value]
            else:
                d[field].append(value)
        else:
            index.append(asset_id)
            d = {'asset_id': asset_id}
            d[field] = [value]
            changes.append(d)

            # end result should be: [{'asset_id': xxx, 'draft_user': ['2'], 'topics': ['a', 'b', 'c']}, {{'asset_id': yyy, 'tags': ['e', 'f', 'g']}}]
            print(changes)
            # to update record, loop through changes, get asset_id, delete that k-v, then use rest of dict to update record

        # db.update(post_update, Record.asset_id == asset_id)
        db.close()
        return


def set_value(value_list, value):
    # we will be getting a list of rank values: record-id_new-rank
    # ['8605132_1', '8605133_0', '8605134_0',]
    db = TinyDB('db.json')
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


def set_draft(ids, status=True):
    # Status: ['0'] -> publish, ['1'] -> draft_api, ['2'] -> draft
    # if status True, set to draft, else set to publish
    # given a list of asset_ids, set them to draft or publish depending on status
    db = TinyDB('db.json')
    Record = Query()
    draft = ['2'] if status else ['0']
    for item_id in ids:
        if item_id:
            db.update({'draft_user': draft}, Record.asset_id == item_id)
            print(f"++++++++\nSetting this item: {item_id} to status: {draft}\n++++++++")
    db.close()
    return


def get_record(s_id):
    db = TinyDB('db.json')
    Record = Query()
    record = db.search(Record.asset_id == s_id)
    db.close()
    return record
