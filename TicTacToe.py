from tkinter import *
import tkinter.messagebox
#Set up the window
tk=Tk()
tk.geometry('415x515')
tk.title("Jeu de Tic-Tac-Toe")

#Create the Canvas area for the game

Canvas=Canvas(tk, bg="white", width=415, height=415)
Canvas.place(x=0,y=100)
line = Canvas.create_line(138,0,138,415)
line = Canvas.create_line(0,138,415,138)
line = Canvas.create_line(0,2*138,415,2*138)
line = Canvas.create_line(2*138,0,2*138,415)

#Create the players and initialize the other variables

joueur1=StringVar()
joueur2=StringVar()
h=0
total_mouv=0
Champion = False


#Asking for the name fo the players
j1_nom = Entry(tk, textvariable=joueur1, bd=4)
j1_nom.grid(row=1, column=1,)
j2_nom = Entry(tk, textvariable=joueur2, bd=4)
j2_nom.grid(row=2, column=1,)


    
#We create a table and append 0 to all of the squares( for the machine 0 is = to an empty square)
board=[]
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append(0)
        
#I have made use of dictionnaries and tuples here since I wanted to challenge myself to find a way to make it work(i know it is not the best way to create this system)
#these two functions control the name being returned when either a cross or a circle win.
def croix_gagnante():
    gagnant1=joueur1.get() 
    gagnant2= joueur2.get()
    dico_gagnant = {"j1": gagnant1 + " Wins!","j2": gagnant2 + " Wins!"}
    mon_tuple=(dico_gagnant["j1"],dico_gagnant["j2"])
    return mon_tuple[0]


def cercle_gagnant():
    gagnant1=joueur1.get() 
    gagnant2= joueur2.get()
    dico_gagnant = {"j1": gagnant1 + " Wins!","j2": gagnant2 + " Wins!"}
    mon_tuple=(dico_gagnant["j1"],dico_gagnant["j2"])
    return mon_tuple[1]


#This function draws two lines in the designated square on the Canvas.
def croix(i,j):
    line2 = Canvas.create_line(i*138,j*138,(i+1)*138,(j+1)*138,width=2,fill="purple",tag="croix")
    line3 = Canvas.create_line(i*138,j*138,(i)*138,(j+1)*138,(i+1)*138,j*138,width=2,fill="purple",tag="croix")

#This function draws an oval, although our dimensions allow it to resemble a circle.
def cercle(i,j):
    circle = Canvas.create_oval(i*138,j*138,(i+1)*138,(j+1)*138,width=2,fill="orange",tag="cercle")
    
#This functions checks if the square on the Canvas has the value 1, if it does it executes the croix() function, and if it has the value 2, it executes the cercle() function.
def afficher():
    for i in range(3):
        for j in range(3):
            if(board[j][i] == 1):
                croix(i,j)
            elif(board[j][i] == 2):
                cercle(i,j)
    Canvas.update()
                
#This is the main function of the code: It checks which square of the Canvas the mouse pointer clicked in, counts how many moves were executed and checks for a tie, determines if the square of the Canvas was already clicked. It also features a system that checks if it is X or O that plays next.
#If you aren't familiar to the global method, it simply allows you to use externally created variables in the function.
def main(event):
    global h,total_mouv,Champion
    mx = event.x
    my = event.y
    for i in range(3):
        for j in range(3):
            
                if i*138 < mx and mx <(i+1)*138 and j*138 <my  and my< (j+1)*138:
                    
                    total_mouv+=1
                    if board[j][i] == 0:
                        h+=1

                        if h%2==0:
                            board[j][i] = 2
                        else:
                            board[j][i] = 1

                        afficher()
                        gagnant()

                    
                        if total_mouv == 9 and Champion == False:
                            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Match Nul!")
                        
                    

                        
                    
                        
                    else:
                         tkinter.messagebox.showinfo("Tic-Tac-Toe", "Case deja utilisée!")
                         total_mouv-=1
                    
             
                    

#verification system that checks for a winner( we do two seperate tests to see if it is the crosses or the circles that are consecutive). We also check if the cells are different from 0(Here again, for the machine, 0 counts as empty, and 3 consecutive empty cells would be considered winning without the test)                        
def gagnant():
    global Champion
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] !=0 and board[i][0] == 1 or
            board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] !=0 and board[0][i] == 1 or
            board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] !=0 and board[0][0] == 1 or
            board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] !=0 and board[2][0] == 1):
            Champion=True
            tkinter.messagebox.showinfo("Tic-Tac-Toe", croix_gagnante())
            break
                
        elif(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] !=0 and board[i][0] == 2 or
            board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] !=0 and board[0][i] == 2 or
            board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] !=0 and board[0][0] == 2 or
            board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] !=0 and board[2][0] == 2 ):
            Champion=True
            tkinter.messagebox.showinfo("Tic-Tac-Toe", cercle_gagnant())
            break
                


Canvas.bind("<Button 1>",main)
  
  
#simple function that is executed when you press the restart button (the buttons is labeled as "recommencer", since I initially wrote this code in french)
def recommencer():
    global h,total_mouv,Champion
    
    h=0
    Champion=False
    total_mouv=0
    Canvas.delete("croix")
    Canvas.delete("cercle")
    for i in range(3):
        for j in range(3):
            board[j][i] = 0
   

#Here we set up the labels for the player names.   
joueurs = Label( tk, text=" Joueur1(X)", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
joueurs.grid(row=1, column=0)


joueurs = Label( tk, text=" Joueur2(O)", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
joueurs.grid(row=2, column=0)


#The button for the restart (recommencer()) function
button1 = Button(tk, text="recommencer", font='Times 10 bold', bg='black', fg='white', height=1, width=10, command=recommencer)
button1.grid(row=2, column=2)


#If you work with a Canvas, never forget to Canvas.update() :)
Canvas.update()

tk.mainloop()

#You can ask me anything about this code on discord : FrostyCitrus#3699

