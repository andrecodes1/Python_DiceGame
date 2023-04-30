from math import* #Importé les fonctions suivantes
import random
from tkinter import*
def script():
    global d1, d2, d3, d4 #Définir les variables globales suivantes
    global montant1, montant2
    montant1=120 #Donner à la variable suivante la valeur 120
    montant2=120#Donner à la variable suivante la valeur 120

    def restart ():#permet de recommencer le programme
        
        res=input("\n Voulez- vous recommencer le programme?: \n repondez par oui ou non : ")#donner la valeur oui ou non à la variable input
        rs=res.strip()
        rer=["oui","Oui","OUi","OUI","ouI","Yes","YEs","YES","Non","non","NON","NO","No","no"]#toutes les réponses possibles

        while rs not in rer:#tant que une réponse dans la liste ci-dessus n'est pas entrer, le programme demandera de recommencer
            print("Veuillez repondre par oui ou par non")
            res= input("Voulez-vous recommencer le programme?: \n").strip()
            rs=res.strip()

        if rs in rer: 
            rerl=["oui","Oui","OUi","OUI","ouI","Yes","YEs","YES"]
            if rs not in rerl:#si la réponse n'est pas dans la liste ci-dessus, le programme se termine
                print("merci de votre patience")
                exit()
            if rs in rer:#si la réponse se trouve dans la liste, le script recommence
                script()
    def reglejeux(): #Définir la fonction suivante
        print("Voici les règlements du jeux:\n 1- Vous commencez avec 120$, vous devez faire une mise supérieure à 0$ et vous ne pouvez dépasser votre bourse.\n 2- Le jeu s’arrête lorsque l’un des joueurs est à 0$ \n 4- L'orde de jeux est le suivant: Le premier joueur joue, et puis vient le second.")
        nom()

    def nom(): #Définir la fonction suivante
        global nom1su, nom2su#Définir les variables globales suivantes
        nom1=input("Veuillez écrire le nom du  joueur 1:") #Donner à la variable suivante la valeur inscrite par l'utilisateur
        nom2=input("Veuillez écrire le nom du joueur 2:")#Donner à la variable suivante la valeur inscrite par l'utilisateur
        nom1s = "".join(nom1.split()) #Gestion des majuscules...
        nom2s = "".join(nom2.split())
        nom1su = nom1s.capitalize()
        nom2su = nom2s.capitalize()
        while nom1su == nom2su : #Tant que les 2 noms sont identiques...
            print("Veuillez donner deux nom différent")#Afficher le texte suivant
            nom1=input("Veuillez écrire le nom du premier joueur:")#Donner à la variable suivante la valeur inscrite par l'utilisateur
            nom2=input("Veuillez écrire le nom du deuxieme joueur:")#Donner à la variable suivante la valeur inscrite par l'utilisateur
            nom1s = "".join(nom1.split())#Gestion des majuscules...
            nom2s = "".join(nom2.split())
            nom1su = nom1s.capitalize()
            nom2su = nom2s.capitalize()
        print ("Bonjour", nom1su, "et", nom2su)#Afficher le texte suivant
        mise()



    def mise():#Définir la fonction suivante
        import random #Importé random
        global montant1, montant2 #Définir les variables globales suivantes
        global nom1su, nom2su #Définir les variables globales suivantes
        global m1i,m2i #Définir les variables globales suivantes


        w1 = list(range(1, montant1+1))
        w1s = [str(int) for int in w1]

        mr2 = ("random", "aléatoire")#Donner à la variable suivante ces valeurs
        mr3 = ("allin", "tout")#Donner à la variable suivante ces valeurs
        mr4 = ("Minimum", "minimum")#Donner à la variable suivante ces valeurs
        i = 0#Donner à la variable suivante la valeur 0
    
        mise1=input("Quelle est votre mise joueur 1 (chiffre de votre choix, all in, random ou minimum): ").lower()#Donner à la variable suivante la valeur inscrite par l'utilisateur
        m1s = "".join(mise1.split())
        if m1s in w1s: #Liste de condition...
            i = i + 1 #Augmenter la valeur de i de 1 
        if m1s in mr2:
            i = i + 2#Augmenter la valeur de i de 2 
        if m1s in mr3:
            i = i + 3#Augmenter la valeur de i de 3 
        if m1s in mr4:
            i = i + 4#Augmenter la valeur de i de 4 
        while i == 0: #Tant que i est à 0
            print("Veuillez mettre un chiffre plus grand que 0 et plus petit que votre banque s.v.p")#Afficher le texte suivant
            mise1 = input("Quelle est votre mise joueur 1(chiffre de votre choix, all in, random ou minimum): ").lower()#Donner à la variable suivante la valeur inscrite par l'utilisateur
            m1s = "".join(mise1.split())
            if m1s in w1s: #Liste de condition...
                i = i + 1 #Augmenter la valeur de i de 1
            if m1s in mr2:
                i = i + 2 #Augmenter la valeur de i de 2
            if m1s in mr3:
                i = i + 3 #Augmenter la valeur de i de 3
            if m1s in mr4:
                i = i + 4 #Augmenter la valeur de i de 4
        while i ==1: #Tant que i est égal à 1
            m1i = int(m1s)#Donner à la variable suivante la valeur numérique de m1s
            print ("Votre mise est : ", m1i)#Afficher la mise
            break
        while i == 2: #Tant que i est égal à 2
            m1i = random.randint(1,montant1) #Donner à mli une valeur aléatoire
            print ("Votre mise aléatoire est : ", m1i) #Afficher le texte suivant
            break
        while i == 3:#Tant que i est égal à 3
            m1i = montant1 #Donner à m1i la valeur de montant1
            print ("votre mise 'all in' est : ", m1i)#Afficher le texte suivant
            break
        while i == 4:#Tant que i est égal à 4
            m1i = 1#Donner à m1i la valeur  1
            print ("Votre mise minimum est : ", m1i)#Afficher le texte suivant
            break
      
    


        w2 = list(range(1, montant2+1))
        w2s = [str(int) for int in w2]

        b = 0 #Donner à b la vleur 0
        m2=input("Quelle est votre mise joueur 2(chiffre de votre choix, all in, random ou minimum): ").lower()#Donner à la variable suivante la valeur inscrite par l'utilisateur
        m2s = "".join(m2.split())
        if m2s in w2s:#Liste de condition..
            b = b + 1#Augmenter la valeur de b de 1 
        if m2s in mr2:
            b = b + 2#Augmenter la valeur de b de 2
        if m2s in mr3:
            b = b + 3#Augmenter la valeur de b de 3
        if m2s in mr4:
            b = b + 4#Augmenter la valeur de b de 4
        while b == 0:#Tant que b est égal à 0
            print("Veuillez mettre un chiffre plus grand que 0 et plus petit que votre banque s.v.p") #Afficher le texte suivant
            m2 = input("Quelle est votre mise joueur 2(chiffre de votre choix, all in, random ou minimum): ").lower()#Donner à la variable suivante la valeur inscrite par l'utilisateur
            m2s = "".join(mise1.split())
            if m2s in w2s:#Liste de condition..
                b = b + 1#Augmenter la valeur de b de 1 
            if m2s in mr2:
                b = b + 2#Augmenter la valeur de b de 2
            if m2s in mr3:
                b = b + 3#Augmenter la valeur de b de 3
            if m2s in mr4:
                b = b + 4#Augmenter la valeur de b de 4
        while b ==  1:#Tant que b est égal à 1
            m2i = int(m2s)#Doner à m2i la valeur numérique de m2s
            print ("Votre mise est : ", m2i)
            break
        while b == 2:#Tant que b est égal à 2
            m2i = random.randint(1,montant2)#Donner à m2i une valeur aléatoire dans le range indiqué
            print ("Votre mise aléatoire est : ", m2i)#Afficher le texte suivant
            break
        while b == 3:#Tant que b est égal à 3
            m2i = montant2#Donner à m2i la valeur de montant2
            print ("Votre mise 'all in' est : ", m2i)#Afficher le texte suivant
            break
        while b == 4:#Tant que b est égal à 4
            m2i = 1#Donner à m2i la valeur 1
            print ("Votre mise minimum est : ", m2i)#Afficher le texte suivant
            break
        jeu()

    

    def bourse():#Définir la fonction suivante
    
        global montant1, montant2
        global m1i,m2i,sd1,sd2

    
        if sd1>sd2: #Si sd1 est plus grand que sd2...
            montant1=montant1+m2i#Aumgenter la valeur de montant1 de m2i
            montant2=montant2-m2i#Diminuer la valeur de montant2 de m2i

        elif sd2>sd1:#Si sd2 est plus grand que sd1...
            montant2=montant2+m1i#Aumgenter la valeur de montant2 de m1i
            montant1=montant1-m1i#Diminuer la valeur de montant2 de m1i

        elif sd1==sd2:#Si sd2 est égal à sd1...
            montant1=montant1#Les montants restent identiques...
            montant2=montant2

        while montant1>0 and montant2>0:#Tant que les 2 montants sont plus grands que 0
            print(nom1su,"il vous reste:",montant1,"\n ",nom2su,"il vous reste:",montant2)#Afficher le texte suivant
            mise()

        if montant1<=0 or montant2<=0:#Si un des 2 montants est plus petit que 0
            if montant1<=0:#Si montant1 est plus petit ou égal à 0
                print("La bourse de",nom1su,"est a 0, merci d'avoir jouer")#Afficher le texte suivant
                restart()#Le jeu se termine
            elif montant2<=0:#Si un des 2 montants est plus petit que 0
                print("La bourse de",nom2su,"est a 0, merci d'avoir jouer")#Afficher le texte suivant
                restart()#Le jeu se termine

    def resultat():#Définir la fonction suivante
        global sd1,sd2#Définir les variables global suivantes
        global nom1su, nom2su
        if sd1==sd2:#Si sd1 est égal à sd2
            print("Dommage! Les deux joueurs sont égaux!")#Afficher le texte suivant
        elif sd1<sd2:#Si sd1 est plus petit que sd2...
            print("Bravo",nom2su,"tu as remporté cette manche!!!")#Afficher le texte suivant
        elif sd1>sd2:#Si sd1 est plus grand que sd2...
            print("Bravo",nom1su,"tu as remporter cette manche!!!")#Afficher le texte suivant
    


        bourse()



                                        #debut tkinter
    import random
    def jeu():#Définir la fonction suivante
        global sd1,sd2
        froot=Tk()# une instance de la classe tk() pour créer un objet 
        froot.title('jeu de dés')# instance de type widget
        tex1 = Label(froot, text='Bonjour et bienvenu au jeu du rouleur de dés! \n (P.S. Nous ne sommes par responsable pour toute perte engendré suite au roulement de dés)', fg='red')# widget, zone pour le texte
        tex1.pack()# une méthode pour faire apparaître le widget précédent
        froot.geometry("500x500")

        #lancer dés
        def dice():#Définir la fonction suivante
            global sd1,sd2
            bt1['state'] = DISABLED
            d1=random.choice(my_dice)#Donner à d1 la valeur aléatoire du dé
            d2=random.choice(my_dice)#Donner à d2 la valeur aléatoire du dé
            diceL1.config(text=d1)
            diceL2.config(text=d2)

            sd1=nbr(d1)#Donner à sd1 la valeur de nbr(d1)
            sd2=nbr(d2)#Donner à sd1 la valeur de nbr(d2)
            sdiceL1.config(text=sd1)
            sdiceL2.config(text=sd2)

        def nbr(x):#Définir la fonction suivante
            global sd1,sd2
            if x=='\u2680':
                return(1)
            elif x=='\u2681':
                return(2)
            elif x=='\u2682':
                return(3)
            elif x=='\u2683':
                return(4)
            elif x=='\u2684':
                return(5)
            elif x=='\u2685':
                return(6)

        
        def regles():#Définir la fonction suivante
            print("Voici les règlements du jeux:\n 1- Vous commencez avec 120$, vous devez faire une mise supérieure à 0$ et vous ne pouvez dépasser votre bourse.\n 2- Le jeu s’arrête lorsque l’un des joueurs est à 0$ \n 4- L'orde de jeux est le suivant: Le premier joueur joue, et puis vient le second.")



        #dice button
        bt1=Button(froot,text="Lancer le dés", command=dice)
        bt1.pack(padx=5,pady=10)
        # button
        bt2=Button(froot,text="règles du jeu",command=regles)
        bt2.pack(padx=5,pady=10)
        #button quitter
        bt3=Button(froot,text="Quitter",command=froot.destroy)
        bt3.pack(padx=100,pady=10)
        #dice list
        my_dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        #frame
        frame=Frame(froot)
        frame.pack(pady=20)
        #dice labels
        diceL1=Label(frame,text='',font=("Times New Roman",100))
        diceL1.grid(row=0,padx=5)
        diceL2=Label(frame,text='',font=("Times New Roman",100))
        diceL2.grid(row=0,column=5,padx=5)

        sdiceL1=Label(frame,text='')
        sdiceL1.grid(row=1)
        sdiceL2=Label(frame,text='')
        sdiceL2.grid(row=1,column=5)

        froot.mainloop()

        resultat()
    reglejeux()
                                         #fin tkinter

    
script()
