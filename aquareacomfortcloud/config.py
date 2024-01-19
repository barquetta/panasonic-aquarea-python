AQUAREA_URL = "https://aquarea-smart.panasonic.com/"
LOGIN_URL = "https://accsmart.panasonic.com/auth/login/"
IDP_TOKEN_URL = "https://accsmart.panasonic.com/auth/idpToken/"
LOGOUT_URL = "https://aquarea-smart.panasonic.com/remote/v1/api/auth/logout"
DEVICE_SET_URL = "https://aquarea-smart.panasonic.com/remote/v1/api/devices/"

LOGOUT_HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "aquarea-smart.panasonic.com",
    "Origin": "https://aquarea-smart.panasonic.com",
    "Referer": "https://aquarea-smart.panasonic.com/remote/a2wControl",
    "User-Agent": "G-RAC",
    "X-Requested-With": "XMLHttpRequest"
}

ACCSMART_HEADERS = {
    "X-APP-TYPE": "1",
    "X-APP-VERSION": "1.19.0",
    "X-APP-TIMESTAMP": "1",
    "X-APP-NAME": "Comfort Cloud",
    "X-CFC-API-KEY": "Comfort Cloud",
    "User-Agent": "G-RAC",
    "Accept": "application/json; charset=utf-8",
    "Content-Type": "application/json; charset=utf-8"
}

AQUAREA_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "aquarea-smart.panasonic.com",
    "User-Agent": "G-RAC",
    "X-Requested-With": "com.panasonic.ACCsmart"
}

DEVICE_SET_HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "aquarea-smart.panasonic.com",
    "Origin": "https://aquarea-smart.panasonic.com",
    "Referer": "https://aquarea-smart.panasonic.com/remote/a2wControl",
    "User-Agent": "G-RAC",
    "X-Requested-With": "XMLHttpRequest"
}

