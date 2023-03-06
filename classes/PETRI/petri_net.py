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
        already_exist = False
        source = arc.source.name
        target = arc.target.name
        for current_arc in self.arcs:
            if current_arc.source.name == source and current_arc.target.name == target:
                already_exist = True

        if not already_exist:
            self.arcs.append(arc)
            return True

        return False

    def __str__(self):
        return "Petri Net with {} places, {} transitions, {} arcs".format(len(self.places),
                                                                          len(self.transitions),
                                                                          len(self.arcs))
