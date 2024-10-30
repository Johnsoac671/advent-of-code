def houses_visited(directions):
    visited_houses = {(0,0)}
    movements = {"^" : (0, 1), ">" : (1, 0), "v" : (0, -1), "<" : (-1, 0)}
    
    santa_location = (0, 0)
    
    for direction in directions:
        movement = movements[direction]
        
        santa_location = (santa_location[0] + movement[0], santa_location[1] + movement[1])
        
        visited_houses.add(santa_location)
    
    return visited_houses


def num_houses_visited(directions):
    return len(houses_visited(directions))


def robo_santa(directions):
    santa_directions = []
    robo_directions = []
    
    for x in range(len(directions)):
        if x % 2 == 0:
            santa_directions.append(directions[x])
        else:
            robo_directions.append(directions[x])
    
    santa_houses = houses_visited(santa_directions)
    robo_houses = houses_visited(robo_directions)
    
    return len(santa_houses.union(robo_houses))
            


def test():
    with open("2015/day 3/input.txt", "r") as file:
        line = file.read()
        
        print(f"Number of houses visited by Santa alone: {num_houses_visited(line)}")
        print(f"Number of houses visited by Santa and Robo-Santa: {robo_santa(line)}")
        
test()