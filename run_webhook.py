# -*- coding: utf-8 -*-
'''
Created on 2016年10月20日

@author: hustcc
'''

from app import app
from app import socketio

if __name__ == '__main__':
#     app.run('0.0.0.0', 18340, debug=True,  threaded=True)
    socketio.run(app, host='0.0.0.0', port=18340, debug=True)
