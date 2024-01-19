import requests
import json
from . import config
from . import validation
import os

class AquareaSession:
    def __init__(self, user_email, user_password, token_file_name='~/.panasonic-token'):
        self.user_email = user_email
        self.user_password = user_password
        self.user_token = None
        self.idp_token = None
        self.session_cookies_map = {}
        self.token_file_name = os.path.expanduser(token_file_name)

    def login(self):
        self._get_user_token()
        try:
            self._get_idp_token()
        except validation.ResponseError as ex:
            if ex.status_code == 401:
                # User token expired perhaps, so let's clear the session and log-in again
                self._handle_token_expired()
            else:
                raise validation.ResponseError(ex.status_code, ex.text)
        

    def logout(self):
        if len(self.session_cookies_map) > 0:
            headers = config.LOGOUT_HEADERS
            cookies = next(iter(self.session_cookies_map.values()), None)
            headers["Cookie"] = "; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
            self._clear_session()
            response = requests.post(config.LOGOUT_URL, headers=headers)
            validation.validate_response(response)
        else:
            self._clear_session()
        
    
    def get_session_cookies(self, device_guid):
        if device_guid not in self.session_cookies_map:
            data = {
                "X-Authorization": self.idp_token,
                "cfcLoginMode": "1",
                "gwid": device_guid
            }
            response = requests.post(config.AQUAREA_URL, headers=config.AQUAREA_HEADERS, data=data)

            validation.validate_response(response)

            self.session_cookies_map[device_guid] = response.cookies
        return self.session_cookies_map[device_guid]
    
    def _get_user_token(self):
        if self.user_token is None:
            if os.path.exists(self.token_file_name):
                with open(self.token_file_name, 'r') as tokenFile:
                    self.user_token = tokenFile.read().strip()
            if self.user_token is None or self.user_token == "":
                # The token must be obtained from the server
                data = {
                    "language": 0,
                    "loginId": self.user_email,
                    "password": self.user_password
                }

                response = requests.post(config.LOGIN_URL, headers=config.ACCSMART_HEADERS, json=data)
                
                validation.validate_response(response)
                
                self.user_token = json.loads(response.text)['uToken']
                with open(self.token_file_name, 'w') as tokenFile:
                    tokenFile.write(self.user_token)
                    

    def _get_idp_token(self):
        headers = config.ACCSMART_HEADERS
        headers["X-User-Authorization"] = self.user_token

        response = requests.get(config.IDP_TOKEN_URL, headers=headers)
        
        validation.validate_response(response)

        self.idp_token = json.loads(response.text)['idpToken']

    def _clear_session(self):
        self.user_token = None
        self.idp_token = None
        self.session_cookies_map.clear()
        os.remove(self.token_file_name)
    
    def _handle_token_expired(self):
        self._clear_session()
        self._get_user_token()
        self._get_idp_token()