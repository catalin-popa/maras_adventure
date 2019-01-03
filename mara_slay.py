# Mara's Slay the Spire
from random import randint

enemy_types = ['wild boar', 'goblin', 'wizard', 'troll', 'thief']

def battle(floor):
    global HP
    global energy

    for i in range(len(ascii_floor_number)):
        if i == 4:
            print(ascii_floor_number[i][0:37] + str(floor) + ascii_floor_number[i][38:])
        else:
            print(ascii_floor_number[i])

    #spawn enemy

    if floor == 1:
        enemy = enemy_types[0]
    #elif floor % 5 == 0:
        # we generate a boss enemy here
    else:
        enemy = enemy_types[randint(1, 4)]

    current_poison = 0

    print('')

    if enemy == 'wild boar':
        enemy_HP = 30
        enemy_atk_min, enemy_atk_max = 5, 10
    # elif enemy == 'goblin:
    # ...

    print(ascii_floor)
    print('A', enemy.upper(), 'attacks you!!! It has', enemy_HP, 'HP')
    print('')
    for ascii_line in hog_ascii:
        print(ascii_line)
    print('')

    while enemy_HP > 0:
        enemy_goes_first = randint(1, 100) <= 30 and enemy != 'wild boar'

        enemy_atk_value = randint(enemy_atk_min, enemy_atk_max)

        if character == 'Theseus':
            enemy_atk_value -= passive_block
            if enemy_atk_value < 0:
                enemy_atk_value = 0

        if enemy_goes_first:
            print(enemy.upper(), 'attacks for', enemy_atk_value)
            HP -= enemy_atk_value
            if HP <= 0:
                break

        hero_atk_value = randint(attack_range[0], attack_range[1])
        current_poison += passive_poison

        print('You attack for', hero_atk_value, '...')
        enemy_HP -= hero_atk_value

        if current_poison > 0:
            print(enemy.upper(), 'takes', current_poison, 'poison damage')
            enemy_HP -= current_poison

        if enemy_HP <= 0:
            break

        if not enemy_goes_first:
            print(enemy.upper(), 'attacks for', enemy_atk_value)
            HP -= enemy_atk_value
            if HP <= 0:
                break

    if HP > 0:
        print('End of battle stats: ', HP, energy)
        input('Continue...')
    else:
        print('YOU DIED :\'(')
        input('The End...')

ascii_floor_number = [
'        ______ _',
'        |  ___| |',
'        | |_  | | ___   ___  _ __        ',
'        |  _| | |/ _ \ / _ \| \__|  ---  ',
'        | |   | | (_) | (_) | |    | ? | ',
'        \_|   |_|\___/ \___/|_|     ---  '
]

llama_ascii = [
"                        _    _",
"                       ( \__//)",
"                       .'     )",
"      -----------   __/b d  .  )",
"      | WELCOME |  (_Y_`,     .)",
"      -----------   `--'-,-'  )",
"                         (.  )",
"                         (   )",
"                        (   )",
"                       ( . )         .---.",
"                      (    )        (     )",
"                      (   . )      (  .    )",
"                      (      )    (      .  ),",
"                      ( .     `\"'`  .       `)\\",
"                       (      .              .)\\",
"                       ((  .      .   (   .   )\\\\",
"                       ((       .    (        ) \\\\",
"                        ((     )     _( .   . )  \\\\",
"                        ( ( .   )\"'\"`(.(     )   ( ;",
"                        ( (    )      ( ( . )     \\'",
"                         |~(  )        |~(  )",
"                         | ||~|        | ||~|",
"                    jgs  | || |        | || |",
"                        _| || |       _| || |",
"                       /___(| |      /___(| |",
"                          /___(         /___("
]

hog_ascii = [
'              _,-""""-..__',
'         |`,-\'_. `  ` ``  `--\'\"\"\".',
'         ;  ,\'  | ``  ` `  ` ```  `.',
'       ,-\'   ..-\' ` ` `` `  `` `  ` |==.',
'     ,\'    ^    `  `    `` `  ` `.  ;   \\',
'    `}_,-^-   _ .  ` \ `  ` __ `   ;    #',
'       `"---"\' `-`. ` \---""`.`.  `;',
'                  \\\\` ;       ; `. `,',
'                   ||`;      / / | |',
'      jrei         //_;`    ,_;\' ,_;"'
]
ascii_floor = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

print ('Mara says: welcome to this adventure. It may be your dooooom.')

# + max HP, + per class bonus: warrior +1 passive block, ninja +1 poison, +max_energy
start_bonuses = ['HP boost', 'class boost', 'max energy boost', 'evasion spell']

floor = 0
act = 1

# base HP
HP = 50
energy = 100
# base attack range
attack_range = (8, 20)

passive_block = 0
passive_poison = 0

active_block_chance = (0, 0)
active_heal = 0

base_trait = ''
active_skill = ''

character = ('Theseus' if input('[W]arrior or [N]inja: ')[0] in 'wW' else 'Lightning')

for ascii_line in llama_ascii:
    print(ascii_line)

print('Dear ' + character + ', good luck in your journey!')

input('Continue...')

if character == 'Theseus':
    HP += 25
    passive_block += 5
    base_trait = 'block passively for ' + str(passive_block)
    active_heal = 10
    active_skill = 'heal for ' + str(active_heal) + ' HP'
if character == 'Lightning':
    attack_range = (5, 15)
    passive_poison += 3
    base_trait = 'add ' + str(passive_poison) + ' poison with each shot'
    active_block_chance = (30, 100)
    active_skill = 'block for ' + str(active_block_chance[0]) + '-' + str(active_block_chance[1]) + '% of incoming damage'

print('Your basic trait is: ' + base_trait)
print('Your active skill is: ' + active_skill)

bonus = start_bonuses[randint(0, len(start_bonuses) - 1)]
print('Your start bonus is:', bonus)
input('Continue...')
# todo: add the specified bonus to your character
if bonus == 'HP boost':
    HP += 10
elif bonus == 'max energy boost':
    energy += 10
elif bonus == 'class boost':
    if character == 'Theseus':
        passive_block += 2
    if character == 'Lightning':
        passive_poison += 1

for i in range(1, 2):
    floor += 1
    print(ascii_floor)
    battle(floor)
    # 4 normal battles
    # with a chance to be elite fight or some kind of prize
    # 5 boss

