#!/usr/bin/env python3


class SolidMotor:
    def __init__(self, grains, propellant, nozzle):
        self.grains = grains
        self.propellant = propellant
        self.nozzle = nozzle


class Grains:
    def __init__(self, num, length, diameter, core_diameter):
        self.num = num
        self.length = length
        self.diameter = diameter
        self.core_diameter = core_diameter
        self.web = (diameter - core_diameter)/2


class Propellant:
    def __init__(self, a, n, density, gamma, cstar, mol_mass):
        self.a = a
        self.n = n
        self.density = density
        self.gamma = gamma
        self.cstar = cstar
        self.mol_mass = mol_mass


class Nozzle:
    def __init__(self, throat_diameter, exit_diameter):
        self.throat_diameter = throat_diameter
        self.exit_diameter = exit_diameter


if __name__ == '__main__':

    prop = Propellant(a=0.0263, n=0.3289, density=0.058, gamma=1.254, cstar=5854.4, mol_mass=24.2291)
    nozzle = Nozzle(throat_diameter=1.4, exit_diameter=3.01)
    grains = Grains(num=3, length=9.5, diameter=5.014, core_diameter=2)

    motor = SolidMotor(grains, prop, nozzle)