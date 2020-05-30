class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class TimeOutException(Error):
    def __init__(self):
        self.message = "Timeout"


class MaxDepthException(Error):
    """Exception raised when the maximum exploration depth
    is reached.
    """

    def __init__(self):
        self.message = "Max exploration depth reached"


class MissingTypesError(Error):
    """Exception raised when an user defined class has
    has some missing type annotations.
    """

    def __init__(self, message):
        self.message = message


class RepokNotFoundError(Error):
    """ desc
    """

    def __init__(self, message):
        self.message = message
