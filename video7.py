def cost(b):
    return (b-4) ** 2

print(cost(5))

def num_slope(b):
    h=0.0001
    return (cost(b+h) - cost(b))/h

print(num_slope(5))

def slope(b):
    return 2 * (b -4)

print(slope(5))