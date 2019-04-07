class ItemError(Exception):

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

class OrderError(Exception):
    
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

class SystemError(Exception):

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message