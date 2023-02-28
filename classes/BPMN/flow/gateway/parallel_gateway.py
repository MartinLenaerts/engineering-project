from classes.BPMN.flow.gateway.gateway import Gateway
from constant.gateway_type import GatewayType


class ParallelGateway(Gateway):

    def __init__(self, xml_element):
        super().__init__(xml_element, GatewayType.PARALLEL)
