class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class MaxDepthException(Error):
    """Exception raised when the maximum exploration depth
    is reached.
    """

    def __init__(self):
        self.message = "Max exploration depth reached"


class MissingTypesError(Error):
    """Exception raised when an user defined class has
    no docstring on his init method.
    """

    def __init__(self, message):
        self.message = message


class UnsatBranchError(Error):
    """Exception raised when a branch is not satisfacible.
    """

    def __init__(self):
        self.message = "Unsat branch"


class RepOkFailException(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
        cls -- Class
    """

    def __init__(self, message, cls):
        self.message = message


class ReturnValueRepOkFail(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "The returned value does not pass the repok()"
