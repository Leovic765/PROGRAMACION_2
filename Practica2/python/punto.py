import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return f"Coordenadas Cartesianas: ({self.x}, {self.y})"

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return f"Coordenadas Polares: (r={r:.2f}, θ={math.degrees(theta):.2f}°)"

    def __str__(self):
        return f"Punto({self.x}, {self.y})"
