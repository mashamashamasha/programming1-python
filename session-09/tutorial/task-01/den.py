class Den:
     
    def __init__(self):
        self.lions = []
        self.is_sealed = True

    def add_lion(self, lion):
        self.lion = lion
        if self.is_sealed == True:
            return
        self.lions.append(self.lion)

    def get_hunger_report(self):
        total_number = 0
        if self.is_sealed:
            return #works like a break for loops
        for lion in self.lions:
            total_number += 1
        total_hunger = sum(lion.hunger_level for lion in self.lions)
        if total_number > 0:
            average_hunger = total_hunger/total_number
        else:
            average_hunger = 0
        return {
        "lion_count": total_number, 
        "average_hunger": average_hunger
        }
    def open(self):
        self.is_sealed = False

    def close(self):
        self.is_sealed = True