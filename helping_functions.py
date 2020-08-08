from os import system
import numpy as np
import math
from tensorflow.keras.models import model_from_json
import tensorflow as tf
from tensorflow import keras

#loading of pretrained model and weights starts
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
#loading ends

#function to replicate a list
def copi(l0) :
    tt=[[" "," "," "],[" "," "," "],[" "," "," "]]
    for i in range(3) :
        for j in range(3) :
            tt[i][j]=l0[i][j]
    return tt

#function to clear terminal
def clear_board() :
    _=system("clear")

#function to print the board properly
def print_board(l6) :
    for i in l6 :
        print(i[0],end=' ')
        print("|",end=' ')
        print(i[1],end=' ')
        print("|",end=' ')
        print(i[2])

#function to check whether move is valid
def valid_move(l7,p1,p2) :
    if p1>3 or p1<1 or p2>3 or p2<1 :
        return False
    if l7[p1-1][p2-1]!=' ' :
        return False
    return True

#function to change the game state by making a move
def make_move(p1,p2,li,player_mark) :
    li[p1-1][p2-1]=player_mark
    return li

#function to check whether a someone has won
def check_win(l3) :
    v1,v2,v3,v4,v5,v6,v7,v8,v9=(l3[0][0],l3[0][1],l3[0][2],l3[1][0],l3[1][1],l3[1][2],l3[2][0],l3[2][1],l3[2][2])
    if v1==v2 and v2==v3 and v1!=" ":
        return (True,v1)
    if v4==v5 and v5==v6 and v4!=" ":
        return (True,v4)
    if v7==v8 and v8==v9 and v7!=" ":
        return (True,v7)
    if v1==v4 and v4==v7 and v1!=" ":
        return (True,v1)
    if v2==v5 and v5==v8 and v2!=" ":
        return (True,v2)
    if v3==v6 and v6==v9 and v3!=" ":
        return (True,v3)
    if v1==v5 and v5==v9 and v1!=" ":
        return (True,v1)
    if v3==v5 and v5==v7 and v3!=" ":
        return (True,v3)
    return (False,None)

#function to check whether state is drawn
def check_draw(l4) :
    v1,v2,v3,v4,v5,v6,v7,v8,v9=(l4[0][0],l4[0][1],l4[0][2],l4[1][0],l4[1][1],l4[1][2],l4[2][0],l4[2][1],l4[2][2])
    if v1==" " or v2==" " or v3==" " or v4==" " or v5==" " or v6==" " or v7==" " or v8==" " or v9==" " :
        return True
    return False

#function to generate a random solvable state(used for collection of data)
#returns a board state which is not drawn, not won and is not already present in Data.txt(is unique)
def random_board() :
    turn=""
    while True :
        t=[]
        for i in range(9) :
            ran=math.ceil(3*np.random.rand())
            t.append(ran)
        lt=[["","",""],["","",""],["","",""]]
        c=0
        for i in range(3) :
            for j in range(3) :
                ch=""
                if t[c]==1 :
                    ch="X"
                if t[c]==2 :
                    ch="O"
                if t[c]==3 :
                    ch=" "
                lt[i][j]=ch
                c=c+1
        if check_win(lt)[0] : #checks whether a state generated is already a win
            continue
        if check_draw(lt) is not True : #checks whether a state generated is a draw
            continue
        c_o,c_x=(0,0)
        for i in range(3) :
            for j in range(3) :
                if lt[i][j]=="X" :
                    c_x=c_x+1
                elif lt[i][j]=="O" :
                    c_o=c_o+1
        if c_x>c_o+1 :
            continue
        if c_o>c_x+1 :
            continue
        if c_x>c_o :
            turn="O"
        elif c_o>c_x :
            turn="X"
        else :
            ran=math.ceil(2*np.random.rand())
            if ran==1 :
                turn="X"
            else :
                turn="O"
        f1=open("Data.txt")
        lt_str=""
        for i in t :
            if i==3 :
                lt_str=lt_str+"0"
                continue
            lt_str=lt_str+str(i)
        lt_str=lt_str+"\n"
        flag=0
        for line in f1 :
            if line==lt_str :
                flag=1
                break
        if flag==1 :
            continue
        break
    return (lt,turn)

#function to convert a number to coordinates
def convert_to_coord(num) :
    c1,c2=(0,0)
    if num==0 :
        c1,c2=(1,1)
    elif num==1 :
        c1,c2=(1,2)
    elif num==2 :
        c1,c2=(1,3)
    elif num==3 :
        c1,c2=(2,1)
    elif num==4 :
        c1,c2=(2,2)
    elif num==5 :
        c1,c2=(2,3)
    elif num==6 :
        c1,c2=(3,1)
    elif num==7 :
        c1,c2=(3,2)
    elif num==8 :
        c1,c2=(3,3)
    return (c1,c2)

#function to convert coordinates to number
def convert_to_num(c1,c2) :
    nu=0
    if c1==1 :
        if c2==1 :
            nu=0
        if c2==2 :
            nu=1
        if c2==3 :
            nu=2
    if c1==2 :
        if c2==1 :
            nu=3
        if c2==2 :
            nu=4
        if c2==3 :
            nu=5
    if c1==3 :
        if c2==1 :
            nu=6
        if c2==2 :
            nu=7
        if c2==3 :
            nu=8
    return nu

#function to predict best move
def predict_move(l1,pl) :
    ll=[]
    best_move=0
    for i in range(3) :
        for j in range(3) :
            if l1[i][j]==" " :
                ll.append(0)
            if l1[i][j]=="X" :
                ll.append(1)
            if l1[i][j]=="O" :
                ll.append(2)
    ll.append(pl)
    arr=loaded_model.predict(np.array([ll])) #prediction of best move
    result=np.where(arr==np.amax(arr))
    best_move=int(result[1][0])
    c1,c2=convert_to_coord(best_move)
    #if by chance model predicts an invalid move, random valid move is forced
    while valid_move(l1,c1,c2) is not True:
        ran=math.ceil(9*np.random.rand())
        c1,c2=convert_to_coord(ran)

    #Common Sense starts here
    poss_moves=[]   #list of coordiates of possible moves
    if pl==1 :
        mover_mark="X"    #mark of the one who's turn is there
        opp_mark="O"      #mark of opponent
    else :
        mover_mark="O"
        opp_mark="X"
    for i in range(3) :
        for j in range(3) :
            if l1[i][j]==" " :
                poss_moves.append((i+1,j+1))
    if len(poss_moves)==7 :
        if l1[1][1]==" " :
            return 4
    if l1[0][0]=="X" or l1[0][2]=="X" or l1[2][0]=="X" or l1[2][2]=="X" :
        if len(poss_moves)>6 :
            if l1[0][0]=="X" :
                return 8
            if l1[0][2]=="X" :
                return 6
            if l1[2][0]=="X" :
                return 2
            if l1[2][2]=="X" :
                return 0

    if len(poss_moves)>5 :
        rr=[]
        if l1[0][0]==" " :
            rr.append(0)
        if l1[2][0]==" " :
            rr.append(6)
        if l1[0][2]==" " :
            rr.append(2)
        if l1[2][2]==" " :
            rr.append(8)
        return (rr[math.floor(len(rr)*np.random.rand())])
    #loop to check whether a move exists by which opponent can win
    for co in poss_moves :
        gcopy=copi(l1)
        gcopy[co[0]-1][co[1]-1]=opp_mark
        if check_win(gcopy)[0] is True and check_win(gcopy)[1]==opp_mark :
            best_move=convert_to_num(co[0],co[1])
            break
    #loop to check whether a move exists by which player whose turn is there can win
    for co in poss_moves :
        gcopy=copi(l1)
        gcopy[co[0]-1][co[1]-1]=mover_mark
        if check_win(gcopy)[0] is True and check_win(gcopy)[1]==mover_mark :
            best_move=convert_to_num(co[0],co[1])
            break
    #Common Sense ends here

    return best_move
