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

    def __str__(self):
        res = ""
        for process in self.processes:
            res += ("---|" + str(process.name) + "\n")
            for element in process.elements:
                res += ("---|-----" + str(element.name) + "\n")
            for lane in process.lanes:
                res += ("---|----|" + str(lane.name) + "\n")
                for element in lane.elements:
                    res += ("--------|----" + str(element.name) + "\n")

        return res
