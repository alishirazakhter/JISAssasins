'''
courage is a dog
courage has health value of 100
when courage walks the health value decreases by 1
when courage runs the health value decreases by 5
courage can see the health status
'''

class Dog:
    def __init__(self,initial_health):
        self.health = initial_health
    def walk(self):
        self.health-=1
    def run(self):
        self.health-=5
    def status(self):
        print("Courages health status = {}".format(self.health))

courage=Dog(100)
courage.walk()
courage.walk()
courage.walk()
courage.walk()
courage.walk()
courage.walk()
courage.run()
courage.run()
courage.run()
courage.run()
courage.run()
courage.status()

