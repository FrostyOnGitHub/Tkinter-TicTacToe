from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.geometry('415x515')
tk.title("Jeu de Tic-Tac-Toe")

#on met en place le Canvas

Canvas=Canvas(tk, bg="white", width=415, height=415)
Canvas.place(x=0,y=100)
line = Canvas.create_line(138,0,138,415)
line = Canvas.create_line(0,138,415,138)
line = Canvas.create_line(0,2*138,415,2*138)
line = Canvas.create_line(2*138,0,2*138,415)

#On crée les joueurs et on initialise les autres variables importantes

joueur1=StringVar()
joueur2=StringVar()
h=0
total_mouv=0
Champion = False


#On demande le nom des joueurs
j1_nom = Entry(tk, textvariable=joueur1, bd=4)
j1_nom.grid(row=1, column=1,)
j2_nom = Entry(tk, textvariable=joueur2, bd=4)
j2_nom.grid(row=2, column=1,)


    
#on crée le tableau de tableau auquel on assigne un 0 partout (pour l'ordinateur 0= case vide)
board=[]
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append(0)
        
#fonctions qui retournent le nom du champion dans la fonction gagnant()        
def croix_gagnante():
    gagnant1=joueur1.get() 
    gagnant2= joueur2.get()
    dico_gagnant = {"j1": gagnant1 + " Gagne!","j2": gagnant2 + " Gagne!"}
    mon_tuple=(dico_gagnant["j1"],dico_gagnant["j2"])
    return mon_tuple[0]


def cercle_gagnant():
    gagnant1=joueur1.get() 
    gagnant2= joueur2.get()
    dico_gagnant = {"j1": gagnant1 + " Gagne!","j2": gagnant2 + " Gagne!"}
    mon_tuple=(dico_gagnant["j1"],dico_gagnant["j2"])
    return mon_tuple[1]


#on dessine une croix    
def croix(i,j):
    line2 = Canvas.create_line(i*138,j*138,(i+1)*138,(j+1)*138,width=2,fill="purple",tag="croix")
    line3 = Canvas.create_line(i*138,j*138,(i)*138,(j+1)*138,(i+1)*138,j*138,width=2,fill="purple",tag="croix")

#on dessine un oval (cercle)
def cercle(i,j):
    circle = Canvas.create_oval(i*138,j*138,(i+1)*138,(j+1)*138,width=2,fill="orange",tag="cercle")
    
#le system qui determine si une croix va etre placée ou si c'est un cercle qui va etre placé
def afficher():
    for i in range(3):
        for j in range(3):
            if(board[j][i] == 1):
                croix(i,j)
            elif(board[j][i] == 2):
                cercle(i,j)
    Canvas.update()
                
#Fonction principale du code: verification de la case avec la position de la souris, compteur de mouvements pour une possible égalité, determination si la case est deja utilisée, ainsi qu'un system de determination si c'est X ou O qui joue prochainement.
#C'est aussi dans cette fonction que les fonctions afficher() et gagnant() entre en jeu.
    
#la commande "global" a la ligne 79 permet de rendre les variables h,total_mouv et champion que l'on a initialiser au debut globales, ce qui nous permet de travailler avec dans cette fonction.
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
                    
             
                    


#system de verification pour un gagnant(on fait deux test separes pour voir si c'est les croix qui sont consecutives (dans ce cas les cases sont = a 1), ou si c'est les cercles qui gagnent(dans ce cas les cases sont egales a 2).
#on verifie egalement si les cases testes sont differentes de 0 ( 0 = case vide)
                         
#on utilise break aux lignes 134 et 142 car pour verifier les diagonales, puisque je n'ai pas utilise i, le test s'effectue trois fois, donc le message s'affiche trois fois si il y a un gagnant en diagonale.
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
  
  
#fonction mise en place lorsque le boutton recommencer est appuyé: on efface tout du Canvas et on attribut la valeur 0 a toute les cases(0=case vide)  
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
   

#les differents Label et le Boutton, qui quand il est appuyé, effectue la fonction recommencer()     
joueurs = Label( tk, text=" Joueur1(X)", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
joueurs.grid(row=1, column=0)


joueurs = Label( tk, text=" Joueur2(O)", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
joueurs.grid(row=2, column=0)

button1 = Button(tk, text="recommencer", font='Times 10 bold', bg='black', fg='white', height=1, width=10, command=recommencer)
button1.grid(row=2, column=2)

Canvas.update()

tk.mainloop()


