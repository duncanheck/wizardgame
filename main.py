import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.evade_next = False
        self.shielded = False

    def attack(self, opponent):
        if opponent.evade_next:
            print(f"{opponent.name} evades the attack!")
            opponent.evade_next = False
            return
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        if opponent.shielded:
            damage = 0
            opponent.shielded = False
            print(f"{opponent.name} blocks the attack with Divine Shield!")
        else:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        if self.health < self.max_health:
            heal_amount = random.randint(10, 20)
            self.health = min(self.max_health, self.health + heal_amount)
            print(f"{self.name} heals for {heal_amount} HP! Current health: {self.health}/{self.max_health}")
        else:
            print(f"{self.name}'s health is already full!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses Power Strike for {damage} damage!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} casts Fireball for {damage} damage!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def special_ability(self, opponent):
        print(f"{self.name} uses Quick Shot! Two rapid attacks:")
        self.attack(opponent)
        self.attack(opponent)

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)

    def special_ability(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} activates Divine Shield and will block the next attack!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 10)
        self.health += regen
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}")

# Character creation
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Turn-based battle system
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                sub = input("Use (1) Quick Shot or (2) Evade? ")
                if sub == '1':
                    player.special_ability(wizard)
                elif sub == '2':
                    player.evade()
                else:
                    print("Invalid choice.")
            elif isinstance(player, Paladin):
                sub = input("Use (1) Holy Strike or (2) Divine Shield? ")
                if sub == '1':
                    player.special_ability(wizard)
                elif sub == '2':
                    player.divine_shield()
                else:
                    print("Invalid choice.")
            else:
                player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! Game Over.")
            break

    if wizard.health <= 0:
        print(f"🎉 The wizard {wizard.name} has been defeated by {player.name}! Victory!")

# Main entry point
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()