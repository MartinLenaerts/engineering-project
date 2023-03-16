from classes.PETRI.petri_element import PetriElement


class Place(PetriElement):
    def __init__(self, name, p_id, petri_net):
        self.id = p_id
        self.name = name
        self.tokens = 0
        self.petri_net = petri_net
        self.petri_net.add_place(self)

    def add_token(self):
        self.tokens += 1

    def remove_token(self):
        self.tokens -= 1

    def __str__(self):
        return {"name": self.name, "id": self.id}.__str__()
