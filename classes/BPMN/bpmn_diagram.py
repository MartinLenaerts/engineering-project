class BpmnDiagram:
    def __init__(self):
        self.processes = []
        self.elements = []

    def append_process(self, process):
        self.processes.append(process)

    def append_element(self, element):
        self.elements.append(element)

    def __str__(self):
        res = ""
        for process in self.processes:
            res += ("---|"+str(process.name)+"\n")
            for element in process.elements:
                res += ("---|-----" + str(element.name) + "\n")
            for lane in process.lanes:
                res += ("---|----|"+str(lane.name)+"\n")
                for element in lane.elements:
                    res += ("--------|----"+str(element.name)+"\n")

        return res
