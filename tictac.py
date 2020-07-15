lst=[[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(3):
    print(lst[i])
print("Positin matrix is as per keypad.....")
print("7 8 9 \n4 5 6\n1 2 3")
p1=input("Select player one's symbol....")
p2=input("Select player two's symbol....")
count=0
while(count<9):
    win=0
    if count%2==0:
        pos=int(input("Player one...."))
        if pos==7:
            if lst[0][0]==p1 or lst[0][0]==p2:
                print("Invalid Entry!!!\n Re-enter...")
                continue
            lst[0][0]=p1
            count+=1
        elif pos==8:
            if lst[0][1]==p1 or lst[0][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
            lst[0][1]=p1
            count+=1
        elif pos==9:
             if lst[0][2]==p1 or lst[0][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][2]=p1
             count+=1
        elif pos==4:
             if lst[1][0]==p1 or lst[1][0]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][0]=p1
             count+=1
        elif pos==5:
             if lst[1][1]==p1 or lst[1][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][1]=p1
             count+=1
        elif pos==6:
             if lst[1][2]==p1 or lst[1][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][2]=p1
             count+=1
        elif pos==1:
             if lst[2][0]==p1 or lst[2][0]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][0]=p1
             count+=1
        elif pos==2:
             if lst[2][1]==p1 or lst[2][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][1]=p1
             count+=1
        elif pos==3:
             if lst[2][2]==p1 or lst[2][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][2]=p1
             count+=1
        cp=0
        for i in range(3):  
          for j in range(3):
                if lst[i][j]==p1:
                    cp+=1
          if cp==3:
                print("Player 1 is Winner!!!!")
                win+=1
                break
          cp=0
        for i in range(3):
            for j in range(3):
                if lst[j][i]==p1:
                    cp+=1
            if cp==3:
                print("Player 1 is Winner!!!!!")
                win+=1
                break
            cp=0
        cp=0
        for i in range(3):
            if lst[i][i]==p1:
                cp+=1
        if cp==3:
            print("Player 1 is Winner!!!!!")
            win+=1
            break
        cp=0
        j=2
        for i in range(3):
           if lst[i][j]==p1:
               cp+=1
           j=j-1
        if cp==3:
            print("Player 1 is Winner!!!!")
            win+=1
        for i in range(3):
            print(lst[i])
    if win>0:
        break
    if count==9:
        print("Match Draw!!!!")
    else:
        pos=int(input("player two...."))
        if pos==7:
             if lst[0][0]==p1 or lst[0][0]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][0]=p2
             count+=1
        elif pos==8:
             if lst[0][1]==p1 or lst[0][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][1]=p2
             count+=1
        elif pos==9:
             if lst[0][2]==p1 or lst[0][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][2]=p2
             count+=1
        elif pos==4:
             if lst[1][0]==p1 or lst[1][0]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][0]=p2
             count+=1
        elif pos==5:
             if lst[1][1]==p1 or lst[1][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][1]=p2
             count+=1
        elif pos==6:
             if lst[1][2]==p1 or lst[1][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][2]=p2
             count+=1
        elif pos==1:
             if lst[2][0]==p1 or lst[2][0]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][0]=p2
             count+=1
        elif pos==2:
             if lst[2][1]==p1 or lst[2][1]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][1]=p2
             count+=1
        elif pos==3:
             if lst[2][2]==p1 or lst[2][2]==p2:
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][2]=p2
             count+=1
        cp=0
        for i in range(3):  
          for j in range(3):
                if lst[i][j]==p2:
                    cp+=1
          if cp==3:
                print("Player 2 is Winner!!!!")
                win+=1
                break
          cp=0
        for i in range(3):
            for j in range(3):
                if lst[j][i]==p2:
                    cp+=1
            if cp==3:
                print("Player 2 is Winner!!!!!")
                win+=1
                break
            cp=0
        cp=0
        for i in range(3):
            if lst[i][i]==p2:
                cp+=1
        if cp==3:
            print("Player 2 is Winner!!!!!")
            win+=1
            break
        cp=0
        j=2
        for i in range(3):
           if lst[i][j]==p2:
               cp+=1
           j=j-1
        if cp==3:
            print("Player 2 is Winner!!!!")
            win+=1
        for i in range(3):
            print(lst[i])
    if win>0:
        break
