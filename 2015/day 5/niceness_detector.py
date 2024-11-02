def is_nice(string):
    vowels = {"a", "e", "i", "o", "u"}
    naughty_letters = {"ab", "cd", "pq", "xy"}
    
    num_vowels = 0
    num_doubles = 0
    prev_char = "0"
    
    for char in string:
        
        if prev_char + char in naughty_letters:
            return False
        
        if char in vowels:
            num_vowels += 1
        
        if char == prev_char:
            num_doubles += 1

        prev_char = char
    return (num_vowels >= 3) and (num_doubles >= 1)


def test():
    with open("2015/day 5/input.txt", "r") as file:
        lines = file.readlines()
        
        print(f"Nice Strings: {len(list(filter(is_nice, lines)))}")


test()
            
        