# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# PRIMARY CLASS
class Vehicle():
    pass

# 2ND TIER CLASSES
class GroundVehicle(Vehicle):
    pass

class FlightVehicle(Vehicle):
    pass

# 3RD TIER CLASSES
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass