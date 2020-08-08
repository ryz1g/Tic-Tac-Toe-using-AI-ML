import helping_functions as hf
import math

#loop to start the game, exited only when player doesn't want to continue
while True :
    hf.clear_board()
    turn="X"
    game=[[" "," "," "],[" "," "," "],[" "," "," "]]
    human="X"
    comp="O"
    while True :
        human=input("Welcome to Tic Tac Toe, Choose X or O to start:(X goes first)")
        if human=="X" or human=="O" :
            break
        else :
            print("Please give valid entry (X/O)")
    if human=="X" :
        comp="O"
    else :
        comp="X"
    #game starts here, each loop has one or two moves depending upon who startss
    while True :
        hf.clear_board()
        hf.print_board(game)
        c1,c2=(0,0)

        #if it is humans turn

        if turn==human :
            print("Enter coordiate of "+human+":")
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
            game=hf.make_move(c1,c2,game,turn)
            if human=="X" :
                turn="O"
            if human=="O" :
                turn="X"
        if hf.check_win(game)[0] :
            hf.clear_board()
            hf.print_board(game)
            print("Winner is:",hf.check_win(game)[1])
            break
        if hf.check_draw(game) is not True:
            hf.clear_board()
            hf.print_board(game)
            print("Game is drawn")
            break

        c1,c2=(0,0)
        pp=0

        #if it is computers turn
        if turn==comp :
            if comp=="X" :
                pp=hf.predict_move(game,1)
            else :
                pp=hf.predict_move(game,2)
            c1,c2=hf.convert_to_coord(pp)
            game=hf.make_move(c1,c2,game,comp)
            if comp=="X" :
                turn="O"
            if comp=="O" :
                turn="X"

        if hf.check_win(game)[0] :
            hf.clear_board()
            hf.print_board(game)
            print("Winner is:",hf.check_win(game)[1])
            break
        if hf.check_draw(game) is not True:
            hf.clear_board()
            hf.print_board(game)
            print("Game is drawn")
            break

    temp=input("Would you like to play again?(y/n)")
    if temp=="n" :
        print("Thanks for playing!Bye!")
        break
