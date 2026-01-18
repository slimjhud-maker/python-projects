from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, opponent):
        pass

    @abstractmethod
    def defend(self):
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0


class Warrior(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, opponent):
        hit = random.randint(1, 100)
        crit = random.randint(1, 100)

        if hit <= 70:
            return f"{self.name} misses the attack!"

        damage = 10
        if crit <= 20:
            damage *= 2
            text = f"CRITICAL HIT! {self.name} deals {damage} damage!"
        else:
            text = f"{self.name} slashes for {damage} damage!"

        opponent.take_damage(damage)
        return text

    def defend(self):
        return "Warrior blocks with a heavy shield!"


class Wizard(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, opponent):
        hit = random.randint(1, 100)
        crit = random.randint(1, 100)

        if hit <= 60:
            return f"{self.name}'s fireball misses!"

        damage = 15
        if crit <= 25:
            damage *= 2
            text = f"CRITICAL HIT! {self.name} blasts for {damage} damage!"
        else:
            text = f"{self.name} casts a fireball for {damage} damage!"

        opponent.take_damage(damage)
        return text

    def defend(self):
        return "Wizard raises a magic barrier!"


class Archer(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, opponent):
        hit = random.randint(1, 100)
        crit = random.randint(1, 100)

        if hit <= 50:
            return f"{self.name}'s arrow misses!"

        damage = 12
        if crit <= 30:
            damage *= 2
            text = f"CRITICAL HIT! {self.name} fires a deadly arrow for {damage} damage!"
        else:
            text = f"{self.name} shoots an arrow for {damage} damage!"

        opponent.take_damage(damage)
        return text

    def defend(self):
        return "Archer dodges swiftly!"


warrior = Warrior("Warrior", 100)
wizard = Wizard("Wizard", 80)
archer = Archer("Archer", 90)

print(f"""
Creating characters...

{warrior.name} - Health: {warrior.health}
{wizard.name} - Health: {wizard.health}
{archer.name} - Health: {archer.health}

Battle begins!

{warrior.attack(wizard)}
{wizard.attack(archer)}
{archer.attack(warrior)}

{warrior.defend()}
{wizard.defend()}
{archer.defend()}

After round 1:
{warrior.name} health: {warrior.health}
{wizard.name} health: {wizard.health}
{archer.name} health: {archer.health}
""")