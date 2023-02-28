












class Process(BpmnElement):
    def __init__(self, name):
        super().__init__(name)


class Task(BpmnElement):
    def __init__(self, name):
        super().__init__(name)


class Gateway(BpmnElement):
    def __init__(self, name):
        super().__init__(name)


def transform_to_petri_net(bpmn_model):
    petri_net = PetriNet()

    for element in bpmn_model:
        if isinstance(element, Process):
            place = Place(element.name)
            petri_net.add_place(place)
        elif isinstance(element, Task):
            transition = Transition(element.name)
            petri_net.add_transition(transition)
        elif isinstance(element, Gateway):
            # handle gateway
            pass

    return petri_net
