class Place:
    def __init__(self, name):
        self.name = name
        self.tokens = 0

    def add_token(self):
        self.tokens += 1

    def remove_token(self):
        self.tokens -= 1

    def __str__(self):
        return self.name


class Transition:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Arc:
    def __init__(self, source, target, weight=1):
        self.source = source
        self.target = target
        self.weight = weight


class PetriNet:
    def __init__(self):
        self.places = []
        self.transitions = []
        self.arcs = []

    def add_place(self, place):
        self.places.append(place)

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_arc(self, arc):
        self.arcs.append(arc)

    def __str__(self):
        return "Petri Net with {} places and {} transitions".format(len(self.places), len(self.transitions))


class BpmnElement:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


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
