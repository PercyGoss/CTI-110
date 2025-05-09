# Percy Goss
# 26/04/2025 (26th of April, 2025)
# P5Lab
# The Game... 
# It might a bit too big for the assignment, but I'm having fun creating it so I don't care.

import random

def combat(enemy, e_str, e_dex, e_hp, health, base_health, dexterity, strength, ability):
    dr = 0
    ability_counter = 1
    hex_timer = 0
    focus_timer = 0
    guard = 0
    
    print('Combat Start')
    
    if e_dex > dexterity:
        turn = 0
        print('The', enemy, 'is too quick!')
    else:
        turn = 1
    
    while e_hp > 0 and health > 0:
        if ability_counter == 1:
            while turn == 1:
                print(f'{enemy} Health:', e_hp)
                print(f'Your health: {health}/{base_health}')
                action = input('Attack      Guard       Ability\n')
                print()
                
                if action.lower() == 'attack':
                    damage = damage_check(strength)
                    e_hp -= damage
                    print (f'You attack for {damage} damage.')
                    turn = 0
                elif action.lower() == 'guard':
                   guard = 1
                   dr += 3
                   print('You raise your guard...')
                   turn = 0
                elif action.lower() == 'ability':
                    if ability == 'Flurry':
                        print()
                        print('Blind fury!')
                        atk1 = damage_check(strength) - 5
                        print (f'You slash for {atk1} damage.')
                        atk2 = damage_check(strength) - 7
                        print (f'You cut for {atk2} damage.')
                        atk3 = damage_check(strength) - 8
                        print (f'You swing for {atk3} damage.')
                        e_hp -= atk1 + atk2 + atk3
                        ability_counter = 0
                    elif ability == 'Focus':
                        print()
                        print('Breathe in, and out...')
                        print('Dodge chance increased for 3 turns!')
                        focus_timer = 3
                        ability_counter = 0
                    elif ability == 'Prayer':
                        print()
                        print('You need not speak, only trust...')
                        print('30 health restored!')
                        health += 30
                        if health > base_health:
                            health = base_health
                        ability_counter = 0
                    elif ability == 'Hex':
                        print()
                        print('A silent incantation...')
                        print(f'{enemy}\'s attack reduced for 3 turns!')
                        hex_timer += 3
                        dr += 7
                        ability_counter = 0
                    
                    turn = 0
                else:
                    print('That is not an available action.')
                    print()
        else:
            while turn == 1:
                print(f'{enemy} Health:', e_hp)
                print(f'Your health: {health}/{base_health}')
                action = input('Attack      Guard\n')
                
                if action.lower() == 'attack':
                    damage = damage_check(strength)
                    e_hp -= damage
                    print (f'You attack for {damage} damage.')
                    turn = 0
                elif action.lower() == 'guard':
                    guard_timer += 1
                    dr += 3
                    print('You raise your guard...')
                    turn = 0
                elif action.lower() == 'ability':
                    print('You\'ve already used your ability.')
                    print()
                else:
                    print('That is not an available action.')
                    print()
                    
        if turn == 0 and e_hp > 0:
            print()
            e_damage = damage_check(e_str)
            
            if guard == 1 and hex_timer == 1:
                e_damage -= 10
            elif guard == 0 and hex_timer == 1:
                e_damage -= 7
            elif guard == 1 and hex_timer == 0:
                e_damage -= 3
            
            if focus_timer > 0:
                dodge = dodge_check(dexterity+5)
                focus_timer -= 1
            else: dodge = dodge_check(dexterity)
            
            if e_damage < 0:
                print(f'The {enemy}\'s attack bounces right off you, harmless.')
            elif dodge == 'damage taken':
                print(f'The {enemy} attacks, dealing {e_damage} damage.')
                health -= e_damage
            else:
                print(f'The {enemy} attacks, but misses!')
            
            print()
            turn = 1
    
    if e_hp <= 0:
        print('Victory!')
        health += 15
        if health > base_health:
            health = base_health
        print('You take a brief moment to recoup. 15 health recovered.')
        condition = condition_check(health, base_health)
        print('You are in', condition, 'condition.')
    if health <= 0:
        print('Defeat...')
        print('You are dragged, unconcious, back to your cell. Security is tightened. It appears it will be a very long time before you can attempt another escape.')
            
def naming(c_class):
    name = input(f'How shall you name your new host?\n')
    print()
    print(f'{name}, the {c_class}... How very interesting.')

def stat_check(stat):
    chance = random.random()
    
    if stat == 20:
        if chance >= .25:
            outcome = 'Success!'
        else:
            outcome = 'Failure...'
    elif stat == 15:
        if chance >= .5:
            outcome = 'Success!'
        else:
            outcome = 'Failure...'
    else:
        if chance >= .75:
            outcome = 'Success!'
        else:
            outcome = 'Failure...'
    
    return outcome

def condition_check(health, base_health):
    if health == base_health:
        condition = 'perfectly unharmed.'
    elif health/base_health >= .75:
        condition = 'scratched, but you\'ll be fine.'
    elif health/base_health >= .5:
        condition = 'hurt.'
    elif health/base_health >= .25:
        condition = 'gravely wounded.'
    elif health/base_health > 0:
        condition = 'desperate.'
    else:
        condition = 'defeated.'
    
    return condition

def dodge_check(dexterity):
    chance = random.random()
    
    if dexterity == 25:
        if chance >= 70:
            outcome = 'attack dodged'
        else:
            outcome = 'damage taken'
    elif dexterity == 20:
        if chance >= .80:
            outcome = 'attack dodged'
        else:
            outcome = 'damage taken'
    elif dexterity == 15:
        if chance >= .85:
            outcome = 'attack dodged'
        else:
            outcome = 'damage taken'
    else:
        if chance >= .90:
            outcome = 'attack dodged'
        else:
            outcome = 'damage taken'
    
    return outcome

def damage_check(strength):
    damage = random.randint(strength-5, strength+5)
    return damage

    
def main():        
    class_picker = 'n'
    print('Within the asylum, 4 poor fools lie in wait for an end that will never come.')
    print('     The Warrior, great of might and will, exiled for treason. Once, they were a hero, but those days are long gone.')
    print('     The Wanderer, quick of foot and wit, chained down for treason. Always in the right place, at the wrong time.')
    print('     The Devout, strong of faith and justice, punished for treason. Even shackled, they cling to their deity.')
    print('     The Forlorn, weak-bodied with a powerful mind. Their history is shrouded by time, but their craft is unmatched.')
    
    while class_picker.lower() != 'y':
        print()
        c_class = input("Which accursed soul shall be your vessel? (Warrior/Wanderer/Devout/Forlorn) - ")
        if c_class.lower() == "warrior":
            print('The Warrior, generic but well-rounded. Average dexterity, average strength, average health.')
            print('Once per combat encounter, the Warrior may cast Flurry, striking rapidly for reduced damage.')
            dexterity = 15
            strength = 15
            base_health = 150
            health = 150
            ability = 'Flurry'
            print()
            naming(c_class)
            class_picker = 'y'
        elif c_class.lower() == "wanderer":
            print('The Wanderer, light and agile but an unpracticed fighter. High dexterity, low strength, average health.')
            print('Once per combat enocunter, the Wanderer may cast Focus, attuning to their senses and increasing dodge')
            dexterity = 20
            strength = 10
            base_health = 150
            health = 150
            ability = 'Focus'
            print()
            naming(c_class)
            class_picker = 'y'
        elif c_class.lower() == "devout":
            print('The Devout, hard to kill but rather slow. Low dexterity, average strength, high health.')
            print('Once per combat encounter, the Devout may cast Prayer, calling to their deity in their time of need and healing them.')
            dexterity = 10
            strength = 15
            base_health = 200
            health = 200
            ability = 'Prayer'
            print()
            naming(c_class)
            class_picker = 'y'
        elif c_class.lower() == "forlorn":
            print('The Forlorn, frail and powerful at once. Average dexterity, high strength, low health.')
            print('Once per combat encounter, the Forlorn may cast Hex, placing a strength-sapping curse on the enemy.')
            dexterity = 15
            strength = 20
            base_health = 100
            health = 100
            ability = 'Hex'
            print()
            naming(c_class)
            class_picker = 'y'
        else:
            print('Are you not content with what I have offered you? A pity you have no choice.')
    
    condition = condition_check(health, base_health)
    if condition != 'defeated.':
    #Introduction
        print()
        if c_class.lower() == 'warrior':
            print('Sick. This place makes you sick. The foul smell, the dreary atmosphere, the wailing from some of the other 5 cells. All of it. ')
            print('It makes you angry. You shouldn\'t be here. You were a legend! How far you have fallen. But you\'re no fool, oh no.')
            print('You have eternity, after all, and you can be so very patient. So, as rainwater rusts your cell door, you wait. And eventually...')
            print('You kick it down. Freedom, at last...')
        elif c_class.lower() == "wanderer":
            print("Why? Why are you here? What did you do? Treason? It makes no sense, you think, you hardly ever visited this kingdom.")
            print("You yearn for the open skies, long to simply return to the road. Anything but rot in this place for eternity.")
            print("Eternity... eventually, an opportunity presents itself. Hanging vines, just sturdy enough to support you, grow above.")
            print("You're not one to pass up such an opportunity, are you? And so, you climb your way out.")
        elif c_class.lower() == 'devout':
            print('It has been years since you were imprisoned. So many years, in some dark and dismal dungeon. Yet you never lost faith. ')
            print('No. You prayed. You prayed day in, and day out, for salvation. For absolution. You know it\' hopeless, but yet you pray still.')
            print('Your prayers never fell on deaf ears. You deity heard every. Single. One. And when the time was right, they ansered.')
            print('Walking out, you look at the other locked cells. Poor fools, you think, trapped without devotion. And you leave.')
        elif c_class.lower() == 'forlorn':
            print('It wasn\'t long after they found you that you were thrown here. It\'s been so long, it\'s difficult to even recall why.')
            print('They sapped you of all your strength, at first. They thought it would hold you forever. That you were powerless without your spells.')
            print("Perhaps you are. But your spells belong to you, and you alone. They are part of your soul, and no god nor man can take that from you.")
            print("Your cell door crumbles to ash so easily. Hmph. Nothing lasts forever.")
        print()
#The game begins
        if c_class.lower == 'wanderer':
            print('Climbing atop. you find yourself surrounded by a sheer on most sides. There is only one safe path, an opening above the hall past your cell. \nSo, taking in the fresh air one last time, you drop back down into the Asylum.')
        print('A long corridor, lined with empty cells and dying torches, stretches ahead of you. At the end is a locked door, and a dozing guard. You have 3 choices.') 
        print('Try to pick the keys off of and sneak past him. (Dexteirty check)')
        print('Just get his attention. (Initiate Combat)')
        print()
        decision1 = input('What approach do you take? Surprise, stealth, or fight?\n')
        if decision1.lower() == 'surprise':
            result1 = stat_check(strength)
            if result1 == 'Success!':
                print('You approach steadily at first, before charging in to jump the guard. Caught off guard, he\'s hardly a challenge.')
                print('Taking the key from his unconcious body, you unlock the door. By the time he wakes up, you should already be long gone.')
            else:
                print('You charge in yelling, but that only gives the guard enough time to wake and register the situation.')
                health -= 10
                print('As you charge in, he waits until you get closer. Then, he plants a firm kick on your chest. So that\'s how it\'s going to be?')
                combat('guard', 5, 15, 50, health, base_health, dexterity, strength, ability)
                print('Taking the keys from the defeated guard, you unlock the door and move on.')
        elif decision1.lower() == 'stealth':
            result1 = stat_check(dexterity)
            if result1 == 'Success!':
                print('Cautious and silent, you sneak up to the sleeping guard. Slowly, you take the keys from his belt and unlock the door past him.')
                print('The loud creak of the door stirs the guard from his slumber, but you have just enough time to slip through and lock the door back up behind you.')
            else:
                print('You make it oh, so close. So very close. But as you grab the keys, you fumble and drop them. You have just enough time to register what happened')
                health -= 5
                print('You immediately step back, the guard\'s sword just barely grazing your arm as you retreat. Looks like you\'ll have to use a different approach.')
                combat('guard', 5, 15, 50, health, base_health, dexterity, strength, ability)
                print('Taking the keys from the defeated guard, you unlock the door and move on.')
        else:
            print('No need for theatrics, right? You\'re plently capable. Let\'s make this a fair.')
            combat('guard', 5, 15, 50, health, base_health, dexterity, strength, ability)
            print('Taking the keys from the defeated guard, you unlock the door and move on.')
        print('The room beyond opens up into a small courtyard, covered in a bleak layer of dying grass and fallen leaves. Is that what season it is?')
        print('Time is a funny thing, in the Asylum. You recall lush vines near the cells, yet here it all seems dead. Just how long has it really been since you were locked up here?')
        print('It\'s best not to dwell on such things, you think. Right now, your only goal is escape. And so, you press on.')
        
    else:
        print('You awake once more in an all too familiar cell, yet now watchful guards are posted to ensure you do not escape again.')
        print('Oh well. Such a shame really, a golden opportunity wasted. But nothing truly lasts forever, does it? Perhaps, some other time, another opportunity will make itself know.')
        print('Until then, however, you have naught to do but wait.')
        print('GAME OVER')
    input('There is nothing else for now. Say what you wish, or say nothing, and leave.')
main()