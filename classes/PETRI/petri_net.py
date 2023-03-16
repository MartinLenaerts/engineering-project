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
        return "Petri Net with {} places, {} transitions, {} arcs".format(len(self.places),
                                                                          len(self.transitions),
                                                                          len(self.arcs))
