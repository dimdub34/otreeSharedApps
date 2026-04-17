from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(Hexaco, timeout_happened=True)
