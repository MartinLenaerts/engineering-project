class Lane:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element.value)
