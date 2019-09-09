# -*- coding: utf-8 -*-

from flask import Flask
from room_status import RoomStatus
from flask_cors import CORS
import os
app = Flask(__name__) 
CORS(app)
app.secret_key = os.environ.get('SECRET_KEY', 'some-secret-key')
room_status = RoomStatus()
