import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'mach_iv'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # questions MACH-IV
    QUESTIONS_MACH = [
        {"id": 1,
         "text": "Il ne faut jamais dire à quelqu'un la véritable raison pour laquelle on a fait quelque chose, à moins qu'il n'y ait un intérêt à le faire.",
         "reverse": False},
        {"id": 2, "text": "La meilleure façon de gérer les gens est de leur dire ce qu'ils veulent entendre.",
         "reverse": False},
        {"id": 3, "text": "On ne devrait agir que lorsque l'on est certain que c'est moralement juste.",
         "reverse": True},
        {"id": 4, "text": "La plupart des gens sont fondamentalement bons et gentils.", "reverse": True},
        {"id": 5,
         "text": "Il est plus sûr de présumer que tous les gens ont un fond de méchanceté qui ressortira s'ils en ont l'occasion.",
         "reverse": False},
        {"id": 6, "text": "L'honnêteté est la meilleure politique en toutes circonstances.", "reverse": True},
        {"id": 7, "text": "Il n'y a aucune excuse pour mentir à quelqu'un d'autre.", "reverse": True},
        {"id": 8, "text": "D'une manière générale, les gens ne travaillent dur que s'ils y sont forcés.",
         "reverse": False},
        {"id": 9,
         "text": "Tout bien considéré, il vaut mieux être humble et honnête que d'être important et malhonnête.",
         "reverse": True},
        {"id": 10,
         "text": "Quand on demande à quelqu'un de faire quelque chose, il vaut mieux donner les vraies raisons plutôt que des raisons qui ont plus de poids.",
         "reverse": True},
        {"id": 11, "text": "La plupart des gens qui réussissent dans le monde mènent une vie propre et morale.",
         "reverse": True},
        {"id": 12, "text": "Quiconque fait entièrement confiance à quelqu'un d'autre s'expose aux problèmes.",
         "reverse": False},
        {"id": 13,
         "text": "La plus grande différence entre la plupart des criminels et les autres gens est que les criminels sont assez stupides pour se faire prendre.",
         "reverse": False},
        {"id": 14, "text": "La plupart des gens sont courageux.", "reverse": True},
        {"id": 15, "text": "Il est sage de flatter les personnes importantes.", "reverse": False},
        {"id": 16, "text": "Il est possible d'être bon sous tous les rapports.", "reverse": True},
        {"id": 17, "text": "P.T. Barnum avait tort de dire qu'il naît un naïf chaque minute.", "reverse": True},
        {"id": 18, "text": "Il est difficile de réussir sans couper les coins ronds ici et là.", "reverse": False},
        {"id": 19,
         "text": "Les gens oublient plus facilement la mort de leurs parents que la perte de leur patrimoine.",
         "reverse": False},
        {"id": 20, "text": "La plupart des gens ne renoncent pas facilement à leur pouvoir.", "reverse": False},
    ]
    NUM_QUESTIONS = len(QUESTIONS_MACH)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mach_score = models.FloatField()

    def set_mach_score(self):
        total = 0
        for q in C.QUESTIONS_MACH:
            val = getattr(self, f'mach_{q["id"]}')
            if q['reverse']:
                total += (6 - val)
            else:
                total += val
        self.mach_score = total / C.NUM_QUESTIONS


# Fields generation
for q in C.QUESTIONS_MACH:
    setattr(Player, f'mach_{q["id"]}', models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q["text"]
    ))


class MachPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [f'mach_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f'mach_{i}', random.randint(1, 6))
        player.set_mach_score()


page_sequence = [MachPage]
