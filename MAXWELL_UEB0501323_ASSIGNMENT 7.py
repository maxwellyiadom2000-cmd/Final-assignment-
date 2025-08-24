import math

# ------------------------------
# Base Class
# ------------------------------
class PetroleumFormula:
    def calculate(self):
        raise NotImplementedError("This method should be overridden.")


# ------------------------------
# Child Classes for Each Formula
# ------------------------------

class HydrostaticPressure(PetroleumFormula):
    # P = ρ * g * h
    def __init__(self, density, depth, g=9.81):
        self.density = density
        self.depth = depth
        self.g = g

    def calculate(self):
        try:
            return self.density * self.g * self.depth
        except Exception as e:
            print(f"Error in HydrostaticPressure: {e}")


class DarcyFlow(PetroleumFormula):
    # Q = (k * A * ΔP) / (μ * L)
    def __init__(self, k, A, deltaP, mu, L):
        self.k = k
        self.A = A
        self.deltaP = deltaP
        self.mu = mu
        self.L = L

    def calculate(self):
        try:
            return (self.k * self.A * self.deltaP) / (self.mu * self.L)
        except Exception as e:
            print(f"Error in DarcyFlow: {e}")


class FormationVolumeFactor(PetroleumFormula):
    # Bo = Vb / Vo
    def __init__(self, Vb, Vo):
        self.Vb = Vb
        self.Vo = Vo

    def calculate(self):
        try:
            return self.Vb / self.Vo
        except ZeroDivisionError:
            print("Error: Vo cannot be zero!")


class GasCompressibilityFactor(PetroleumFormula):
    # Z = (P * V) / (n * R * T)
    def __init__(self, P, V, n, T, R=8.314):
        self.P = P
        self.V = V
        self.n = n
        self.T = T
        self.R = R

    def calculate(self):
        try:
            return (self.P * self.V) / (self.n * self.R * self.T)
        except ZeroDivisionError:
            print("Error: n*R*T cannot be zero!")


class ReynoldsNumber(PetroleumFormula):
    # Re = (ρ * v * D) / μ
    def __init__(self, density, velocity, diameter, mu):
        self.density = density
        self.velocity = velocity
        self.diameter = diameter
        self.mu = mu

    def calculate(self):
        try:
            return (self.density * self.velocity * self.diameter) / self.mu
        except ZeroDivisionError:
            print("Error: μ cannot be zero!")


class ProductivityIndex(PetroleumFormula):
    # J = Q / (Pe - Pw)
    def __init__(self, Q, Pe, Pw):
        self.Q = Q
        self.Pe = Pe
        self.Pw = Pw

    def calculate(self):
        try:
            return self.Q / (self.Pe - self.Pw)
        except ZeroDivisionError:
            print("Error: Pe and Pw cannot be equal!")


# ------------------------------
# Polymorphism Demonstration
# ------------------------------
def show_result(formula_obj):
    # Same interface for all formulas
    print(f"{formula_obj.__class__.__name__} result = {formula_obj.calculate()}")


# ------------------------------
# Main Program
# ------------------------------
if __name__ == "__main__":
    # Create objects
    f1 = HydrostaticPressure(density=1000, depth=1500)
    f2 = DarcyFlow(k=100, A=20, deltaP=500, mu=1, L=50)
    f3 = FormationVolumeFactor(Vb=1.2, Vo=1.0)
    f4 = GasCompressibilityFactor(P=2000000, V=0.05, n=100, T=350)
    f5 = ReynoldsNumber(density=850, velocity=2, diameter=0.1, mu=0.001)
    f6 = ProductivityIndex(Q=500, Pe=3000, Pw=2500)

    # Polymorphic function call
    formulas = [f1, f2, f3, f4, f5, f6]
    for formula in formulas:
        show_result(formula)
