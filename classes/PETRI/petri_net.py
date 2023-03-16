class PetriNet:
    def __init__(self):
        self.places = []
        self.transitions = []
        self.arcs = []
        self.sub_nets = []

    def add_place(self, place):
        self.places.append(place)

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_arc(self, arc):
        self.arcs.append(arc)

    def add_sub_net(self, sub_net):
        self.sub_nets.append(sub_net)

    def get_all_places(self):
        all_places = self.places

        for sub_net in self.sub_nets:
            all_places += sub_net.get_all_places()

        return all_places

    def __str__(self):
        return "Petri Net with {} places, {} transitions, {} arcs".format(len(self.places),
                                                                          len(self.transitions),
                                                                          len(self.arcs))
