import requests
from . import config
from . import validation

class NotImplementedYetError(Exception):
    pass

class AquareaDevice:
    def __init__(self, device_guid, session_instance):
        self.device_guid = device_guid
        self.login_instance = session_instance

    def set(self, data):
        session_cookies = self.login_instance.get_session_cookies(self.device_guid)
        selected_device_id = session_cookies.get('selectedDeviceId', None)

        url = config.DEVICE_SET_URL + selected_device_id
        headers = config.DEVICE_SET_HEADERS
        headers["Cookie"] = "; ".join([f"{cookie.name}={cookie.value}" for cookie in session_cookies])
        
        response = requests.post(url, headers=headers, json=data)
        
        validation.validate_response(response)

        return response
    
    def get(self, data):
        raise NotImplementedYetError("This method is not implemented yet.")