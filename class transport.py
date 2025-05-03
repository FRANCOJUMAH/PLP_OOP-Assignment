class Transport:
    def move(self):
        pass  # Placeholder method

class Car(Transport):
    def move(self):
        return "🚗 Driving"

class Plane(Transport):
    def move(self):
        return "✈️ Flying"

class Boat(Transport):
    def move(self):
        return "⛵ Sailing"

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Testing polymorphism
for vehicle in vehicles:
    print(vehicle.move())


# Polymorphism: Each subclass defines move() differently
# Inheritance: Car, Plane, and Boat inherit from Transport
# Scalability: We can easily add more transport types (like Train)
