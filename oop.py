class Character:
    def __init__(self, rank, speed):
        self.rank = rank
        self.speed = speed
    def increase_speed(self):
        self.speed += 10


chief = Character(1, 20)
soldier = Character(39, 5)

print(f"Chief Speed: {chief.speed}")
print(f"Soldier Speed: {soldier.speed}")
soldier.increase_speed()
print(f"Chief Speed: {chief.speed}")
print(f"Soldier Speed: {soldier.speed}")