# CS 61A World Game Data:
from classes import *

# Characters:

gerald = Character('Gerald',
                 "I can't believe I lost my wallet again! "
                 "I wish someone could find it for me."
                 "I could also really use a hot dog.")
juliette = Character('Juliette',
                  'Gerald went to Soda to start grading. You can find him there.')
jobel = Character('Jobel',
                   'What do you mean ok doesnt work? ')
meghna = Character('Meghna',
                    'No one brought food to the potluck! '
                    'Maybe the Golden Bear Cafe (GBC) is open; we can get food there.')
andrew = Character('Jessica',
                    'I heard you like games, so I put some games in this game. '
                    'Have you gone to Games of Berkeley on Shattuck?')
jessica = Character('Andrew',
                  'Hey! Want to play ultimate frisbee?')
student = Character('Student',
                    'I once went into Dwinelle and got lost for 3 days! '
                    'That place is a maze!')
scared_student = Character('Terrified Student',
                           "I've been lost in Dwinelle for weeks")

# Things:
wallet = Thing('Wallet',
               "Looks like Gerald's wallet. We should return it to him.")
hotdog = Thing('Hotdog',
               'Yummy! Bring it to a TA')
coffee = Thing('Coffee',
               'The sweet, caffienated nectar of the gods')
cards = Thing('Monopoly',
              'Just right for 61A study breaks!')
strange_skull = Thing('Strange Skull',
                      'A strange skull. Dinosaur? Giraffe? Who knows.')

# Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')

# Places:

sather_gate = Place('Sather Gate', 'Sather Gate - A fairly ineffective gate',
                    [], [])
fsm = Place('FSM', 'Free Speech Cafe - Home of Coffee',
            [], [wallet, coffee])
vlsb = Place('VLSB', 'VLSB - THE building of Life Sciences',
             [juliette], [])
soda = Place('Soda', 'Soda Hall - A building where Soda is not allowed',
             [gerald, meghna], [])
gbc = Place('GBC', 'Golden Bear Cafe - Now with healthy food',
            [], [hotdog])
campanile = Place('Campanile', 'The Campanile - A great tower!',
                  [jobel], [])
game_store = Place('Games of Berkeley', 'Games of Berkeley',
                   [], [cards])
woz = Place('Woz', 'Wozniak Lounge',
            [], [])
shattuck = Place('Shattuck', 'Shattuck Avenue',
                 [], [])
wheeler = Place('Wheeler Hall', 'Wheeler Hall - CS61A lectures are held here.',
                [jessica], [skeleton_key])
dwinelle = Place('Dwinelle Hall', 'Dwinelle Hall - A Maze',
                 [student], [])
deep_dwinelle = Place('Deep in Dwinelle Hall', 'You are lost in Dwinelle Hall',
                      [scared_student], [strange_skull])
memorial_glade = Place('Memorial Glade', 'Memorial Glade on a beautiful day',
                       [andrew], [])


# Exits:
sather_gate.add_exits([gbc, wheeler, dwinelle, memorial_glade])
gbc.add_exits([sather_gate])
wheeler.add_exits([sather_gate, campanile])
deep_dwinelle.add_exits([deep_dwinelle, dwinelle])
dwinelle.add_exits([sather_gate, vlsb, wheeler, deep_dwinelle])
memorial_glade.add_exits([sather_gate, fsm, campanile, soda])
campanile.add_exits([memorial_glade, wheeler])
vlsb.add_exits([fsm, soda, shattuck, dwinelle])
shattuck.add_exits([vlsb, game_store])
fsm.add_exits([vlsb, memorial_glade])
soda.add_exits([woz, vlsb, memorial_glade])
woz.add_exits([soda])
game_store.add_exits([shattuck])

# Locked Buildings
fsm.locked = True

# Player:
# The Player should start at sather_gate.
me = None

