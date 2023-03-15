class ElementsGroup:
    def __init__(self, element_id):
        self.elements = []
        self.id = element_id

    def add_element(self, element):
        self.elements.append(element)

    def get_start_element(self):
        return self.elements[0]

    def get_end_element(self):
        return self.elements[len(self.elements) - 1]
