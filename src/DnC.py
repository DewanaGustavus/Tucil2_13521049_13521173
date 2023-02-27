from Euclid import Euclid
from Sorting import merge_sort
from Bruteforce import compute_bruteforce

euclid = Euclid()

def compute_DnC(points):
    assert len(points) > 1, "list should contain at least 2 point"
    points = merge_sort(points, 0)
    points = merge_sort(points, 1)
    return DnC(points)
    
def conquer_strip(points, min_dist):
    strip_points = []
    mid = len(points)//2
    for point in points:
        if(abs(point[1] - points[mid][1]) < min_dist):
            strip_points.append(point)
    
    euclid = Euclid()
    closest_index = (0, 1)
    strip_length = len(strip_points)
    for i in range(strip_length):
        for j in range(i+1, strip_length):
            if abs(points[i][1] - points[j][1]) >= min_dist:
                break
            new_dist = euclid.distance(points[i], points[j])
            if new_dist < min_dist:
                min_dist = new_dist
                closest_index = (i, j)
    
    return euclid.call_counter, min_dist, closest_index

def DnC(points):
    length = len(points)
    if length <= 3:
        answer_brute = compute_bruteforce(points)
        euclid.call_counter += answer_brute[0]
        return answer_brute
    
    mid = length//2
    list1 = points[:mid]
    list2 = points[mid:]
    answer_left = DnC(list1)
    answer_right = DnC(list2)
    
    dist = answer_left[1]
    closest_index = answer_left[2]
    if answer_right[1] < dist:
        dist = answer_right[1]
        closest_index = answer_right[2]
        
    answer_strip = conquer_strip(points, dist)
    euclid.call_counter += answer_strip[0]
    if answer_strip[1] < dist:
        dist = answer_strip[1]
        closest_index = answer_strip[2]

    return euclid.call_counter, dist, closest_index


if __name__ == "__main__":
    points = [[1,2], [2,3], [10,2], [4,4]]
    call_counter, dist, closest_index = compute_DnC(points)
    print(f"euclid call : {call_counter}")
    print(f"distance : {dist}")
    print(f"closest point : {points[closest_index[0]]}, {points[closest_index[1]]}")
    print()
    
    points = [[1,2,3,4], [2,3,4,5], [10,2,12,6], [4,4,4,4]]
    call_counter, dist, closest_index = compute_DnC(points)
    print(f"euclid call : {call_counter}")
    print(f"distance : {dist}")
    print(f"closest point : {points[closest_index[0]]}, {points[closest_index[1]]}")
    print()
    
    from Randomizer import *
    points = random_points(100, 5, 1000)
    call_counter, dist, closest_index = compute_DnC(points)
    call_counter2, dist2, closest_index2 = compute_bruteforce(points)
    print(f"DnC euclid call : {call_counter}")
    print(f"brute euclid call : {call_counter2}")
    print(f"distance DnC : {dist}")
    print(f"distance brute : {dist2}")
    print(f"closest point : {points[closest_index2[0]]}, {points[closest_index2[1]]}")
    print()