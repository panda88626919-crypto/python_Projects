from pip._internal import self_outdated_check


class parent:
    hair_color = "Brown"
    speaks = "English"

class child(parent):
    def __init__ (self, hair_color):
        super().__init__()
        hair_color = "Black"
        self.hair_color = hair_color
        self.speak = parent.speaks + ["German"]
