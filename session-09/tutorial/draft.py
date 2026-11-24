class Lion:
    
    def __init__(self, name, age, strength, hunger_level=6):
        """Initialize attributes to describe a lion."""
        self.name = name
        self.age = age
        self.strength = strength
        self.hunger_level = hunger_level# Default value if not provided
    def __str__(self):
        bla = f"{self.hunger_level} - {self.name}"
        return bla
    
fff = Lion('f', 89 , 'op')
print(fff)
ggg = Lion('g', 89 , 'op', 90)
print(ggg)


