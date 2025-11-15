def square_pattern(n) :
    for i in range(n) :
        print("*" * n)

def triangle(n) :
    j = 1
    for i in range(n) :
        print("# " * j)
        j+=1

def right_triangle_pattern(n) :
    for i in range(1,n+1) :
        print("# " * i)

def inverted_triangle(n) :
    for i in range(n,0,-1) :
        print("# " * i)


def pyramid_pattern(n) : 
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
      

# inverted_triangle(5)
# square_pattern(5)
# triangle(5)
# right_triangle_pattern(5)
pyramid_pattern(5)