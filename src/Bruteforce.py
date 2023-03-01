from Euclid import Euclid


def compute_bruteforce(points):
    # assert len(points) > 1, "list should contain at least 2 point"
    euclid = Euclid()
    min_dist = float('inf')
    amount = len(points)
    closest_pair = (0, 1)
    for i in range(amount):
        for j in range(i+1, amount):
            new_dist = euclid.distance(points[i], points[j])
            if new_dist < min_dist:
                min_dist = new_dist
                closest_pair = (points[i], points[j])

    return euclid.call_counter, min_dist, closest_pair


if __name__ == "__main__":
    points = [[1, 2], [2, 3], [10, 2], [4, 4]]
    call_counter, dist, closest_pair = compute_bruteforce(points)
    print(f"euclid call : {call_counter}")
    print(f"distance : {dist}")
    print(
        f"closest point : {points[closest_pair[0]]}, {points[closest_pair[1]]}")
    print()

    points = [[1, 2, 3, 4], [2, 3, 4, 5], [10, 2, 12, 6], [4, 4, 4, 4]]
    call_counter, dist, closest_pair = compute_bruteforce(points)
    print(f"euclid call : {call_counter}")
    print(f"distance : {dist}")
    print(
        f"closest point : {points[closest_pair[0]]}, {points[closest_pair[1]]}")

    from Randomizer import *
    points = random_points(100, 5, 1000)
    call_counter, dist, closest_pair = compute_bruteforce(points)
    print(f"euclid call : {call_counter}")
    print(f"distance : {dist}")
    print(
        f"closest point : {points[closest_pair[0]]}, {points[closest_pair[1]]}")
