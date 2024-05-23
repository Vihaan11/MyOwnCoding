def display(r1,r2,r3):
    print('''\n         0    1    2
         ↓    ↓    ↓''')
    print(f"r1-->  {r1}")
    print(f"r2-->  {r2}")
    print(f"r3-->  {r3}")

r1=[' ',' ',' ']
r2=[' ',' ',' ']
r3=[' ',' ',' ']

def usr_index():
    global rowno
    global colno
    
    rowno=""
    colno=""
    
    while rowno not in ['1','2','3']:
        rowno=input("Enter a row(1, 2 or 3): ")
        if rowno not in ['1','2','3']:
            print('Invalid input')
    rowno=int(rowno)
    
    while colno not in ['0','1','2']:
        colno=input("Enter a col(0, 1 or 2): ")
        if colno not in ['0','1','2']:
            print('Invalid input')
    colno=int(colno)

def usr_replace(rowno,colno):
    player=""    
    while player not in ["O","X"]:
        player=input("O or X : ")
        if player not in ["O","X"]:
            print('Invalid input')
    if rowno==1 and r1[colno]==' ':
        r1[colno]=player
    elif rowno==2 and r2[colno]==' ':
        r2[colno]=player
    elif rowno==3 and r3[colno]==' ':
        r3[colno]=player
    else:
        print("Invalid Input")


def checkwin():

    xcond1=bool(r1[0]=='X' and r2[1]=='X' and r3[2]=='X') # Conditions for X to win
    xcond2=bool(r1[2]=='X' and r2[1]=='X' and r3[0]=='X') # Conditions for X to win
    xcond3=bool(r1[0]=='X' and r2[0]=='X' and r3[0]=='X') # Conditions for X to win
    xcond4=bool(r1[1]=='X' and r2[1]=='X' and r3[1]=='X') # Conditions for X to win
    xcond5=bool(r1[2]=='X' and r2[2]=='X' and r3[2]=='X') # Conditions for X to win
    xcond6=bool(r1==['X','X','X']) # Conditions for X to win
    xcond7=bool(r2==['X','X','X']) # Conditions for X to win
    xcond8=bool(r3==['X','X','X']) # Conditions for X to win

    ocond1=bool(r1[0]=='O' and r2[1]=='O' and r3[2]=='O') # Conditions for O to win
    ocond2=bool(r1[2]=='O' and r2[1]=='O' and r3[0]=='O') # Conditions for O to win
    ocond3=bool(r1[0]=='O' and r2[0]=='O' and r3[0]=='O') # Conditions for O to win
    ocond4=bool(r1[2]=='O' and r2[1]=='O' and r3[0]=='O') # Conditions for O to win
    ocond5=bool(r1[2]=='O' and r2[2]=='O' and r3[2]=='O') # Conditions for O to win
    ocond6=bool(r1==['O','O','O']) # Conditions for O to win
    ocond7=bool(r2==['O','O','O']) # Conditions for O to win
    ocond8=bool(r3==['O','O','O']) # Conditions for O to win

    if xcond1 or xcond2 or xcond3 or xcond4 or xcond5 or xcond6 or xcond7 or xcond8:
        display(r1, r2, r3)
        print("\nX wins!!!")
        exit()
    elif ocond1 or ocond2 or ocond3 or ocond4 or ocond5 or ocond6 or ocond7 or ocond8:
        display(r1, r2, r3)
        print("\nO wins!!!")
        exit()

while True:
    display(r1, r2, r3)
    usr_index()
    usr_replace(rowno, colno)
    checkwin()
