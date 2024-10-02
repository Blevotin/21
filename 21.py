class Horse():
    def __init__(self):
        self.x_distance = 0;
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx;

class Eagle():
    def __init__(self):
        self.y_distance = 0
        self.sound2 = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.fly(dy)
        self.run(dx)

    def get_pos(self):
        print(self.x_distance, self.y_distance)

    def voice(self):
        print(f"{self.sound}")
        print(f"{self.sound2}")

p1 = Pegasus()

p1.get_pos()
p1.move(10, 15)
p1.get_pos()
p1.move(5, 20)
p1.get_pos()

p1.voice()

# print(Pegasus.__mro__)