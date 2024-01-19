class ResponseError(Exception):
    ''' Unexcpected response '''
    def __init__(self, status_code, text):
        super(ResponseError, self).__init__(
            'Invalid response'
            ', status code: {0} - Data: {1}'.format(
                status_code,
                text))
        self.status_code = status_code
        self.text = text

def validate_response(response):
    """ Verify that response is OK """
    if response.status_code == 200:
        return
    raise ResponseError(response.status_code, response.text)