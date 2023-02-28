from enum import Enum


class GatewayType(Enum):
    EXCLUSIVE = 'EXCLUSIVE'
    PARALLEL = 'PARALLEL'
    INCLUSIVE = 'INCLUSIVE'
    EVENT_BASED = 'EVENT_BASED'
