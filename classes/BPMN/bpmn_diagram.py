from classes.BPMN.connecting.connection_flow import Connection
from classes.BPMN.flow.flow_object import FlowObject


def print_element(element):
    res = "{} [{}] ".format(element.name, element.element_id)

    if isinstance(element, FlowObject):
        res += " (in: {}  , out: {} )".format(len(element.incoming_elements), len(element.outgoing_elements))

    if isinstance(element, Connection):
        res += "{} (in: {}  , out: {} )".format(element.__class__.__name__, element.source.name,
                                                element.target.name)

    return res


class BpmnDiagram:
    def __init__(self):
        self.processes = []
        self.elements = []

    def append_process(self, process):
        self.processes.append(process)

    def append_element(self, element):
        self.elements.append(element)

    def get_start_event(self):
        events = []
        for element in self.elements:
            class_name = element.__class__.__name__
            if class_name == "StartEvent":
                events.append(element)
        for process in self.processes:
            for element in process.elements:
                class_name = element.__class__.__name__
                if class_name == "StartEvent":
                    events.append(element)
            for lane in process.lanes:
                for element in lane.elements:
                    class_name = element.__class__.__name__
                    if class_name == "StartEvent":
                        events.append(element)
        return events

    def get_all_elements_flat(self):
        elements = []
        for process in self.processes:
            for element in process.elements:
                elements.append(element)
            for lane in process.lanes:
                for element in lane.elements:
                    elements.append(element)

        for element in self.elements:
            elements.append(element)

        return elements

    def __str__(self):
        res = ""
        for process in self.processes:
            res += ("---|" + str(process.name) + "\n")
            for element in process.elements:
                res += ("---|-----" + print_element(element) + "\n")
            for lane in process.lanes:
                res += ("---|----|" + str(lane.name) + "\n")
                for element in lane.elements:
                    res += ("--------|----" + print_element(element) + "\n")

        for element in self.elements:
            res += ("-" + print_element(element) + "\n")

        return res
