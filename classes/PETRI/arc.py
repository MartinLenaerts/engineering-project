from classes.PETRI.petri_element import PetriElement


class Arc(PetriElement):
    def __init__(self, source, target, petri_net, weight=1):
        self.source = source
        self.target = target
        self.weight = weight
        self.petri_net = petri_net
        self.petri_net.add_arc(self)

    def __str__(self) -> str:
        return {"source": self.source.__str__(), "target": self.target.__str__()}.__str__()
