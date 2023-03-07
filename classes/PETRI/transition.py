class Transition:
    def __init__(self, name):
        if name == "":
            name = "None"
        self.name = name

    def __str__(self):
        return self.name
