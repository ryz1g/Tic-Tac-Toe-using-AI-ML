import helping_functions as hf

f1=open("Data.txt", "a")
f2=open("Labels.txt", "a")

while True :

    hf.clear_board()
    gg,cha=hf.random_board()
    hf.print_board(gg)
    print("Chance of",cha)

    st1=""
    for i in range(3) :
        for j in range(3) :
            tra=0
            if gg[i][j]==" " :
                tra=0
            if gg[i][j]=="X" :
                tra=1
            if gg[i][j]=="O" :
                tra=2
            st1=st1+str(tra)+","
    if cha=="X" :
        st1=st1+"1"
    else :
        st1=st1+"2"

    c1,c2=(0,0)
    while True :
        coord_str=input("What do you think human?\n")
        try :
            c1=int(coord_str[0])
            c2=int(coord_str[2])
        except :
            print("Enter Valid Move")
            continue
        vl1=hf.valid_move(gg,c1,c2)
        if vl1 :
            break
        print("Enter Valid Move")

    hf.make_move(c1,c2,gg,cha)
    hf.clear_board()
    hf.print_board(gg)
    y=input("Is this correct?(y/n)")
    temp=[[0,0,0],[0,0,0],[0,0,0]]
    if y=="y" :
        temp[c1-1][c2-1]=1
        print(temp)
    else :
        continue

    st=""
    for i in range(3) :
        for j in range(3) :
            st=st+str(temp[i][j])
            if i!=2 :
                st=st+","
            else :
                if j!=2 :
                    st=st+","

    f1.write(st1)
    f1.write("\n")
    f2.write(st)
    f2.write("\n")
