__author__ = 'luke.beer'

from enum import Enum


class State(Enum):
    INIT = 'INIT'
    IDLE = 'IDLE'
    ARCHIVE = 'ARCHIVE'
    COMPRESS = 'COMPRESS'
    COLLECT = 'COLLECT'
    WAITING = 'WAITING'
