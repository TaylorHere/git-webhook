# -*- coding: utf-8 -*-
'''
Created on 2016-10-28
push message to front-end useing socketio
@author: hustcc
'''

from app.utils import JsonUtil
from app import config


def push_webhook_status(data):
    '''when webhook status changed'''
    _push_data('webhook_status', data)


def push_new_history(data):
    '''when a new push event is hooked'''
    _push_data('new_history', data)


def push_history_status(data):
    '''when history status changed'''
    _push_data('history_status', data)


def _push_data(type, data):
    if not data or not type:
        pass
    data = JsonUtil.object_2_json({'type': type, 'data': data})
    # request websocket to push msg
    requests.post(config.BASE_URL + '/ws/send', {'data': data})
