class PacPerson():
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        pass

    def hit(self):
        pass

    def gettingHit(self):
        pass

    def eat(self):
        pass

    def respawn(self):
        pass

class Ghost():
    def __init__(self, speed, behavior, color):
        self.speed = speed
        self.behavior = behavior
        self.color = color
    
    def move(self):
        pass

    def hit(self):
        pass

    def gettingHit(self):
        pass

    def eat(self):
        pass

    def respawn(self):
        pass

PacMan = PacPerson(15)
Pinky = Ghost(5, "surprise", "pink")
Blinky = Ghost(10, "follow", "red")