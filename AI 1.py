import random
def board():
    global places
    print()
    print("\t\t\t\t\t\t\t\t\t  ━   ━   ━ ")
    print(f"\t\t\t\t\t\t\t\t\t┃ {places[0][0]} ┃ {places[0][1]} ┃ {places[0][2]} ┃\t\t     1   2   3")
    print("\t\t\t\t\t\t\t\t\t  ━   ━   ━ ")
    print(f"\t\t\t\t\t\t\t\t\t┃ {places[1][0]} ┃ {places[1][1]} ┃ {places[1][2]} ┃\t\t     4   5   6")
    print("\t\t\t\t\t\t\t\t\t  ━   ━   ━ ")
    print(f"\t\t\t\t\t\t\t\t\t┃ {places[2][0]} ┃ {places[2][1]} ┃ {places[2][2]} ┃\t\t     7   8   9")
    print("\t\t\t\t\t\t\t\t\t  ━   ━   ━ ")
    print()

def check_win():
    global places,user,pc
    r1 = places[0][0] == places[0][1] == places[0][2] =='✘'
    r2 = places[1][0] == places[1][1] == places[1][2] =='✘'
    r3 = places[2][0] == places[2][1] == places[2][2] =='✘'
    c1 = places[0][0] == places[1][0] == places[2][0] =='✘'
    c2 = places[0][1] == places[1][1] == places[2][1] =='✘'
    c3 = places[0][2] == places[1][2] == places[2][2] =='✘'
    d1 = places[0][0] == places[1][1] == places[2][2] =='✘'
    d2 = places[0][2] == places[1][1] == places[2][0] =='✘'
    su = sum(user[0]) + sum(user[1]) + sum(user[2])
    sp = sum(pc[0]) + sum(pc[1]) + sum(pc[2])
    pr1 = places[0][0] == places[0][1] == places[0][2] == 'O'
    pr2 = places[1][0] == places[1][1] == places[1][2] == 'O'
    pr3 = places[2][0] == places[2][1] == places[2][2] == 'O'
    pc1 = places[0][0] == places[1][0] == places[2][0] == 'O'
    pc2 = places[0][1] == places[1][1] == places[2][1] == 'O'
    pc3 = places[0][2] == places[1][2] == places[2][2] == 'O'
    pd1 = places[0][0] == places[1][1] == places[2][2] == 'O'
    pd2 = places[0][2] == places[1][1] == places[2][0] == 'O'
    #print(r1,r2,r3,c1,c2,c3,d1,d2)
    if r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2:
        return True,'✘'
    elif pr1 or pr2 or pr3 or pc1 or pc2 or pc3 or pd1 or pd2:
        return True,'O'
    elif su+sp==9:
        return True,'Draw'
    return False,'DOe'

def announce(who):
    print()
    print('\t\t\t\t\t\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    if who=='O':
        print("\t\t\t\t\t\t\t\t\t\t\tYayy!! I won the match")
    elif who=='✘':
        print("\t\t\t\t\t\t\t\t\t\t\t\tYou won the match!!")
    else:
        print("\t\t\t\t\t\t\t\t\t\t\t\tAyyo!! Its a Draww")
    print('\t\t\t\t\t\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def player_turn():
    global places,last
    while True:
        place=int(input("Now its your turn :"))-1
        pos=places[place//3][place%3]
        if not (0<=place<=9):
            print("Enter the number in tha range (1-9)!!")
        elif pos==' ' :
            places[place // 3][place % 3]='✘'
            user[place // 3][place % 3]=True
            last=(place // 3,place % 3)
            break
        else:
            print("Place is already occupied!!")
            print()

def system():
    global places,user,last,pc
    r1 = [user[0][0] , user[0][1] , user[0][2]]
    r2 = [user[1][0] , user[1][1] , user[1][2]]
    r3 = [user[2][0] , user[2][1] , user[2][2]]
    c1 = [user[0][0] , user[1][0] , user[2][0]]
    c2 = [user[0][1] , user[1][1] , user[2][1]]
    c3 = [user[0][2] , user[1][2] , user[2][2]]
    d1 = [user[0][0] , user[1][1] , user[2][2]]
    d2 = [user[0][2] , user[1][1] , user[2][0]]
    #pc status
    pr1 = [pc[0][0], pc[0][1], pc[0][2]]
    pr2 = [pc[1][0], pc[1][1], pc[1][2]]
    pr3 = [pc[2][0], pc[2][1], pc[2][2]]
    pc1 = [pc[0][0], pc[1][0], pc[2][0]]
    pc2 = [pc[0][1], pc[1][1], pc[2][1]]
    pc3 = [pc[0][2], pc[1][2], pc[2][2]]
    pd1 = [pc[0][0], pc[1][1], pc[2][2]]
    pd2 = [pc[0][2], pc[1][1], pc[2][0]]
    su = sum(user[0]) + sum(user[1]) + sum(user[2])
    #sp = sum(pc[0]) + sum(pc[1]) + sum(pc[2])
    if su==1:
        #print(1)
        if places[1][1]==' ':
            places[1][1]='O'
            pc[1][1]=True
            print("I placed at 5th position")
        else:
            while True:
                t=random.randint(0,8)
                if t!=4:
                    break
            places[t//3][t%3]='O'
            pc[t//3][t%3]=True
            print("I placed at",t+1,"position")

    #Attack@2Win
    elif (sum(pr1)==2 and sum(r1)!=1) or (sum(pr2)==2 and sum(r2)!=1) or (sum(pr3)==2 and sum(r3)!=1):
        #print(2)
        if sum(pr1)==2 and sum(r1)!=1:
            plarow(0)
        elif sum(pr2)==2 and sum(r2)!=1:
            plarow(1)
        elif sum(pr3)==2 and sum(r3)!=1:
            plarow(2)
    elif (sum(pc1)==2 and sum(c1)!=1) or (sum(pc2)==2 and sum(c2)!=1) or (sum(pc3)==2 and sum(c3)!=1):
        #print(3)
        if sum(pc1)==2 and sum(c1)!=1:
            placol(0)
        elif sum(pc2)==2 and sum(c2)!=1:
            placol(1)
        elif sum(pc3)==2 and sum(c3)!=1:
            placol(2)
    elif (sum(pd1)==2 and sum(d1)!=1) or (sum(pd2)==2 and sum(d2)!=1):
       # print(4)
        if sum(pd1)==2 and sum(d1)!=1:
            for i in range(3):
                if (not user[i][i]) and (not pc[i][i]):
                    pc[i][i]=True
                    places[i][i]='O'
                    print("I placed at", (i * 3 + i)+1, "position")
                    break
        elif sum(pd2)==2 and sum(d2)!=1:
         #   print(5)
            if (not user[0][2]) and (not pc[0][2]):
                pc[0][2]=True
                places[0][2]='O'
                print("I placed at 3rd position")
            elif (not user[1][1]) and (not pc[1][1]):
                pc[1][1]=True
                places[1][1]='O'
                print("I placed at 5th position")
            elif (not pc[2][0]) and (not user[2][0]):
                pc[2][0]=True
                places[2][0]='O'
                print("I placed at 7th position")

    #Defence@2
    elif (sum(r1)==2 and sum(pr1)!=1) or (sum(r2)==2 and sum(pr2)!=1) or (sum(r3)==2 and sum(pr3)!=1):
       # print(6)
        if sum(r1)==2 and sum(pr1)!=1:
            plarow(0)
        elif sum(r2)==2 and sum(pr2)!=1:
            plarow(1)
        elif sum(r3)==2 and sum(pr3)!=1:
            plarow(2)
    elif (sum(c1)==2 and sum(pc1)!=1) or (sum(c2)==2 and sum(pc2)!=1) or (sum(c3)==2 and sum(pc3)!=1):
      #  print(7)
        if sum(c1)==2 and sum(pc1)!=1:
            placol(0)
        elif sum(c2)==2 and sum(pc2)!=1:
            placol(1)
        elif sum(c3)==2 and sum(pc3)!=1:
            placol(2)
    elif (sum(d1)==2 and sum(pd1)!=1) or (sum(d2)==2 and sum(pd2)!=1):
       # print(8)
        if sum(d1)==2 and sum(pd1)!=1:
            for i in range(3):
                if not user[i][i] and (not pc[i][i]):
                    pc[i][i]=True
                    places[i][i]='O'
                    print("I placed at", (i * 3)+1 + i, "position")
                    break
        elif sum(d2)==2 and sum(pd2)!=1:
        #    print(9)
            if (not user[0][2]) and (not pc[0][2]):
                pc[0][2]=True
                places[0][2]='O'
                print("I placed at 3rd position")
            elif (not user[1][1]) and (not pc[1][1]):
                pc[1][1]=True
                places[1][1]='O'
                print("I placed at 5th position")
            elif (not pc[2][0]) and (not user[2][0]):
                pc[2][0]=True
                places[2][0]='O'
                print("I placed at 8th position")

    else:
       # print(10)
        for i in range(3):
            p=True
            for j in range(3):
                if (not pc[i][j]) and (not user[i][j]):
                    pc[i][j]=True
                    places[i][j]='O'
                    p=False
                    print("I placed at", i * 3 + j+1, "position")
                    break
            if not p:
                break

def plarow(row):
    global places,user,pc
    for i in range(3):
        if (not user[row][i]) and (not pc[row][i]):
            pc[row][i]=True
            places[row][i]= 'O'
            print("I placed at",row*3+i+1,"position")
            break

def placol(col):
    global places,user,pc
    for i in range(3):
        if (not user[i][col]) and (not pc[i][col]):
            pc[i][col]=True
            places[i][col]='O'
            print("I placed at",i*3+col+1,"position")
            break

if __name__=='__main__':
    places=[[" "," "," "],[" "," "," "],[" "," "," "]]
    user=[[False,False,False],[False,False,False],[False,False,False]]
    pc=[[False,False,False],[False,False,False],[False,False,False]]
    last=-1
    print()
    print()
    print()
    print("\t\t\t\t\t\t\t\t\t\tHello welcome to TIC-TAC-TOE")
    print("\t\t\t\t\t\t\t\t\t\t   You(X) v/s Computer(O)")
    board()
    for i in range(9):
        player_turn()
        board()
        res, data = check_win()
        if res:
            announce(data)
            break
        system()
        board()
        res,data=check_win()
        if res:
            announce(data)
            break