def is_prime(x, int):
    if  x < 2:
        return False
    else:
        for i in range(2, x - 1):
            if x %  x == 0:
                return False
        return True
