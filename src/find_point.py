import math

def point_from_origin(degrees, magnitude):
    radians = math.radians(degrees)
    x = magnitude * math.cos(radians)
    y = magnitude * math.sin(radians)
    return x, y

# Example usage
degrees = 45
magnitude = 10.5
print(point_from_origin(degrees, magnitude))

