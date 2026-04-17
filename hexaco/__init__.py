import random

from otree.api import *

doc = "The H Factor of Personality,  Kibeom Lee & Michael C. Ashton"

class C(BaseConstants):
    NAME_IN_URL = 'hexaco_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    QUESTIONS = [
        {"id": 1, "text": "Visiter une galerie d'art m'ennuierait."},
        {"id": 2, "text": "J'organise et je prévois à l'avance afin d'éviter de tout bousculer à la dernière minute."},
        {"id": 3,
         "text": "Je suis rarement rancunier(ère), même envers les personnes qui m'ont causé de graves préjudices."},
        {"id": 4, "text": "Je me sens raisonnablement satisfait de moi-même dans l'ensemble."},
        {"id": 5, "text": "J'ai peur de voyager en cas d'intempéries."},
        {"id": 6,
         "text": "Je n'aurais pas recours à la flatterie pour obtenir une augmentation de salaire ou une promotion, même si je crois que cela aurait d'excellentes chances de réussir."},
        {"id": 7, "text": "Apprendre l'histoire et les politiques d'autres pays m'intéresse."},
        {"id": 8, "text": "Je me donne au maximum afin d'atteindre un but."},
        {"id": 9, "text": "Les gens me disent parfois que je juge trop les autres."},
        {"id": 10, "text": "Je fais rarement part de mes opinions pendant des réunions de groupe."},
        {"id": 11, "text": "Parfois, je ne peux m'empêcher de m'inquiéter pour des incidents sans importance."},
        {"id": 12,
         "text": "Si j'avais la certitude de ne jamais me faire prendre, je volerais volontiers un million de dollars."},
        {"id": 13, "text": "J'aimerais bien créer une œuvre d'art comme un roman, une chanson ou une peinture."},
        {"id": 14, "text": "Lorsque je travaille, je me soucie peu des petits détails."},
        {"id": 15, "text": "Les gens disent parfois que je suis une personne têtue."},
        {"id": 16,
         "text": "Je préfère les emplois qui exigent une interaction sociale active à un emploi où il faut travailler seul."},
        {"id": 17,
         "text": "Lorsqu'une expérience douloureuse m'afflige, j'ai besoin de quelqu'un pour me sentir mieux."},
        {"id": 18, "text": "Avoir beaucoup d'argent n'est pas particulièrement important pour moi."},
        {"id": 19, "text": "Porter attention aux idées radicales est une perte de temps."},
        {"id": 20,
         "text": "Lorsque je prends des décisions, je me fie à mon intuition du moment plutôt que de prendre le temps d'évaluer rationnellement la question."},
        {"id": 21, "text": "Les gens trouvent que je suis une personne qui se fâche facilement."},
        {"id": 22, "text": "La plupart du temps, je suis jovial(e) et optimiste."},
        {"id": 23, "text": "Voir quelqu'un pleurer me donne envie de pleurer moi-même."},
        {"id": 24, "text": "Je crois mériter plus de respect qu'une personne moyenne."},
        {"id": 25, "text": "Si j'en avais la chance, j'aimerais bien assister à un concert de musique classique."},
        {"id": 26, "text": "Au travail, mon désordre me cause parfois des problèmes."},
        {"id": 27, "text": "Mon attitude envers ceux qui m'ont traité injustement est de « pardonner et oublier »."},
        {"id": 28, "text": "J'estime que je suis une personne peu populaire."},
        {"id": 29, "text": "Les dangers physiques me font très peur."},
        {"id": 30,
         "text": "Pour obtenir quelque chose de quelqu'un en particulier, je rirais de ses blagues même si elles sont plates."},
        {"id": 31, "text": "Je n'ai jamais vraiment aimé feuilleter une encyclopédie."},
        {"id": 32, "text": "Je ne fais que le strict minimum de mon travail."},
        {"id": 33, "text": "Je juge souvent les autres avec indulgence."},
        {"id": 34, "text": "Dans des situations sociales, je suis la personné qui fait généralement les premiers pas."},
        {"id": 35, "text": "J'ai tendance à beaucoup moins m'inquiéter que la plupart des gens."},
        {"id": 36, "text": "Je n'accepterais jamais de pot-de-vin, aussi gros soit-il."},
        {"id": 37, "text": "On me dit souvent que j'ai beaucoup d'imagination."},
        {"id": 38, "text": "Je fais toujours mon travail avec minutie, même lorsque cela exige plus de temps."},
        {"id": 39, "text": "Je suis plutôt flexible dans mes opinions lorsque les gens ne sont pas d'accord avec moi."},
        {"id": 40, "text": "Me faire des amis est ma priorité quand je suis dans un nouvel environnement."},
        {"id": 41, "text": "Je peux gérer les situations difficiles sans le soutien moral de qui que ce soit."},
        {"id": 42, "text": "Posséder des articles de luxe me ferait très plaisir."},
        {"id": 43, "text": "J'aime bien les gens qui sont capables d'une vision non conventionnelle des choses."},
        {"id": 44, "text": "Je fais beaucoup d'erreurs, parce que je ne pense pas avant d'agir."},
        {"id": 45, "text": "La plupart des gens se fâchent plus rapidement que moi."},
        {"id": 46, "text": "La plupart des gens sont plus optimistes et dynamiques que moi."},
        {"id": 47,
         "text": "Je me sens très émotif(ve) quand une personne qui m'est proche s'en va pour une longue période"},
        {"id": 48, "text": "Je veux que les gens sachent que je suis une personne importante et supérieure."},
        {"id": 49, "text": "Je ne me considère pas comme une personne artistique ou créative."},
        {"id": 50, "text": "On me qualifie souvent de perfectionniste."},
        {"id": 51,
         "text": "Même lorsque les gens commettent de nombreuses erreurs, j'émets rarement des commentaires négatifs."},
        {"id": 52, "text": "J'estime parfois que je suis une personne sans valeur."},
        {"id": 53, "text": "Même en cas d'urgence, je ne panique pas."},
        {"id": 54,
         "text": "Je ne ferais pas semblant d'aimer une personne dans le seul but d'obtenir une faveur d'elle."},
        {"id": 55, "text": "Parler de philosophie m'ennuie."},
        {"id": 56, "text": "Je préfère être spontané(e) que de m'en tenir à un plan."},
        {"id": 57, "text": "Lorsqu'on me dit que j'ai tort, ma réaction première est de défendre mon point de vue."},
        {"id": 58, "text": "Lorsque je suis en groupe, je suis souvent le ou la porte-parole."},
        {"id": 59,
         "text": "Je reste impassible même dans des situations où la plupart des gens deviennent très émotifs."},
        {"id": 60,
         "text": "Je serais tenté(e) d'utiliser de la fausse monnaie si j'étais certain(e) de ne jamais me faire prendre"}
    ]
    NUM_QUESTIONS = len(QUESTIONS)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

for q in C.QUESTIONS:
    setattr(Player, f"hexaco_{q['id']}", models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q["text"]
    ))


class Hexaco(Page):
    form_model = 'player'

    def get_form_fields(player):
        return [f'hexaco_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            for q in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f"hexaco_{q}", random.randint(1, 5))


page_sequence = [Hexaco]
