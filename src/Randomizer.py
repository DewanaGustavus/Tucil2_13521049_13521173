import random

def random_points(n, m, limit):
    # ? make random so 2 point can't locate in same place
    points = [[random.uniform(0,limit) for __ in range(m)] for _ in range(n)]
    return points

def xyz_random_points(n, limit):
    x = [random.uniform(0,limit) for _ in range(n)]
    y = [random.uniform(0,limit) for _ in range(n)]
    z = [random.uniform(0,limit) for _ in range(n)]
    return (x, y, z)
    
if __name__ == "__main__":
    print(random_points(3,2,10))
    print(random_points(10,4,20))