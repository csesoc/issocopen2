# -*- coding: utf-8 -*-

def autheticate_key(server_key: str, user_key: str) -> bool:
    if server_key != user_key:
        raise AuthenticationError()
    return True

def generate_error_resp_body(status_code: int, error_msg):
    '''
    this function generates the response body as a dict
        statusCode: HTTP_STATUS_CODE
        message: TEXT_MESSAGE
    '''
    return {
        "statusCode": status_code,
        "message": error_msg
    }

def parse_request(request):
    '''
    this function validates the request that user POSTed
    '''
    data = {}
    MAX_ALLOWED_LENGTH = 38
    if request.content_length > MAX_ALLOWED_LENGTH:
        raise InvaildRequestError()
        
    request.get_data(parse_form_data=True)

    if 'clientID' not in request.headers:
        raise InvaildRequestError()

    body_tags = ('doorClosed','peopleInside')
    for tag in body_tags:
        if tag not in request.form.keys():
            raise InvaildRequestError()
        if request.form[tag] != 'True' and request.form[tag] != 'False':
            raise InvaildRequestError()
        else:
            data[tag] = True if request.form[tag] == 'True' else False
    
    return data
    
class AuthenticationError(Exception):
    def __init__(self):
        self._msg = "Invalid Key"

    @property
    def message(self):
       return self._msg

class InvaildRequestError(Exception):
    def __init__(self):
        self._msg = "Invaild Request"

    @property
    def message(self):
        return self._msg