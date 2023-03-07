from enum import Enum


class BpmnXmlElement(Enum):
    MESSAGE = "{http://www.omg.org/spec/BPMN/20100524/MODEL}message"
    MESSAGE_FLOW = "{http://www.omg.org/spec/BPMN/20100524/MODEL}messageFlow"
    PARTICIPANT = "{http://www.omg.org/spec/BPMN/20100524/MODEL}participant"
    PROCESS = "{http://www.omg.org/spec/BPMN/20100524/MODEL}process"
    LANE_SET = "{http://www.omg.org/spec/BPMN/20100524/MODEL}laneSet"
    LANE = "{http://www.omg.org/spec/BPMN/20100524/MODEL}lane"
    FLOW_NODE_REF = "{http://www.omg.org/spec/BPMN/20100524/MODEL}flowNodeRef"
    START_EVENT = "{http://www.omg.org/spec/BPMN/20100524/MODEL}startEvent"
    OUTGOING = "{http://www.omg.org/spec/BPMN/20100524/MODEL}outgoing"
    MESSAGE_EVENT_DEFINITION = "{http://www.omg.org/spec/BPMN/20100524/MODEL}messageEventDefinition"
    PARALLEL_GATEWAY = "{http://www.omg.org/spec/BPMN/20100524/MODEL}parallelGateway"
    EXCLUSIVE_GATEWAY = "{http://www.omg.org/spec/BPMN/20100524/MODEL}exclusiveGateway"
    INCOMING = "{http://www.omg.org/spec/BPMN/20100524/MODEL}incoming"
    INTERMEDIATE_CATCH_EVENT = "{http://www.omg.org/spec/BPMN/20100524/MODEL}intermediateCatchEvent"
    TASK = "{http://www.omg.org/spec/BPMN/20100524/MODEL}task"
    END_EVENT = "{http://www.omg.org/spec/BPMN/20100524/MODEL}endEvent"
    TERMINATE_EVENT_DEFINITION = "{http://www.omg.org/spec/BPMN/20100524/MODEL}terminateEventDefinition"
    SEQUENCE_FLOW = "{http://www.omg.org/spec/BPMN/20100524/MODEL}sequenceFlow"
    EVENT_BASED_GATEWAY = "{http://www.omg.org/spec/BPMN/20100524/MODEL}eventBasedGateway"
    TIMER_EVENT_DEFINITION = "{http://www.omg.org/spec/BPMN/20100524/MODEL}timerEventDefinition"
    TIMEDATE = "{http://www.omg.org/spec/BPMN/20100524/MODEL}timeDate"
    COLLABORATION = "{http://www.omg.org/spec/BPMN/20100524/MODEL}collaboration"
    BPMN_DIAGRAM = "{http://www.omg.org/spec/BPMN/20100524/DI}BPMNDiagram"
    SUB_PROCESS = "{http://www.omg.org/spec/BPMN/20100524/MODEL}subProcess"
