def get_number_from_pos(x,y):

    if(101 > x > 0 and 101 > y > 0):
        number = 0
    elif(201 > x > 100 and 101 > y > 0):
        number = 1
    elif(301 > x > 200 and 101 > y > 0):
        number = 2
    elif(101 > x > 0 and 201 > y > 100):
        number = 3
    elif(201 > x > 100 and 201 > y > 100):
        number = 4
    elif(301 > x > 200 and 201 > y > 100):
        number = 5
    elif(101 > x > 0 and 301 > y > 200):
        number = 6
    elif(201 > x > 100 and 301 > y > 200):
        number = 7
    elif(301 > x > 200 and 301 > y > 200):
        number = 8
    else:
        number = 100
    return number

def get_pos_from_number(x,y):

    if(101 > x > 0 and 101 > y > 0):
        number = 0
    elif(201 > x > 100 and 101 > y > 0):
        number = 1
    elif(301 > x > 200 and 101 > y > 0):
        number = 2
    elif(101 > x > 0 and 201 > y > 100):
        number = 3
    elif(201 > x > 100 and 201 > y > 100):
        number = 4
    elif(301 > x > 200 and 201 > y > 100):
        number = 5
    elif(101 > x > 0 and 301 > y > 200):
        number = 6
    elif(201 > x > 100 and 301 > y > 200):
        number = 7
    elif(301 > x > 200 and 301 > y > 200):
        number = 8
    else:
        number = 100
    return number

def play_mode(n,m):
    if(84 < m < 117 and 328 < n < 472):
        mode = 1
    elif(184 < m < 217 and 328 < n < 520):
        mode = 2
    else:
        mode = 100
    return mode


#(328, 84) (328, 117)
#(472, 84) (472, 117)

#(328, 184) (520, 184)
#(328, 217) (520, 217)

def get_pos_from_number(temp):
    if(temp == 0):
        return 6, 6
    if (temp == 1):
        return 106, 6
    if (temp == 2):
        return 206, 6
    if (temp == 3):
        return 6, 106
    if (temp == 4):
        return 106, 106
    if (temp == 5):
        return 206, 106
    if (temp == 6):
        return 6, 206
    if (temp == 7):
        return 106, 206
    if (temp == 8):
        return 206, 206

# (0,0) (100,0) (200,0) (300,0)
# (0,100) (100,100) (200,100) (300,100)
# (0,200) (100,200) (200,200) (300,200)
# (0,300) (100,300) (200,300) (300,300)

#(328, 84) (328, 117)
#(472, 84) (472, 117)

#(328, 184) (328, 217)
#(328, 217) (520, 217)
