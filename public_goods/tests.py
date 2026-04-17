from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            yield Instructions

            if self.subsession.instructions_relues:
                yield Submission(InstructionsWaitMonitor, check_html=False)

        yield Submission(Decision, timeout_happened=True)

        yield Results

        if self.player.round_number == C.NUM_ROUNDS:
            yield Final
