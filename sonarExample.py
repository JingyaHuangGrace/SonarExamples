def add(a, b):
    return a + b

def compare(a, b):
    if a > b:
        print(f"{a} > {b}")
    elif a == b: # duplicate condition fixed
        print(f"{a} = {b}")
    else:
        print(f"{a} < {b}")

if __name__ == "__main__":
    a, b, c, d = 2, 2, 4, 3
    
    print(f"a + b = {add(a, b)}")
    add(a,b)
    compare(a, b)
    compare(c, d)
