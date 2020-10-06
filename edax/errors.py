"""
Library-wise errors
"""


class EDAXError(Exception):
    """
    Base exception, used library-wise
    """


class UnreachableError(EDAXError):
    """
    Error indicating some path of the code is unreachable.
    """
