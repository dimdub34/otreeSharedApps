from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(MachPage, timeout_happened=True)
