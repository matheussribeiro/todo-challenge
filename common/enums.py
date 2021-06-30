from enum import Enum

class EnvironmentSet(str, Enum):
    DEVELOPMENT = 'DEVELOPMENT'
    PRODUCTION = 'PRODUCTION'
    TEST = 'TEST'
