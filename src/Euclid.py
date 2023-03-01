from math import sqrt


class Euclid:
    def __init__(self):
        self.call_counter = 0

    def distance(self, p1, p2):
        assert len(p1) == len(p2), "Both point should have equal length"
        self.call_counter += 1
        dist2 = 0
        for x1, x2 in zip(p1, p2):
            dx = abs(x1 - x2)
            dist2 += dx*dx
        return sqrt(dist2)
