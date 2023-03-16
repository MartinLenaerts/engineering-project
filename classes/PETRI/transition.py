from classes.PETRI.petri_element import PetriElement


class Transition(PetriElement):
    def __init__(self, name, t_id, petri_net, color="grey"):
        if name == "":
            name = "None"
        self.name = name
        self.id = t_id
        self.color = color
        self.petri_net = petri_net
        self.petri_net.add_transition(self)

    def __str__(self):
        return {"name": self.name, "id": self.id}.__str__()
