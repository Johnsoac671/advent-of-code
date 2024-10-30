from hashlib import md5

def check_hash(string, target):
    result = md5(string.encode()).hexdigest()
    
    return result if result[:len(target)] == target else None


def get_valid_hash(key, target):
    x = 1
    
    while True:
        test_value = key + str(x)
        
        if check_hash(test_value, target):
            return x
        
        x += 1
        
        
print(f"Five zeroes: {get_valid_hash("bgvyzdsv", "00000")}")
print(f"Five zeroes: {get_valid_hash("bgvyzdsv", "000000")}")