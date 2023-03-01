from Euclid import Euclid
from Sorting import merge_sort
from Bruteforce import compute_bruteforce
from Randomizer import *

euclid = Euclid()


def compute_DnC(points):
    assert len(points) > 1, "list should contain at least 2 point"
    euclid.call_counter = 0
    pointsx = merge_sort(points, 0)
    pointsy = merge_sort(points, 1)
    return DnC(pointsx, pointsy)


def conquer_strip(pointsy, mid_x, min_dist):
    strip_points = [point for point in pointsy if abs(
        point[0] - mid_x) <= min_dist]
    dimension = len(pointsy[0])

    closest_pair = (0, 0)
    strip_length = len(strip_points)
    for i in range(strip_length):
        for j in range(i+1, strip_length):
            if abs(strip_points[i][1] - strip_points[j][1]) >= min_dist:
                break
            skip = False
            for d in range(2, dimension):
                if abs(strip_points[i][d] - strip_points[j][d]) >= min_dist:
                    skip = True
                    break
            if skip:
                continue
            new_dist = euclid.distance(strip_points[i], strip_points[j])
            if new_dist < min_dist:
                min_dist = new_dist
                closest_pair = (strip_points[i], strip_points[j])

    return euclid.call_counter, min_dist, closest_pair


def DnC(pointsx, pointsy):
    length = len(pointsx)
    if length <= 3:
        answer_brute = compute_bruteforce(pointsx)
        euclid.call_counter += answer_brute[0]
        return answer_brute

    mid = length//2
    list1x = pointsx[:mid]
    list2x = pointsx[mid:]
    mid_x = pointsx[mid-1][0]

    list1y = []
    list2y = []
    for point in pointsy:
        if point[0] <= mid_x:
            list1y.append(point)
        if point[0] >= mid_x:
            list2y.append(point)

    answer_left = DnC(list1x, list1y)
    answer_right = DnC(list2x, list2y)

    dist = answer_left[1]
    closest_pair = answer_left[2]
    if answer_right[1] < dist:
        dist = answer_right[1]
        closest_pair = answer_right[2]

    answer_strip = conquer_strip(pointsy, mid_x, dist)
    if answer_strip[1] < dist:
        dist = answer_strip[1]
        closest_pair = answer_strip[2]

    return euclid.call_counter, dist, closest_pair


def loop_driver():
    for i in range(1000):
        points = random_points(1000, 5, 100000000)
        call_counter, dist, closest_pair = compute_bruteforce(points)
        call_counter2, dist2, closest_pair2 = compute_DnC(points)
        if dist != dist2:
            print("wrong")
            print(dist)
            print(dist2)
            print()


def dnc2_driver():
    for i in range(10):
        points = random_points(200, 2, 1000)
        call_counter, dist, closest_pair = compute_bruteforce(points)
        call_counter2, dist2, closest_pair2 = compute_DnC(points)
        call_counter3, dist3, closest_pair3 = compute_DnC2(points)
        print(f"brute euclid call : {call_counter}")
        print(f"DnC euclid call : {call_counter2}")
        print(f"DnC2 euclid call : {call_counter3}")
        print()
        print(f"distance brute : {dist}")
        print(f"distance DnC : {dist2}")
        print(f"distance DnC2 : {dist3}")
        print()


if __name__ == "__main__":
    dnc2_driver()

    # loop_driver()
