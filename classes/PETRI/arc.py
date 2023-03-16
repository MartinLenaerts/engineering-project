from classes.PETRI.petri_element import PetriElement


class Arc(PetriElement):
    def __init__(self, source, target, weight=1):
        self.source = source
        self.target = target

        self.weight = weight
