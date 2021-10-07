from random import randrange

def pick_random(event):
    
    size = len(event)
    choice = randrange(0,size - 1)
    
    return event[choice]

def random_enemy_attack(enemy_name):
    lion = ['light attack', 'heavy attack', 'special attack']
    hydra = ['light attack', 'heavy attack', 'special attack']
    cerberus = ['light attack', 'heavy attack', 'special attack']

    if enemy_name == 'lion':
        random_attack = pick_random(lion)
        return random_attack

    elif enemy_name == 'hydra':
        random_attack = pick_random(hydra)
        return random_attack

    elif enemy_name == 'cerberus':
        random_attack = pick_random(cerberus)
        return random_attack

def player_attack(): #! add loop to prevent other input

    print('1. light attack')
    print('2. heavy attack')
    print('3. special attack')
    print('4. defend')

    player_choice = (int(input('Choose an attack! (Enter 1-4) ')))

    if player_choice == 1:
        player_attack = 'light attack'
        return player_attack

    elif player_choice == 2:
        player_attack = 'heavy attack'
        return player_attack

    elif player_choice == 3:
        player_attack = 'special attack'
        return player_attack

    elif player_choice == 4:
        player_attack = 'defend'
        return player_attack

def attack(enemy_name): #TODO add input to provide readability, adjust stat values

    hercules = {
    'health' : 100,
    'attack power' : 5,
    'light attack' : 25,
    'heavy attack' : 50,
    'special attack' : 100,
    'defend' : 0
    }

    lion = {
    'health' : 250,
    'attack power' : 7,
    'light attack' : 35,
    'heavy attack' : 70,
    'special attack' : 90,
    'number of attacks' : 3
    }

    hydra = {
    'health' : 500,
    'attack power' : 2,
    'light attack' : 10,
    'heavy attack' : 20,
    'special attack' : 40,
    'number of attacks' : 3
    }

    cerberus = {
    'health' : 500,
    'attack power' : 10,
    'light attack' : 50,
    'heavy attack' : 100,
    'special attack' : 200,
    'number of attacks' : 3
    }
    
    if enemy_name == 'lion':
        enemy_stats = lion

    elif enemy_name == 'hydra':
        enemy_stats = hydra

    elif enemy_name == 'cerberus':
        enemy_stats = cerberus

    enemy_health = enemy_stats['health']
    player_health = hercules['health']

    while enemy_health > 0 and hercules['health'] > 0:

        out_damage = hercules[player_attack()]
        enemy_health -= out_damage

        if enemy_health <= 0:
            print('Victory!')
            break

        print(f'you attack, enemy health = {enemy_health}')

        in_damage = enemy_stats[random_enemy_attack(enemy_name)]
        player_health -= in_damage

        if player_health <= 0:
            print('You died!')
            break

        print(f'the enemy attacks, you have {player_health} health remaining')