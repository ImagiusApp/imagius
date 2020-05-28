# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Application Data Initialization
"""
import sys
from pathlib import Path, PureWindowsPath
from imagius.constants import APP_NAME, DB_SETTINGS, DB_META, APP_VERSION
from imagius.exceptions import AppDataDirReadWriteFailed
from imagius.util import user_app_data_dir, meta_db_path, settings_db_path, eprint


def init_app_data_dir():
    p = Path(user_app_data_dir())
    if not p.exists():
        try:
            p.mkdir(exist_ok=True)
        except:
            eprint('Unable to access or create application data location: %s' %
                   user_app_data_dir())
            raise AppDataDirReadWriteFailed


def init_app_db():
    init_meta_db()
    init_settings_db()


def init_meta_db():
    from imagius.db import dbmgr
    p = Path(meta_db_path())
    if not p.exists():
        db = dbmgr(p)
        db.create_meta_db_from_schema()


def init_settings_db():
    from imagius.db import dbmgr
    p = Path(settings_db_path())
    if not p.exists():
        db = dbmgr(p)
        db.create_settings_db_from_schema()

        # Add the current version info
        db.connect()
        query = 'INSERT INTO settings (key, value) VALUES (?, ?)'
        params = ('VERSION', APP_VERSION)
        db.run_insert_query(query, params)
        db.disconnect()
