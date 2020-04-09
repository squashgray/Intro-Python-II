
class Room:
    def __init__(self,name, description, n_to=None, s_to=None, e_to=None, w_to=None ):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return (f"{self.name}, {self.description}")
    