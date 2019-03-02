class Person:

    def __init__(self, name):
        self.name = name


    def reveal_yourself(self):
        print(f"My name is {self.name}")


class SuperHero(Person):

    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name =hero_name


    def reveal_yourself(self):
        super(SuperHero,self).reveal_yourself()
        print(f'...and im also {self.hero_name}')



# rob = Person('Rob')
# rob.reveal_yourself()

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_yourself()
