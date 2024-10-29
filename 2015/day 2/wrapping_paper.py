def get_paper_amount(string):
    l, w, h = map(int, string.split("x"))
    
    dimensions = (2*l*w, 2*w*h, 2*l*h)
    
    smallest = min(dimensions) // 2
    
    return sum(dimensions) + smallest


def get_ribbon_amount(string):
    l, w, h = map(int, string.split("x"))
    
    dimensions = (2*l, 2*w, 2*h)
    
    longest = max(dimensions)
    
    return (sum(dimensions) - longest) + (l * w * h)


def test():
    with open("2015/day 2/input.txt", "r") as file:
        lines = file.readlines()
        
        print(f"Paper needed: {sum(map(get_paper_amount, lines))} sqft")
        print(f"Ribbon needed: {sum(map(get_ribbon_amount, lines))} sqft")


test()
