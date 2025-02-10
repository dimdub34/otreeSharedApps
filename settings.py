from os import environ

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = '1267413152020'

PARTICIPANT_FIELDS = ["payoff_ecu"]
SESSION_FIELDS = ["fill_auto", "language", "understanding", "lexicon", "test"]
LANGUAGE_CODE = 'fr'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    fill_auto=False,
    test=False,
    doc=""
)

SESSION_CONFIGS = [
    dict(
        name="counting_task",
        display_name="Counting Task",
        app_sequence=["counting_task"],
        num_demo_participants=5
    ),
    dict(
        name="slider_task",
        display_name="Slider Task",
        app_sequence=["slider_task"],
        num_demo_participants=5,
    ),
    dict(
        name='bret',
        display_name="Bomb Risk Elicitation Task (BRET)",
        app_sequence=['bret'],
        num_demo_participants=2,
    ),
    dict(
        name='nle',
        display_name="Number Line Estimation (NLE)",
        app_sequence=['nle'],
        num_demo_participants=2,
    ),
    dict(
        name='eckelGrossman',
        display_name="Eckel & Grossman",
        app_sequence=['eckelGrossman'],
        num_demo_participants=2,
    ),
    dict(
        name='svo',
        display_name="Social Value Orientation (SVO)",
        app_sequence=['svo'],
        num_demo_participants=2,
    ),
    dict(
        name='bart',
        display_name="Balloon Analogue Risk Task (BART)",
        app_sequence=['bart'],
        num_demo_participants=2,
    ),

]
