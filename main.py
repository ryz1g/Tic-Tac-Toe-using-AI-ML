import helping_functions as hf

while True :
    hf.clear_board()
    turn=1
    game=[[" "," "," "],[" "," "," "],[" "," "," "]]
    p1="X"
    p2="O"
    while True :
        p1=input("Welcome to Tic Tac Toe, Choose X or O to start:")
        if p1=="X" or p1=="O" :
            break
        else :
            print("Please give valid entry (X/O)")
    if p1=="X" :
        p2="O"
    else :
        p2="X"
    while True :
        hf.clear_board()
        hf.print_board(game)
        if turn%2==0 :
            print("Enter coordiate player 2("+p2+"):")
        else :
            print("Enter coordiate player 1("+p1+"):")
        c1,c2=(0,0)
        while True :
            coord_str=input("Coordinates (eg:1,2):")
            try :
                c1=int(coord_str[0])
                c2=int(coord_str[2])
            except :
                print("Enter Valid Move")
                continue
            vl1=hf.valid_move(game,c1,c2)
            if vl1 :
                break
            print("Enter Valid Move")
        if turn%2==0 :
            game=hf.make_move(c1,c2,game,p2)
        else :
            game=hf.make_move(c1,c2,game,p1)
        if hf.check_draw(game) is not True:
            hf.clear_board()
            hf.print_board(game)
            print("Game is drawn")
            break
        if hf.check_win(game)[0] :
            hf.clear_board()
            hf.print_board(game)
            print("Winner is:",hf.check_win(game)[1])
            break
        turn=turn+1
    temp=input("Would you like to play again?(y/n)")
    if temp=="n" :
        print("Thanks for playing!Bye!")
        break
