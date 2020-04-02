class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class MaxDepthException(Error):
    """Exception raised when the maximum exploration depth
    is reached.
    """

    def __init__(self):
        self.message = "Max exploration depth reached"


class MaxRecursionException(Error):
    """Exception raised when the maximum recursion depth
    is reached.
    """

    def __init__(self):
        self.message = "Max exploration recursion reached"


class MissingTypesError(Error):
    """Exception raised when an user defined class has
    has some missing type annotations.
    """

    def __init__(self, message):
        self.message = message


class UnsatBranchError(Error):
    """Exception raised when a branch is not satisfacible.
    """

    def __init__(self):
        self.message = "Unsat branch"


class RepOkFailException(Error):
    """
    """

    def __init__(self):
        self.message = "Repok Fail"


class CouldNotBuildError(Error):
    """
    """

    def __init__(self):
        self.message = "Could not build the complete structure"


class ReturnValueRepOkFail(Error):
    """
    """

    def __init__(self):
        self.message = "The returned value does not pass the repok()"


class RepokNotFoundError(Error):
    """ desc
    """

    def __init__(self, message):
        self.message = message
