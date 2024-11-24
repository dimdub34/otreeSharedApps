import random

from otree.api import *
from pathlib import Path

app_name = Path(__file__).parent.name

doc = """
Mesure de l'attitude au risque selon la méthode de Binswanger (1980), reprise par Eckel & Grossman (2002, 2008) <br>
Les valeurs des lotteries sont issues du papier : <br>
Dave, C., Eckel, C.C., Johnson, C.A. et al. Eliciting risk preferences: When is simple better?. J Risk Uncertain 41, 
219–243 (2010). https://doi.org/10.1007/s11166-010-9103-z <br>
Les valeurs sont divisées par 10 pour représenter des Euros (en tâche de contrôle).
"""


class C(BaseConstants):
    NAME_IN_URL = 'biswanger'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    LOTERIES = {
        1: (2.8, 2.8), 2: (2.4, 3.6), 3: (2.0, 4.4), 4: (1.6, 5.2), 5: (1.2, 6.0), 6: (0.2, 7.0)
    }
    NUM_LOTERIES = len(LOTERIES)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(choices=list(C.LOTERIES.keys()))
    lottery_randomVal = models.IntegerField(
        doc="If random value <= 50 the payoff is equal to the left value in the chosen lottery, otherwise it is "
            "equal to the right one.")

    def compute_payoff(self):
        self.lottery_randomVal = random.randint(1, 100)
        self.payoff = cu(C.LOTERIES[self.lottery_choice][self.lottery_randomVal > 50])
        txt_final = (f"Vous avez choisi la lottery {self.lottery_choice} : 50 % de chances de gagner "
                     f"{cu(C.LOTERIES[self.lottery_choice][0])} et 50 % de chances de gagner "
                     f"{cu(C.LOTERIES[self.lottery_choice][1])}. <br>"
                     f"Suite au tirage au sort, votre gain est de {self.payoff}.")
        self.participant.vars[app_name] = dict(txt_final=txt_final, payoff=self.payoff)


# ======================================================================================================================
#
# PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Decision(MyPage):
    form_model = "player"
    form_fields = ["lottery_choice"]

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False)
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.lottery_choice = random.choice(list(C.LOTERIES.keys()))
        player.compute_payoff()

class Result(MyPage):
    pass


page_sequence = [Decision, Result]
