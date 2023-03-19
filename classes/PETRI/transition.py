from classes.PETRI.petri_element import PetriElement


class Transition(PetriElement):
    def __init__(self, name, t_id, petri_net, color="grey"):
        super().__init__()
        if name == "":
            name = "None"
        self.name = name
        self.id = t_id
        self.color = color
        self.petri_net = petri_net
        for t in petri_net.transitions:
            if (t.name == name and name is not None) or (self.id == t.id):
                raise Exception("❗ ( name : {}, id : {} ) transition already exist ! ❗️".format(self.name, self.id))
        self.petri_net.add_transition(self)

    def __str__(self):
        return {"name": self.name, "id": self.id}.__str__()

    def to_text(self):
        header = "#trans {} \n".format(self.name or self.id)
        in_elements = self.list_elements("in", self.in_elements) + "\n"
        out_elements = self.list_elements("out", self.out_elements) + "\n"
        footer = "#endtr \n"

        return header + in_elements + out_elements + footer

    def list_elements(self, start, array):
        elements = start + "{"

        for element in array:
            elements += "p{}<...>;".format(element.name)

        elements += "}"

        return elements
