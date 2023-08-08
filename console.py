#!/usr/bin/python3

from models import Vehicle

Car = Vehicle(4, "Venza")

print(Car.brand)
print(Car.num_of_tires)

Car.num_of_tires = 8

print(Car.brand)
print(Car.num_of_tires)
