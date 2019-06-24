# -*- coding: utf-8 -*-

from flask import Flask
from room_status import RoomStatus
from flask_cors import CORS
app = Flask(__name__) 
CORS(app)
app.secret_key = '43c75ba1997338c3e6daf0c003c6bfedd0c4da2e72b1d5a7e019d62420de72df'
room_status = RoomStatus()
