class Place:
    def __init__(self, name, p_id):
        self.id = p_id
        self.name = name
        self.tokens = 0

    def add_token(self):
        self.tokens += 1

    def remove_token(self):
        self.tokens -= 1

    def __str__(self):
        return self.name
