from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
# WE NEED: get_message() & set_message()

class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self._message = ""

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

