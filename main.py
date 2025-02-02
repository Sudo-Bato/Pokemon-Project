class Pokemon:
    def __init__(self, name, type, pv):
        self.name = name
        self.type = type
        self.pv = pv

    def greet(self):
        return f"{self.name} greets you."
    
Pikachu = Pokemon("Pikachu", "Electrik", 100)

print(Pikachu.greet())
        