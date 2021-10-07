from random import randrange

def pick_random(event):
    
    size = len(event)
    choice = randrange(0,size - 1)
    
    return event[choice]

def random_enemy_attack(enemy_name):
    lion = ['Swipe', 'Bite', 'Pounce']
    hydra = ['Bite', 'Slam', 'Poison']
    cerberus = ['Bite', 'Scratch', 'Firebreath']

    if enemy_name == 'Nemean Lion':
        random_attack = pick_random(lion)
        return random_attack

    elif enemy_name == 'Learnaean Hydra':
        random_attack = pick_random(hydra)
        return random_attack

    elif enemy_name == 'Cerberus':
        random_attack = pick_random(cerberus)
        return random_attack

def player_attack():

    print('\n1. light attack')
    print('2. heavy attack')
    print('3. special attack')
    print('4. defend')

    player_choice = 0

    while player_choice < 1 or player_choice > 4:
        player_choice = (int(input('Choose an attack! (Enter 1-4) ')))
       
        if player_choice < 1 or player_choice > 4:
            print('Please use number keys 1-4 to make your selection')

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
        

def attack(enemy_name):

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
    'attack power' : 5,
    'Swipe' : 5,
    'Bite' : 10,
    'Pounce' : 15
    }

    hydra = {
    'health' : 300,
    'attack power' : 7,
    'Bite' : 5,
    'Slam' : 10,
    'Poison' : 20
    }

    cerberus = {
    'health' : 350,
    'attack power' : 10,
    'Bite' : 15,
    'Scratch' : 10,
    'Firebreath' : 25
    }
    
    if enemy_name == 'Nemean Lion':
        enemy_stats = lion

    elif enemy_name == 'Learnaean Hydra':
        enemy_stats = hydra

    elif enemy_name == 'Cerberus':
        enemy_stats = cerberus

    enemy_health = enemy_stats['health']
    player_health = hercules['health']

    while enemy_health > 0 and hercules['health'] > 0:

        out_damage = hercules[player_attack()]
        enemy_health -= out_damage



        if enemy_health <= 0:
            print('\nVictory!')
            break

        print(f'\nyou attack, enemy health = {enemy_health}')
        input('Press enter to continue:')

        random_attack = random_enemy_attack(enemy_name)
        in_damage = enemy_stats[random_attack]
        
        if out_damage == 0: #if defend is used
            in_damage = 0
        
        player_health -= in_damage

        if player_health <= 0:
            print('\nYou died!')
            break

        print(f'\n{enemy_name} used {random_attack}, you have {player_health} health remaining')
        input('Press enter to continue:')

attack('Nemean Lion')