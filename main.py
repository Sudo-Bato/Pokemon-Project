# All the classes

# Pokemon class
class Pokemon:
    def __init__(self, name, type, pv):
        self.name = name
        self.type = type
        self.pv = pv

    def greet(self):
        return f"{self.name} vous salue."
    
    def attack(self, target, damage):
        target.pv -= damage
        if target.pv <= 0:
            return f"{self.name} a infligé {damage} de dégats a {target.name}, {target.name} est K.O !"
        return f"{self.name} a infligé {damage} de dégats a {target.name}."
        

# Start of the game
print("Welcome ! I am professor Chen.")

print("To start your journey, you will need a little companion")

print("Chose one among the tree starters")

    
# Starters available
starters = ["pikachu", "charmander", "eevee"]

# Chosing a starter
while True:
    starter_choice = input("Type the name of the starter (Pikachu / Charmander / Eevee) : ").lower()
    if starter_choice in starters:
        break
    print("Invalid choice. Please choose Pikachu, Charmander, or Eevee.")

if starter_choice == "pikachu":
    user_pokemon = Pokemon("Pikachu", "Electrik", 250)
elif starter_choice == "charmander":
    user_pokemon = Pokemon("Charmander", "Fire", 250)
elif starter_choice == "eevee":
    user_pokemon = Pokemon("Eevee", "Normal", 250)

print(user_pokemon.greet())
