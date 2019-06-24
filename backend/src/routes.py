# -*- coding: utf-8 -*-
from server import app, room_status
from flask import jsonify, request
from helper_func import *

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == "GET":
        resp_body = {
            "roomStatus": room_status.get_room_status(),
            "doorStatus": room_status.door_status,
            "isEmpty": room_status.is_people_inside,
            "lastUpdateTime": room_status._timestamp
        }

        return jsonify(resp_body)

    elif request.method == 'POST':
        secret_key = 'some-secret-key'  # hash key will be regenerated in production environment
        request_data = None
        # validate the request
        try:
           request_data = parse_request(request)
        except InvaildRequestError as e:
            return jsonify(generate_error_resp_body(400, e.message)), 400
            
        # authenticate request
        user_key = request.headers['clientID']
        try:
            autheticate_key(secret_key, user_key)
        except AuthenticationError as e:
           return jsonify(generate_error_resp_body(401, e.message)), 401

        room_status.set_is_door_closed(request_data['doorClosed'])
        room_status.set_people_status(request_data['peopleInside'])

        return jsonify(status='success')

# handles page 404
@app.errorhandler(404)
def not_found(e):
    resp_body = {
        'status': 404,
        'message': "Requested resource not found"
    }
    return jsonify(resp_body),404 
    