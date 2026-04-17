import random

from otree.api import *

doc = "SD3 (Short Dark Triad) - Paulhus, 2013"


class C(BaseConstants):
    NAME_IN_URL = 'shortDarkTriad'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # SD3 - 27 items (9 Mach, 9 Narc, 9 Psych)
    QUESTIONS_SD3 = [
        # MACHIAVÉLISME
        {"id": 1, "text": "Il n'est pas sage de divulguer ses secrets.", "rev": False},
        {"id": 2, "text": "J'aime utiliser des manipulations intelligentes pour arriver à mes fins.", "rev": False},
        {"id": 3, "text": "Il faut s'assurer que vos plans bénéficient à vous-même, pas aux autres.", "rev": False},
        {"id": 4, "text": "L'essentiel est de choisir le bon moment pour exploiter les autres.", "rev": False},
        {"id": 5, "text": "Il y a des gens qu'il faut inévitablement écraser pour réussir.", "rev": False},
        {"id": 6, "text": "Évitez les conflits directs, mais manipulez en coulisses.", "rev": False},
        {"id": 7, "text": "Gardez une trace des informations que vous pourrez utiliser plus tard contre les gens.",
         "rev": False},
        {"id": 8, "text": "On devrait faire ce qui est nécessaire pour obtenir ce que l'on veut.", "rev": False},
        {"id": 9, "text": "Beaucoup de gens sont des imbéciles et il est facile de les mener par le bout du nez.",
         "rev": False},
        # NARCISSISME
        {"id": 10, "text": "Les gens voient naturellement en moi un leader.", "rev": False},
        {"id": 11, "text": "Je déteste être une personne ordinaire.", "rev": False},
        {"id": 12, "text": "Je sais que je suis spécial parce que tout le monde me le dit.", "rev": False},
        {"id": 13, "text": "J'aime attirer l'attention sur moi.", "rev": False},
        {"id": 14, "text": "Je suis une personne exceptionnelle.", "rev": False},
        {"id": 15, "text": "J'aime fréquenter des personnes importantes.", "rev": False},
        {"id": 16, "text": "J'ai été comparé à des personnes célèbres.", "rev": False},
        {"id": 17, "text": "Je suis digne de tout le respect qui m'est dû.", "rev": False},
        {"id": 18, "text": "J'aime qu'on me flatte.", "rev": False},
        # PSYCHOPATHIE
        {"id": 19, "text": "J'aime me venger des gens qui me cherchent des noises.", "rev": False},
        {"id": 20, "text": "J'aime les activités risquées ou dangereuses.", "rev": False},
        {"id": 21, "text": "Les gens qui m'embêtent le regrettent toujours.", "rev": False},
        {"id": 22, "text": "Je ne me sens jamais coupable d'avoir fait quelque chose de mal.", "rev": False},
        {"id": 23, "text": "La vengeance doit être rapide et efficace.", "rev": False},
        {"id": 24, "text": "Les gens disent que je suis hors de contrôle.", "rev": False},
        {"id": 25, "text": "Il est vrai que je peux être cruel par moments.", "rev": False},
        {"id": 26, "text": "Je n'ai pas peur des conséquences de mes actes.", "rev": False},
        {"id": 27, "text": "Je n'ai jamais eu d'ennuis avec la loi.", "rev": True},  # Item inversé
    ]
    NUM_QUESTIONS = len(QUESTIONS_SD3)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score_mach = models.FloatField()
    score_narc = models.FloatField()
    score_psych = models.FloatField()

    def set_sd3_scores(self):
        def get_val(idx):
            q = C.QUESTIONS_SD3[idx - 1]
            val = getattr(self, f'sd3_{idx}')
            return (6 - val) if q['rev'] else val

        self.score_mach = sum(get_val(i) for i in range(1, 10)) / 9
        self.score_narc = sum(get_val(i) for i in range(10, 19)) / 9
        self.score_psych = sum(get_val(i) for i in range(19, 28)) / 9


for q in C.QUESTIONS_SD3:
    setattr(Player, f'sd3_{q["id"]}', models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q['text'],
    ))


class DarkTriadPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [f'sd3_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f'sd3_{i}', random.randint(1, 5))
        player.set_sd3_scores()


page_sequence = [DarkTriadPage]
