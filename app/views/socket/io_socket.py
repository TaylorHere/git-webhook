# -*- coding: utf-8 -*-
'''
Created on 2016-10-28

@author: hustcc
'''

from app import socketio, app
from app.utils import RequestUtil
from flask.globals import request


# broadcast data to frontend
@app.route('/ws/send', methods=['POST', 'GET'])
def websocket_send():
    data = RequestUtil.get_parameter('data', '')
    socketio.emit('ws', data, broadcast=True)
    return 'ws.'


@socketio.on_error()
def error_handler(e):
    pass
