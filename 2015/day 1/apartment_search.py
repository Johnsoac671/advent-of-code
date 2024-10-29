from itertools import accumulate

def find_apartment(string):
    return sum(map(lambda x: 1 if x == "(" else -1, string))


def enter_basement(string):
    running_totals = list(accumulate(map(lambda x: 1 if x == "(" else -1, string)))
    
    return running_totals.index(-1) + 1 if -1 in running_totals else None
     


def test():
    with open(r"2015\day 1\input.txt", "r") as file:
        string = file.read()
        print(f"Santa needs to go to apartment: {find_apartment(string)}")
        print(f"Santa enters the basement on move: {enter_basement(string)}")

test()