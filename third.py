import matplotlib.pyplot as plt

limit_spiral = 1024
limit_six = 530
limit_ulam = 1024

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def six_generator(limit_six):
    six_array = []
    for i in range(limit_six):
        n_minus = i*6 - 1
        n_plus = i*6 + 1
        if is_prime(n_minus):
            six_array.append([n_minus, "*"])
        elif is_prime(n_minus) == False:
            six_array.append(["{}*6 -1".format(i), " "])
        if is_prime(n_plus):
            six_array.append([n_plus, "*"])
        elif is_prime(n_plus) == False:
            six_array.append(["{}*6 +1".format(i), " "])
    return six_array

def ulam_gen(limit_ulam):
    ulam_array = []
    for i in range(limit_ulam):
        if is_prime(i):
            ulam_array.append("*")
        else:
            ulam_array.append(" ")
    return ulam_array

def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

moves = [move_right, move_down, move_left, move_up]

def gen_points(end):
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    yield [n,pos]

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n+=1
                yield [n,pos]

        times_to_move+=1

spiral = list(gen_points(limit_spiral))
lista1 = six_generator(limit_six)
lista2 = ulam_gen(limit_ulam)

for index, item in enumerate(spiral):
    item.append(lista2[index][0])

coordinates = []

for item in spiral:
    if(item[2] == "*"):
        coordinates.append(item[1])
x = []
y = []

for item in coordinates:
    x.append(item[0])
    y.append(item[1])

plt.plot(x, y, 'o')
plt.show()
