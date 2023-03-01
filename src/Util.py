def point_to_string(point):
    string = "("
    for xyz in point:
        string += f"{xyz:0.2f}, "
    string = string[:-2] + ")"
    return string


def validate_n(n):
    try:
        n = int(n)
        if n < 2:
            return "points must contain at least 2 point"
        else:
            return n
    except:
        return "please input an integer"


def validate_limit(limit):
    try:
        limit = float(limit)
        return limit
    except:
        return "please input correct decimal value"


def validate_d(d):
    try:
        d = int(d)
        if d < 2:
            return "please input at least 2 dimension"
        else:
            return d
    except:
        return "please input an integer"
