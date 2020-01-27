class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class MaxDepthException(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "Max exploration depth reached"


class ClassNotDocumentedError(Error):
    """Exception raised when an user defined class has
    no docstring on his init method.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, the_class):
        self.the_class = the_class
        self.message = "Docstring not found in: " + the_class.__name__


class UnsatBranchError(Error):
    """Exception raised when a branch is not satisfacible.

    Attributes:
        message -- explanation of the error
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

    def __init__(self, cls):
        self.message = str(cls) + "repok fail"


class ReturnValueRepOkFail(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "The returned value does not pass the repok()"
