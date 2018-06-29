config = {
    # could reduce db name to just project_name.json
    "project_name":
    "ticats",
    "name":
    "spec",
    "db_name":
    "ticats.json",
    "db_fields_dflt": {
        'desc_user': '',
        'draft_user': 0,  # int 0:published, 1-2: draft
        'rank': 0,  # int
        'rank_time': 0,  # int
        'label_user': '',
        'title_user': '',
        'tags_user': [],  # list of strings
    },
    "db_fields": [
        'asset_id', 'author_api', 'caption_api', 'categories_api', 'label_api',
        'source_api', 'desc_api', 'draft_api', 'link', 'img_api',
        'img_api_thumb', 'pubdate_api', 'region_api', 'site_api', 'tags_api',
        'timestamp', 'title_api'
    ],
    "apis": [
        {
            "url":
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=ticats&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
            "filter": ["searchResultView"]
        },
        {
            "url":
            'http://api.zuza.com/search/article/default?&category=sports&subcategory=football&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
            "filter": ["searchResultView"]
        },
        {
            "url":
            'http://api.zuza.com/search/article/default?guid=346a9bb4-5f2b-4838-b632-4abcc516eeca&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            "filter": ["searchResultView"]
        },
        {
            "url":
            'http://api.zuza.com/search/article/default?guid=ad33da77-38f2-42fc-ba36-392490bee98b&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5&startindex=1&endindex=5',
            "filter": ["searchResultView"]
        },
    ],
    "munge": [],
    "section_list": ["Ticats", "CFL"],
    "tag_list": ["BC", "CGY", "EDM", "MTL", "OTT", "TOR", "SSK", "WPG", "Opinion", "Gameday", "Profile", "Feature", "League"],
    "schedule": [
        {"name": "Week 1", "games": ["June 14: EDM 33 @ WPG 30", "June 15: TOR 19 @ SSK 27", "June 16: HAM 14 @ CGY 28", "June 16: MTL 10 @ BC 22"], "end": ""},
        {"name": "Week 2", "games": ["June 21: SSK 17 @ OTT 40", "June 22: WPG 56 @ MTL 10", "June 22: HAM 38 @ EDM 21", "June 23: CGY 41 @ TOR 7"], "end": ""},
        {"name": "Week 3", "games": ["June 28: OTT @ CGY 9pm", "June 29: WPG @ HAM 7pm", "June 29: BC @ EDM 10pm", "June 30: MTL @ SSK 9pm"], "end": ""},
    ]
}

# BY KEYWORD
# http://api.zuza.com/search/article/default?q=KeywordsAlias:”XXXXX"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5
# BY CATEGORY/SUBCATEGORY
# http://api.zuza.com/search/article/default?&category=XXXX&subcategory=XXXX&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# BY AUTHOR: where guid: is author page key.
# http://api.zuza.com/search/article/default?guid=25a2fb14-ae69-41f2-beab-bdda47383f93&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=5