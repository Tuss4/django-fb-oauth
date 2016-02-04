class StatusNotOkay(Exception):

    """Should be raised when the status code of a response isn't 200"""

    def __init__(self, value, url):
        self.value = value
        self.request_url = url

    def __str__(self):
        return repr("Non 200 status returned.\nStatus: {}.\nRequest url: {}.".format(
            self.value, self.request_url))
