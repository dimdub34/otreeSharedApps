from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Instructions
        yield Submission(Decision, timeout_happened=True, check_html=False)
        yield Results
