class Transition:
    def __init__(self, name, t_id, color="grey"):
        if name == "":
            name = "None"
        self.name = name
        self.id = t_id
        self.color = color

    def __str__(self):
        return self.name
