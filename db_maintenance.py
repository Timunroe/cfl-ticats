import config as cfg
from tinydb import TinyDB, Query
# from operator import itemgetter
import datetime


def set_expire():
    db = TinyDB(cfg.config['db_name'])
    Record = Query()
    for record in db.all():
        if 'timestamp_epoch' not in record:
            date_object = datetime.datetime.strptime(record['pubdate_api'], '%Y-%m-%dT%H:%M:%S')
            timestamp_epoch = int((date_object - datetime.datetime(1970, 1, 1)).total_seconds())
            db.update({'timestamp_epoch': timestamp_epoch}, Record.asset_id == record['asset_id'])


set_expire()
