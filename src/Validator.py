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
