from classes.BPMN.flow.gateway.gateway import Gateway
from constant.gateway_type import GatewayType


class EventBasedGateway(Gateway):

    def __init__(self, element_id, name):
        super().__init__(element_id, name, GatewayType.EVENT_BASED)