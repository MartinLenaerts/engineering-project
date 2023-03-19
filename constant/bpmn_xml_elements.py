from enum import Enum


def get_clean_name(element_name):
    return element_name.replace(BpmnXmlElement.PREFIX.value, "")


class BpmnXmlElement(Enum):
    PREFIX = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"

    MESSAGE = "{}message".format(PREFIX)
    MESSAGE_FLOW = "{}messageFlow".format(PREFIX)
    PARTICIPANT = "{}participant".format(PREFIX)
    PROCESS = "{}process".format(PREFIX)
    LANE_SET = "{}laneSet".format(PREFIX)
    LANE = "{}lane".format(PREFIX)
    FLOW_NODE_REF = "{}flowNodeRef".format(PREFIX)
    START_EVENT = "{}startEvent".format(PREFIX)
    OUTGOING = "{}outgoing".format(PREFIX)
    MESSAGE_EVENT_DEFINITION = "{}messageEventDefinition".format(PREFIX)
    PARALLEL_GATEWAY = "{}parallelGateway".format(PREFIX)
    EXCLUSIVE_GATEWAY = "{}exclusiveGateway".format(PREFIX)
    INCOMING = "{}incoming".format(PREFIX)
    INTERMEDIATE_CATCH_EVENT = "{}intermediateCatchEvent".format(PREFIX)
    TASK = "{}task".format(PREFIX)
    END_EVENT = "{}endEvent".format(PREFIX)
    TERMINATE_EVENT_DEFINITION = "{}terminateEventDefinition".format(PREFIX)
    SEQUENCE_FLOW = "{}sequenceFlow".format(PREFIX)
    EVENT_BASED_GATEWAY = "{}eventBasedGateway".format(PREFIX)
    TIMER_EVENT_DEFINITION = "{}timerEventDefinition".format(PREFIX)
    TIMEDATE = "{}timeDate".format(PREFIX)
    COLLABORATION = "{}collaboration".format(PREFIX)
    BPMN_DIAGRAM = "{http://www.omg.org/spec/BPMN/20100524/DI}BPMNDiagram"
    SUB_PROCESS = "{}subProcess".format(PREFIX)
