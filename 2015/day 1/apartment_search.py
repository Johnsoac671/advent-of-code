def find_apartment(string):
    return sum(map(lambda x: 1 if x == "(" else ")", string))