import matplotlib.pyplot as plt 
import numpy as np 
class Hero :
    def __init__(self, name, profession, health=100, level=1):
        self.name = name
        self.profession = profession
        self.health = health
        self.level = level
        def_status ='Alive'
        self.status =def_status
    def introduce(self):
        self.name = input("Enter your hero's name: ")
        self.profession = input("Choose your profession (Warrior, Mage, Rogue): ")
        self.health = int(input("Enter your hero's health (default 100): ") or 100)
        self.level = int(input("Enter your hero's level (default 1): ") or 1)
        self.status = input("Enter your hero's status (default Alive): ")
        print("Welcome, {name} the {profession}! Your adventure begins now.".format(name=self.name, profession=self.profession))
    def level_up(self):
        self.level += 1
        print("Congratulations! You've reached level {level}!".format(level=self.level))
    
    def take_damage(self, damage):
        self.health -= damage
        self.status = 'PAIN!!!' if self.health <= 50 else 'Injured'
        print("AHHHHH! {name} took {damage} damage and is now at {health} health. Status: {status}".format(name=self.name, damage=damage, health=self.health, status=self.status))
    def get_user_function(self):
        print("\n--- Choose a Spell ---")
        
        try:
            user_input = int(input("Enter a spell: "))
            if user_input == 1: 
             self.health+=20
             print("You cast a Healing Spell!")
            elif user_input == 2:
                print("You cast a Fireball Spell!")
            if user_input == 3:
                self.level += 15
                print("You cast an Experience Spell!")
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number or YOU SHALL NOT PASS!!!")
            return None
player = Hero("Aragorn", "Warrior")

player.introduce()
spell = player.get_user_function()
if spell == 1:
    player.health += 20
    print("You cast a Healing Spell! Your health is now {health}.".format(health=player.health))
elif spell == 2:
    print("You cast a Fireball Spell!")
elif spell == 3:
    player.level += 15
    print("You cast an Experience Spell! Your level is now {level}.".format(level=player.level))
loop = True
for i in range(3):
    if loop:
        try:
            user_input = int(input("Enter a spell: "))
            if user_input == 1: 
             player.health+=20
             print("You cast a Healing Spell! Your health is now {health}.".format(health=player.health))
            elif user_input == 2:
                print("You cast a Fireball Spell!")
            if user_input == 3:
                player.level += 15
                print("You cast an Experience Spell! Your level is now {level}.".format(level=player.level))
            loop = False
        except ValueError:
            print("Invalid input. Please enter a valid number or YOU SHALL NOT PASS!!!")
