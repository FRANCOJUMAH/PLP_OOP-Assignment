class Superhero:
    def __init__(self, name, alias, power, weakness):
        self.name = name
        self.alias = alias
        self.power = power
        self._weakness = weakness  # Encapsulation: Marking weakness as private
    
    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    def reveal_identity(self):
        return f"My real name is {self.name}."

    def get_weakness(self):
        return f"{self.alias}'s weakness is {self._weakness}."                                                                                                                                      
    


    # Derived Class 
    # This subclass FlyingHero inherits from Superhero but adds a new flying ability


    class FlyingHero(Superhero):
    def __init__(self, name, alias, power, weakness, flight_speed):
        super().__init__(name, alias, power, weakness)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.alias} flies at {self.flight_speed} and uses {self.power}!"

# Creating objects
hero1 = Superhero("Bruce Wayne", "Batman", "Genius intellect and martial arts", "Human limitations")
hero2 = FlyingHero("Clark Kent", "Superman", "Super strength and heat vision", "Kryptonite", "Super-sonic speed")

# Testing methods
print(hero1.use_power())
print(hero1.get_weakness())
print(hero2.use_power()) 


# Encapsulation: _weakness is a private attribute, accessible only via a method
# Polymorphism: use_power() is overridden in FlyingHero
# Inheritance: FlyingHero inherits from Superhero and adds flight_speed