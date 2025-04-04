import random
import numpy as np
from otree.api import *
from pathlib import Path

app_name = Path(__file__).parent.name

doc = """
Social Value Orientation - 6 matrices <br>
Murphy, R. O., Ackermann, K. A., & Handgraaf, M. J. J. (2011). Measuring Social Value Orientation. 
Judgment and Decision Making, 6(8), 771-781.
"""


class C(BaseConstants):
    NAME_IN_URL = 'svo'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    matrices = [
        [(85, 85), (85, 76), (85, 68), (85, 59), (85, 50), (85, 41), (85, 33), (85, 24), (85, 15)],
        [(85, 15), (87, 19), (89, 24), (91, 28), (93, 33), (94, 37), (96, 41), (98, 46), (100, 50)],
        [(50, 100), (54, 98), (59, 96), (63, 94), (68, 93), (72, 91), (76, 89), (81, 87), (85, 85)],
        [(50, 100), (54, 89), (59, 79), (63, 68), (68, 58), (72, 47), (76, 36), (81, 26), (85, 15)],
        [(100, 50), (94, 56), (88, 63), (81, 69), (75, 75), (69, 81), (63, 88), (56, 94), (50, 100)],
        [(100, 50), (98, 54), (96, 59), (94, 63), (93, 68), (91, 72), (89, 76), (87, 81), (85, 85)]
    ]

    conversion_rate = 0.05


# ======================================================================================================================
#
# -- SUBSESSION
#
# ======================================================================================================================
class Subsession(BaseSubsession):
    pass


# ======================================================================================================================
#
# -- GROUP
#
# ======================================================================================================================
class Group(BaseGroup):
    selected_choice = models.IntegerField()
    selected_player = models.IntegerField()
    selected_player_decision_self = models.IntegerField()
    selected_player_decision_other = models.IntegerField()


def compute_payoffs(group: Group):
    group.selected_choice = random.randint(1, 6)
    group.selected_player = random.randint(1, 2)
    group.selected_player_decision_self = getattr(group.get_player_by_id(group.selected_player),
                                                  f"svo_choice_{group.selected_choice}_self")
    group.selected_player_decision_other = getattr(group.get_player_by_id(group.selected_player),
                                                   f"svo_choice_{group.selected_choice}_other")

    for p in group.get_players():
        compute_payoff(p)


# ======================================================================================================================
#
# -- PLAYER
#
# ======================================================================================================================

class Player(BasePlayer):
    svo_choice_1_self = models.IntegerField()
    svo_choice_1_other = models.IntegerField()
    svo_choice_2_self = models.IntegerField()
    svo_choice_2_other = models.IntegerField()
    svo_choice_3_self = models.IntegerField()
    svo_choice_3_other = models.IntegerField()
    svo_choice_4_self = models.IntegerField()
    svo_choice_4_other = models.IntegerField()
    svo_choice_5_self = models.IntegerField()
    svo_choice_5_other = models.IntegerField()
    svo_choice_6_self = models.IntegerField()
    svo_choice_6_other = models.IntegerField()
    svo_mean_self = models.FloatField()
    svo_mean_other = models.FloatField()
    svo_score = models.FloatField()


def compute_score(player: Player):
    values_player, values_other = [], []
    for i in range(1, len(C.matrices) + 1):
        values_player.append(getattr(player, f"svo_choice_{i}_self"))
        values_other.append(getattr(player, f"svo_choice_{i}_other"))
    player.svo_mean_self = np.round(np.mean(values_player), 3)
    player.svo_mean_other = np.round(np.mean(values_other), 3)
    player.svo_score = np.round(
        np.degrees(
            np.arctan((player.svo_mean_other - 50) / (player.svo_mean_self - 50))
        ), 3)


def compute_payoff(player: Player):
    txt_final = f"C'est le tableau {player.group.selected_choice} qui a été aléatoirement sélectionné. <br>"
    if player.group.selected_player == player.id_in_group:
        player.payoff = cu(player.group.selected_player_decision_self * C.conversion_rate)
        txt_final += (f"C'est votre répartition qui s'est appliquée dans la paire. Vous avez choisi un montant de "
                      f"{player.group.selected_player_decision_self} ECU pour vous et de "
                      f"{player.group.selected_player_decision_other} ECU pour l'autre joueur. Vous gagnez donc "
                      f"{player.payoff}  et l'autre joueur de "
                      f"votre paire gagne {cu(player.group.selected_player_decision_other * C.conversion_rate)}.")

    else:
        player.payoff = cu(player.group.selected_player_decision_other * C.conversion_rate)
        txt_final += (f"C'est la répartition de l'autre joueur qui s'est appliquée dans la paire. Il a choisi "
                      f"un montant de {player.group.selected_player_decision_self} ECU pour lui-même et un montant de "
                      f"{player.group.selected_player_decision_other} ECU pour vous. Vous gagnez donc {player.payoff} "
                      f"et l'autre joueur de votre paire gagne "
                      f"{cu(player.group.selected_player_decision_self * C.conversion_rate)} .")

    player.participant.vars[app_name] = dict(txt_final=txt_final, payoff=player.payoff)


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict()

    @staticmethod
    def js_vars(player: Player):
        return dict(
            matrices=C.matrices,
            fill_auto=player.session.config.get("fill_auto", False)
        )


class WaitForPairing(WaitPage):
    group_by_arrival_time = True


class Decision(MyPage):
    form_model = "player"

    def get_form_fields(player):
        fields_self = [f"svo_choice_{i}_self" for i in range(1, len(C.matrices) + 1)]
        fields_other = [f"svo_choice_{i}_other" for i in range(1, len(C.matrices) + 1)]
        return fields_self + fields_other

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, len(C.matrices) + 1):
                current_mat = C.matrices[i - 1]
                selected_cell = random.choice(current_mat)
                setattr(player, f"svo_choice_{i}_self", selected_cell[0])
                setattr(player, f"svo_choice_{i}_other", selected_cell[1])
        compute_score(player)


class DecisionWaitForGroup(WaitPage):
    wait_for_all_groups = False

    @staticmethod
    def after_all_players_arrive(group: Group):
        compute_payoffs(group)


class Results(MyPage):
    pass


page_sequence = [WaitForPairing, Decision, DecisionWaitForGroup, Results]
