#Single Player RPG

#Import Files
import functions


#Create Playable Characters

class Player:
    def __init__(self, health, mana, speed):
        self._health = health
        self._mana = mana
        self._speed = speed
    
    def get_speed(self):
        return self._speed
    
    def get_stats(self):
        return self._health, self._mana, self._speed

    def take_damage(self, damage):
        self._health -= damage
    
    #First we want to set the player's attack + modifer
    #to call later on the enemies
    def get_player_modifier(self):
        return functions.d20() + self.get_speed()
        
#Check to see if Player is still alive
    def check_alive(self):
        return self._health > 0
    
#########################################################################

#=====================   Create subclass Ranger   ======================#

#########################################################################

class Ranger(Player):
    def __init__(self, sword_damage=10, fireball_damage=15):
        super().__init__(100, 15, 2.5)
        self._sword_damage = sword_damage
        self._fireball_damage = fireball_damage
  
#Ranger sword attack
    def sword_attack(self, target):
        modified_attack = self.get_player_modifier()
        if self.check_alive():
            if modified_attack >= target.get_speed():  # First check if the attack lands
                if modified_attack >= 20:  # If the attack lands, check if it's critical
                    target.take_damage(self._sword_damage * 2)  # If it's critical, do double damage
            else:  # If it's not critical...
                target.take_damage(self._sword_damage)  # Do normal damage
        else:
            print('Game Over')
        
#Ranger mana attack (fireball)
    def fireball(self, target):
        if self.check_alive():
            if self._mana >= 5:
                target.take_damage(self._fireball_damage)
                self._mana -= 5
            else:
                print('Not enough mana to cast')
        else:
            print('Game Over')
            
#########################################################################

#=====================   Create Enemies   ==============================#

#########################################################################

class Enemy:
    def __init__(self, health, attack1, attack2, speed):
        self._health = health
        self._attack1 = attack1
        self._attack2 = attack2
        self._speed = speed

    def get_speed(self):
        return self._speed
    
    def get_stats(self):
        return self._health, self._attack1, self._attack2, self._speed

    def take_damage(self, damage):
        self._health -= damage
        
    def get_player_modifier(self):
        return functions.d20() + self.get_speed()
#Check to see if Enemy is still alive
    def check_alive(self):
        return self._health > 0
        
class Wolf(Enemy):
    def __init__(self):
        super().__init__(20, 10, 5, 5.0)
           
    def bite_attack(self, target):
           if self.check_alive():
               target.take_damage(self._attack1)
           else:
               print('Wolf has been slain')
               
    def claw_attack(self, target):
        if self.check_alive():
            target.take_damage(self._attack2)
        else:
            print('Wolf has been slain') 
            
            
##########################################################################
#=======================   Test Function   ==============================#
##########################################################################

#ranger = Ranger()
#wolf = Wolf()

#print("Ranger attacks wolf:")
#ranger.sword_attack(wolf)
#print('Wolf stats after attack:', wolf.get_stats())

#print("Wolf bites ranger:")
#wolf.bite_attack(ranger)
#print('Ranger stats after bite:', ranger.get_stats())