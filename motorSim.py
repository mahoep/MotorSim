#!/usr/bin/env python3

from math import pi


class SolidMotor:
    def __init__(self, grains, propellant, nozzle):
        self.grains = grains
        self.propellant = propellant
        self.nozzle = nozzle

    def simulate(self):
        pressure = 14.7
        self.propellant.mass = (pi/4 * self.grains.diameter**2 - pi/4 * self.grains.core_diameter**2) * \
                self.grains.length * self.grains.num * self.propellant.density

        throatArea = self.nozzle.throat_diameter**2 * pi/4
        dt = 0.0001
        time = 0
        pressure_data = []
        time_data = []
        while 1:
            burnArea = (pi/4 * self.grains.diameter**2 - pi/4 * self.grains.core_diameter**2) * 2 * self.grains.num + \
                       self.grains.core_diameter * pi * self.grains.length * self.grains.num

            amount_burned = self.propellant.a * pressure ** self.propellant.n * dt

            pressure = (burnArea / throatArea * self.propellant.density * self.propellant.cstar * self.propellant.a*12/386.06) ** \
                       (1 / (1 - self.propellant.n))

            self.grains.core_diameter += amount_burned*2
            self.grains.length -= amount_burned*2


            time += dt
            pressure_data.append(pressure)
            time_data.append(time)
            if self.grains.core_diameter >= self.grains.diameter:
                break


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
    motor.simulate()