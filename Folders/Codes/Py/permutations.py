def permutations(array: list):
    length = len(array)

    if length == 0:
        return []

    elif length == 1:
        return [[]]

    else:
        for i in length:
            letter = 