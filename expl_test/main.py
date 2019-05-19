def func(a, b, e=3):
    try:
        c = int(a) + int(b) + int(e)
    except ValueError:
        raise ValueError("fff")
    return c