from classes.PETRI.petri_element import PetriElement


class Place(PetriElement):
    def __init__(self, name, p_id, petri_net):
        super().__init__()
        self.id = p_id
        self.name = name
        self.tokens = 0
        self.petri_net = petri_net
        for p in petri_net.places:
            if p.name == name:
                raise Exception("❗ '{}' place already exist ! ❗️".format(name))
        self.petri_net.add_place(self)

    def add_token(self):
        self.tokens += 1

    def remove_token(self):
        self.tokens -= 1

    def __str__(self):
        return {"name": self.name, "id": self.id}.__str__()

    def to_text(self):
        return "#place p{} \n".format(self.name)
