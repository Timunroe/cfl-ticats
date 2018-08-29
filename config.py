config = {
    "db_name": "db.json",
    "db_fields_dflt": {
        'desc_user': '',
        #  TODO: Use ints or strings? Forms always return strings!!! IN LISTS!!! Easier to use strings and convert if needed.
        'draft_user': '0',  # str 0:published, 1-2: draft
        'rank': '0',  # str
        'rank_time': '0',  # str
        'label_user': '',
        'title_user': '',
        'sections_user': [],  # will always be a list from source
        'categories_user': [],  # either a list or does not exist from source
        'topics_user': [],  # list of strings
        'tags_user': [],  # list of strings
    },
    # section -> category -> topic -> tags
    "db_fields": [
        'asset_id', 'author_api', 'caption_api', 'categories_api', 'label_api',
        'source_api', 'desc_api', 'draft_api', 'link', 'img_api',
        'img_api_thumb', 'pubdate_api', 'region_api', 'sections_api', 'site_api', 'tags_api',
        'timestamp', 'title_api', 'topics_api'
    ],
    "apis": {
        "default" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ],
        "cfl" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=ticats&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=5',
                "filter": ["searchResultView"]
            },
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=football&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=10',
                "filter": ["searchResultView"]
            },
            {
                "url":
                'http://api.zuza.com/search/article/default?guid=346a9bb4-5f2b-4838-b632-4abcc516eeca&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=5',
                "filter": ["searchResultView"]
            },
            {
                "url":
                'http://api.zuza.com/search/article/default?guid=ad33da77-38f2-42fc-ba36-392490bee98b&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=5',
                "filter": ["searchResultView"]
            },
        ],
        "nfl" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=football&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ],
        "nhl" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=hockey&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ],
        "mlb" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=baseball&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ],
        "mls" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=soccer&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ],
        "nba" : [
            {
                "url":
                'http://api.zuza.com/search/article/default?&category=sports&subcategory=basketball&pageIndex=1&location=hamilton&sort=datedesc&pageSize=1&startindex=1&endindex=20',
                "filter": ["searchResultView"]
            },
        ]
    },
    "munge": [],
    # section -> category -> topic -> tags
    "schedule": [
        {
            "name":
            "Week 1",
            "games": [
                "June 14: EDM 33 @ WPG 30", "June 15: TOR 19 @ SSK 27",
                "June 16: HAM 14 @ CGY 28", "June 16: MTL 10 @ BC 22"
            ],
            "end":
            ""
        },
        {
            "name":
            "Week 2",
            "games": [
                "June 21: SSK 17 @ OTT 40", "June 22: WPG 56 @ MTL 10",
                "June 22: HAM 38 @ EDM 21", "June 23: CGY 41 @ TOR 7"
            ],
            "end":
            ""
        },
        {
            "name":
            "Week 3",
            "games": [
                "June 28: OTT @ CGY 9pm", "June 29: WPG @ HAM 7pm",
                "June 29: BC @ EDM 10pm", "June 30: MTL @ SSK 9pm"
            ],
            "end":
            ""
        },
    ],
}

# BY KEYWORD
# http://api.zuza.com/search/article/default?q=KeywordsAlias:”XXXXX"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5
# BY CATEGORY/SUBCATEGORY
# http://api.zuza.com/search/article/default?&category=XXXX&subcategory=XXXX&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# BY AUTHOR: where guid: is author page key.
# http://api.zuza.com/search/article/default?guid=25a2fb14-ae69-41f2-beab-bdda47383f93&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=5
