from classes.PETRI.petri_element import PetriElement


class Arc(PetriElement):
    def __init__(self, source, target, petri_net, weight=1):
        super().__init__()
        self.source = source
        self.target = target
        self.weight = weight
        self.petri_net = petri_net
        self.petri_net.add_arc(self)

        self.source.out_elements.append(self.target)
        self.target.in_elements.append(self.source)

    def __str__(self) -> str:
        return {"source": self.source.__str__(), "target": self.target.__str__()}.__str__()
