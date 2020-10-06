"""EDAx"""
import logging
from .eda import *

DEFAULT_PARTITIONS = 1

logging.basicConfig(level=logging.INFO, format="%(message)s")

__version__ = "0.2.13"
