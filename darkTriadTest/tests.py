from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(DarkTriadPage, timeout_happened=True)
