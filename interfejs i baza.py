import Losowanie
from tkinter import messagebox
from tkinter import *
from math import *
import pylab 
import tkinter as tk



class Proba(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.Przelacznik(Menu)

    def Przelacznik(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Modelowanie interakcji małżeńskich",font=('Helvetica', 19)).pack(side="top")
        tk.Button(self, text="Pierwsza kategoria",
                  command=lambda: master.Przelacznik(KategoriaPierwsza)).pack()

    

class KategoriaPierwsza(tk.Frame):
    WynikZK1=0
    WynikMK1=0
    def __init__(self, master,*args, **kwargs):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Kategoria pierwsza - Rodzina",font=('Helvetica', 19)).pack(side="top")

        pytanie1kat1 = Losowanie.rodzina1
        pytanie2kat1 = Losowanie.rodzina2
        pytanie3kat1 = Losowanie.rodzina3
        pytanie4kat1 = Losowanie.rodzina4
        pytanie5kat1 = Losowanie.rodzina5

        pyt1=Label(self, text=pytanie1kat1)
        label_1 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_2 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt2=Label(self, text=pytanie2kat1)
        label_3 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_4 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt3=Label(self, text=pytanie3kat1)
        label_5 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_6 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt4=Label(self, text=pytanie4kat1)
        label_7 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_8 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt5=Label(self, text=pytanie5kat1)
        label_9=Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_10=Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        
        KategoriaPierwsza.odp1Z = Entry(self)
        KategoriaPierwsza.odp1M = Entry(self)
        KategoriaPierwsza.odp2Z = Entry(self)
        KategoriaPierwsza.odp2M = Entry(self)
        KategoriaPierwsza.odp3Z = Entry(self)
        KategoriaPierwsza.odp3M = Entry(self)
        KategoriaPierwsza.odp4Z = Entry(self)
        KategoriaPierwsza.odp4M = Entry(self)
        KategoriaPierwsza.odp5Z = Entry(self)
        KategoriaPierwsza.odp5M = Entry(self)

        pyt1.pack(side="top")
        label_1.pack()
        KategoriaPierwsza.odp1Z.pack()
        label_2.pack()
        KategoriaPierwsza.odp1M.pack()
        pyt2.pack(side="top")
        label_3.pack()
        KategoriaPierwsza.odp2Z.pack()
        label_4.pack()
        KategoriaPierwsza.odp2M.pack()
        pyt3.pack(side="top")
        label_5.pack()
        KategoriaPierwsza.odp3Z.pack()
        label_6.pack()
        KategoriaPierwsza.odp3M.pack()
        pyt4.pack(side="top")           
        label_7.pack()
        KategoriaPierwsza.odp4Z.pack()
        label_8.pack()
        KategoriaPierwsza.odp4M.pack()
        pyt5.pack(side="top")
        label_9.pack()
        KategoriaPierwsza.odp5Z.pack()
        label_10.pack()
        KategoriaPierwsza.odp5M.pack()
        

        def calculateZ(event):
            #global KategoriaPierwsza.WynikZK1
            
            KategoriaPierwsza.WynikZK1=int(KategoriaPierwsza.odp1Z.get()) + int(KategoriaPierwsza.odp2Z.get()) + int(KategoriaPierwsza.odp3Z.get()) + int(KategoriaPierwsza.odp4Z.get()) + int(KategoriaPierwsza.odp5Z.get())
            print(KategoriaPierwsza.WynikZK1)
            #messagebox.showinfo("Wynik męża", KategoriaPierwsza.WynikZK1)
            #return KategoriaPierwsza.WynikZK1

    
            KategoriaPierwsza.WynikMK1=int(KategoriaPierwsza.odp1M.get()) + int(KategoriaPierwsza.odp2M.get()) + int(KategoriaPierwsza.odp3M.get()) + int(KategoriaPierwsza.odp4M.get()) + int(KategoriaPierwsza.odp5M.get())
            print(KategoriaPierwsza.WynikMK1)
            #messagebox.showinfo("Wynik męża", KategoriaPierwsza.WynikMK1)
            #return KategoriaPierwsza.WynikMK1



        button_1 = Button(self, text="Zatwierdź wyniki")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)

##        button_1 = Button(self, text="Wynik męża")
##        button_1.bind("<Button-1>",calculateM)
##        button_1.pack(side="right")

        tk.Button(self, text="Następna kategoria",
                 command=lambda: master.Przelacznik(KategoriaDruga)).pack()

     
        
class KategoriaDruga(tk.Frame):
    def __init__(self, master,*args, **kwargs):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Kategoria druga - Czas wolny", font=('Helvetica', 19)).pack(side="top")


        pytanie1kat2 = Losowanie.czas1
        pytanie2kat2 = Losowanie.czas2
        pytanie3kat2 = Losowanie.czas3
        pytanie4kat2 = Losowanie.czas4
        pytanie5kat2 = Losowanie.czas5

        pyt1=Label(self, text=pytanie1kat2)
        label_1 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_2 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt2=Label(self, text=pytanie2kat2)
        label_3 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_4 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt3=Label(self, text=pytanie3kat2)
        label_5 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_6 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt4=Label(self, text=pytanie4kat2)
        label_7 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_8 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt5=Label(self, text=pytanie5kat2)
        label_9=Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_10=Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")


        KategoriaDruga.odp1Z = Entry(self)
        KategoriaDruga.odp1M = Entry(self)
        KategoriaDruga.odp2Z = Entry(self)
        KategoriaDruga.odp2M = Entry(self)
        KategoriaDruga.odp3Z = Entry(self)
        KategoriaDruga.odp3M = Entry(self)
        KategoriaDruga.odp4Z = Entry(self)
        KategoriaDruga.odp4M = Entry(self)
        KategoriaDruga.odp5Z = Entry(self)
        KategoriaDruga.odp5M = Entry(self)


        pyt1.pack(side="top")
        label_1.pack()
        KategoriaDruga.odp1Z.pack()
        label_2.pack()
        KategoriaDruga.odp1M.pack()
        pyt2.pack(side="top")
        label_3.pack()
        KategoriaDruga.odp2Z.pack()
        label_4.pack()
        KategoriaDruga.odp2M.pack()
        pyt3.pack(side="top")
        label_5.pack()
        KategoriaDruga.odp3Z.pack()
        label_6.pack()
        KategoriaDruga.odp3M.pack()
        pyt4.pack(side="top")           
        label_7.pack()
        KategoriaDruga.odp4Z.pack()
        label_8.pack()
        KategoriaDruga.odp4M.pack()
        pyt5.pack(side="top")
        label_9.pack()
        KategoriaDruga.odp5Z.pack()
        label_10.pack()
        KategoriaDruga.odp5M.pack()

  

        def calculateZ(event):
            KategoriaDruga.WynikZK2=int(KategoriaDruga.odp1Z.get()) + int(KategoriaDruga.odp2Z.get()) + int(KategoriaDruga.odp3Z.get()) + int(KategoriaDruga.odp4Z.get()) + int(KategoriaDruga.odp5Z.get())
            #print(KategoriaDruga.WynikZK2)
            #messagebox.showinfo("Wynik żony", KategoriaDruga.WynikZK2)
            
            KategoriaDruga.WynikMK2=int(KategoriaDruga.odp1M.get()) + int(KategoriaDruga.odp2M.get()) + int(KategoriaDruga.odp3M.get()) + int(KategoriaDruga.odp4M.get()) + int(KategoriaDruga.odp5M.get())
            #print(KategoriaDruga.WynikMK2)
            #messagebox.showinfo("Wynik męża", KategoriaDruga.WynikMK2)
            #return KategoriaDruga.WynikMK2

        button_1 = Button(self, text="Zatwierdź wyniki")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)

##        button_1 = Button(self, text="Wynik męża")
##        button_1.bind("<Button-1>", calculateM)
##        button_1.pack(side="right")

     
        tk.Button(self, text="Następna kategoria",
                  command=lambda: master.Przelacznik(KategoriaTrzecia)).pack()

class KategoriaTrzecia(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Kategoria trzecia - Pieniądze", font=('Helvetica', 19)).pack(side="top")

        pytanie1kat3 = Losowanie.pieniadze1
        pytanie2kat3 = Losowanie.pieniadze2
        pytanie3kat3 = Losowanie.pieniadze3
        pytanie4kat3 = Losowanie.pieniadze4
        pytanie5kat3 = Losowanie.pieniadze5

        pyt1=Label(self, text=pytanie1kat3)
        label_1 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_2 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt2=Label(self, text=pytanie2kat3)
        label_3 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_4 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt3=Label(self, text=pytanie3kat3)
        label_5 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_6 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt4=Label(self, text=pytanie4kat3)
        label_7 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_8 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt5=Label(self, text=pytanie5kat3)
        label_9=Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_10=Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")


        KategoriaTrzecia.odp1Z = Entry(self)
        KategoriaTrzecia.odp1M = Entry(self)
        KategoriaTrzecia.odp2Z = Entry(self)
        KategoriaTrzecia.odp2M = Entry(self)
        KategoriaTrzecia.odp3Z = Entry(self)
        KategoriaTrzecia.odp3M = Entry(self)
        KategoriaTrzecia.odp4Z = Entry(self)
        KategoriaTrzecia.odp4M = Entry(self)
        KategoriaTrzecia.odp5Z = Entry(self)
        KategoriaTrzecia.odp5M = Entry(self)

        pyt1.pack(side="top")
        label_1.pack()
        KategoriaTrzecia.odp1Z.pack()
        label_2.pack()
        KategoriaTrzecia.odp1M.pack()
        pyt2.pack(side="top")
        label_3.pack()
        KategoriaTrzecia.odp2Z.pack()
        label_4.pack()
        KategoriaTrzecia.odp2M.pack()
        pyt3.pack(side="top")
        label_5.pack()
        KategoriaTrzecia.odp3Z.pack()
        label_6.pack()
        KategoriaTrzecia.odp3M.pack()
        pyt4.pack(side="top")           
        label_7.pack()
        KategoriaTrzecia.odp4Z.pack()
        label_8.pack()
        KategoriaTrzecia.odp4M.pack()
        pyt5.pack(side="top")
        label_9.pack()
        KategoriaTrzecia.odp5Z.pack()
        label_10.pack()
        KategoriaTrzecia.odp5M.pack()

  

        def calculateZ(event):
            KategoriaTrzecia.WynikZK3=int(KategoriaTrzecia.odp1Z.get()) + int(KategoriaTrzecia.odp2Z.get()) + int(KategoriaTrzecia.odp3Z.get()) + int(KategoriaTrzecia.odp4Z.get()) + int(KategoriaTrzecia.odp5Z.get())
            #print(KategoriaTrzecia.WynikZK3)
            #messagebox.showinfo("Wynik żony", KategoriaTrzecia.WynikZK3)
            #return KategoriaTrzecia.WynikZK3
    
            KategoriaTrzecia.WynikMK3=int(KategoriaTrzecia.odp1M.get()) + int(KategoriaTrzecia.odp2M.get()) + int(KategoriaTrzecia.odp3M.get()) + int(KategoriaTrzecia.odp4M.get()) + int(KategoriaTrzecia.odp5M.get())
            #print(KategoriaTrzecia.WynikMK3)
            #messagebox.showinfo("Wynik męża", KategoriaTrzecia.WynikMK3)
            #return KategoriaTrzecia.WynikMK3

        button_1 = Button(self, text="Zatwierdź wyniki")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)

##        button_1 = Button(self, text="Wynik męża")
##        button_1.bind("<Button-1>", calculateM)
##        button_1.pack(side="right")


        tk.Button(self, text="Następna kategoria",
                  command=lambda: master.Przelacznik(KategoriaCzwarta)).pack()

class KategoriaCzwarta(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Kategoria druga - Obowiązki", font=('Helvetica', 19)).pack(side="top")

        pytanie1kat4 = Losowanie.obowiazki1
        pytanie2kat4 = Losowanie.obowiazki2
        pytanie3kat4 = Losowanie.obowiazki3
        pytanie4kat4 = Losowanie.obowiazki4
        pytanie5kat4 = Losowanie.obowiazki5

        pyt1=Label(self, text=pytanie1kat4)
        label_1 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_2 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt2=Label(self, text=pytanie2kat4)
        label_3 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_4 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt3=Label(self, text=pytanie3kat4)
        label_5 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_6 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt4=Label(self, text=pytanie4kat4)
        label_7 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_8 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt5=Label(self, text=pytanie5kat4)
        label_9=Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_10=Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        KategoriaCzwarta.odp1Z = Entry(self)
        KategoriaCzwarta.odp1M = Entry(self)
        KategoriaCzwarta.odp2Z = Entry(self)
        KategoriaCzwarta.odp2M = Entry(self)
        KategoriaCzwarta.odp3Z = Entry(self)
        KategoriaCzwarta.odp3M = Entry(self)
        KategoriaCzwarta.odp4Z = Entry(self)
        KategoriaCzwarta.odp4M = Entry(self)
        KategoriaCzwarta.odp5Z = Entry(self)
        KategoriaCzwarta.odp5M = Entry(self)

        pyt1.pack(side="top")
        label_1.pack()
        KategoriaCzwarta.odp1Z.pack()
        label_2.pack()
        KategoriaCzwarta.odp1M.pack()
        pyt2.pack(side="top")
        label_3.pack()
        KategoriaCzwarta.odp2Z.pack()
        label_4.pack()
        KategoriaCzwarta.odp2M.pack()
        pyt3.pack(side="top")
        label_5.pack()
        KategoriaCzwarta.odp3Z.pack()
        label_6.pack()
        KategoriaCzwarta.odp3M.pack()
        pyt4.pack(side="top")           
        label_7.pack()
        KategoriaCzwarta.odp4Z.pack()
        label_8.pack()
        KategoriaCzwarta.odp4M.pack()
        pyt5.pack(side="top")
        label_9.pack()
        KategoriaCzwarta.odp5Z.pack()
        label_10.pack()
        KategoriaCzwarta.odp5M.pack()

  

        def calculateZ(event):
            KategoriaCzwarta.WynikZK4=int(KategoriaCzwarta.odp1Z.get()) + int(KategoriaCzwarta.odp2Z.get()) + int(KategoriaCzwarta.odp3Z.get()) + int(KategoriaCzwarta.odp4Z.get()) + int(KategoriaCzwarta.odp5Z.get())
            #print(KategoriaCzwarta.WynikZK4)
            #messagebox.showinfo("Wynik żony", KategoriaCzwarta.WynikZK4)
    
            KategoriaCzwarta.WynikMK4=int(KategoriaCzwarta.odp1M.get()) + int(KategoriaCzwarta.odp2M.get()) + int(KategoriaCzwarta.odp3M.get()) + int(KategoriaCzwarta.odp4M.get()) + int(KategoriaCzwarta.odp5M.get())
            #print(KategoriaCzwarta.WynikMK4)
            #messagebox.showinfo("Wynik męża", KategoriaCzwarta.WynikMK4)

        button_1 = Button(self, text="Zatwierdź wyniki")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)
##
##        button_1 = Button(self, text="Wynik męża")
##        button_1.bind("<Button-1>", calculateM)
##        button_1.pack(side="right")
##    

        tk.Button(self, text="Następna kategoria",
                  command=lambda: master.Przelacznik(KategoriaPiata)).pack()


class KategoriaPiata(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Kategoria piąta - Bliskość", font=('Helvetica', 19)).pack(side="top")

        pytanie1kat5 = Losowanie.bliskosc1
        pytanie2kat5 = Losowanie.bliskosc2
        pytanie3kat5 = Losowanie.bliskosc3
        pytanie4kat5 = Losowanie.bliskosc4
        pytanie5kat5 = Losowanie.bliskosc5

        pyt1=Label(self, text=pytanie1kat5)
        label_1 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_2 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt2=Label(self, text=pytanie2kat5)
        label_3 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_4 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt3=Label(self, text=pytanie3kat5)
        label_5 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_6 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt4=Label(self, text=pytanie4kat5)
        label_7 = Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_8 = Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")

        pyt5=Label(self, text=pytanie5kat5)
        label_9=Label(self, text="Punkt przydzielony za odpowiedź żony (1, 0 lub -1): ")
        label_10=Label(self, text="Punkt przydzielony za odpowiedź męża (1, 0 lub -1): ")


        KategoriaPiata.odp1Z = Entry(self)
        KategoriaPiata.odp1M = Entry(self)
        KategoriaPiata.odp2Z = Entry(self)
        KategoriaPiata.odp2M = Entry(self)
        KategoriaPiata.odp3Z = Entry(self)
        KategoriaPiata.odp3M = Entry(self)
        KategoriaPiata.odp4Z = Entry(self)
        KategoriaPiata.odp4M = Entry(self)
        KategoriaPiata.odp5Z = Entry(self)
        KategoriaPiata.odp5M = Entry(self)

        pyt1.pack(side="top")
        label_1.pack()
        KategoriaPiata.odp1Z.pack()
        label_2.pack()
        KategoriaPiata.odp1M.pack()
        pyt2.pack(side="top")
        label_3.pack()
        KategoriaPiata.odp2Z.pack()
        label_4.pack()
        KategoriaPiata.odp2M.pack()
        pyt3.pack(side="top")
        label_5.pack()
        KategoriaPiata.odp3Z.pack()
        label_6.pack()
        KategoriaPiata.odp3M.pack()
        pyt4.pack(side="top")           
        label_7.pack()
        KategoriaPiata.odp4Z.pack()
        label_8.pack()
        KategoriaPiata.odp4M.pack()
        pyt5.pack(side="top")
        label_9.pack()
        KategoriaPiata.odp5Z.pack()
        label_10.pack()
        KategoriaPiata.odp5M.pack()

  

        def calculateZ(event):
            KategoriaPiata.WynikZK5=int(KategoriaPiata.odp1Z.get()) + int(KategoriaPiata.odp2Z.get()) + int(KategoriaPiata.odp3Z.get()) + int(KategoriaPiata.odp4Z.get()) + int(KategoriaPiata.odp5Z.get())
            #print(KategoriaPiata.WynikZK5)
            #messagebox.showinfo("Wynik żony", KategoriaPiata.WynikZK5)
    
            KategoriaPiata.WynikMK5=int(KategoriaPiata.odp1M.get()) + int(KategoriaPiata.odp2M.get()) + int(KategoriaPiata.odp3M.get()) + int(KategoriaPiata.odp4M.get()) + int(KategoriaPiata.odp5M.get())
            #print(KategoriaPiata.WynikMK5)
            #messagebox.showinfo("Wynik męża", KategoriaPiata.WynikMK5)
            

        def close_window(self): 
            root.destroy()    


        button_1 = Button(self, text="Zatwierdź wyniki")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)

##        button_1 = Button(self, text="Wynik męża")
##        button_1.bind("<Button-1>", calculateM)
##        button_1.pack(side="right")

        
        tk.Button(self, text="Wyniki",
                  command=lambda: master.Przelacznik(Wyniki)).pack()

        button_1 = Button(self, text="Wyjście")
        button_1.bind("<Button-1>", close_window)
        button_1.pack(side="top")

      


class Wyniki(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Wyniki", font=('Helvetica', 19)).pack(side="top")

        def calculateZ(event):
            #cA=KategoriaPierwsza(master)
            #p=cA.calculateZ()
            
            #print(WynikZK1)
            KategoriaPierwsza.WynikZK1
            KategoriaDruga.WynikZK2
            KategoriaTrzecia.WynikZK3
            KategoriaCzwarta.WynikZK4
            KategoriaPiata.WynikZK5
            WynikCalZ=KategoriaPierwsza.WynikZK1+KategoriaDruga.WynikZK2 + KategoriaTrzecia.WynikZK3+KategoriaCzwarta.WynikZK4+KategoriaPiata.WynikZK5
            messagebox.showinfo("Wynik żony", WynikCalZ)

        
        def calculateM(event):
            KategoriaPierwsza.WynikMK1
            KategoriaDruga.WynikMK2
            KategoriaTrzecia.WynikMK3
            KategoriaCzwarta.WynikMK4
            KategoriaPiata.WynikMK5
            WynikCalM=KategoriaPierwsza.WynikMK1 + KategoriaDruga.WynikMK2+KategoriaTrzecia.WynikMK3+KategoriaCzwarta.WynikMK4+KategoriaPiata.WynikMK5
            messagebox.showinfo("Wynik męża", WynikCalM)

        def close_window(self): 
            root.destroy()

        def wykres(event):
            Zsum1 = KategoriaPierwsza.WynikZK1
            Zsum2 = KategoriaDruga.WynikZK2
            Zsum3 = KategoriaTrzecia.WynikZK3
            Zsum4 = KategoriaCzwarta.WynikZK4
            Zsum5 = KategoriaPiata.WynikZK5

            Msum1 = KategoriaPierwsza.WynikMK1
            Msum2 = KategoriaDruga.WynikMK2
            Msum3 = KategoriaTrzecia.WynikMK3
            Msum4 = KategoriaCzwarta.WynikMK4
            Msum5 = KategoriaPiata.WynikMK5              

            # dane żona
            y1 = [Zsum1, Zsum2, Zsum3, Zsum4, Zsum5]
            x1 = [1, 2, 3, 4, 5]

            # dane mąż
            y2 = [Msum1, Msum2, Msum3, Msum4, Msum5]
            x2 = [1, 2, 3, 4, 5]

            fig, axs = pylab.plt.subplots(2)
            pylab.subplots_adjust(hspace=0.62)

            axs[0].plot(x1, y1)
            axs[1].plot(x2, y2)

            axs[0].set(xlabel="Rundy rozmowy", ylabel="Skumulowane pozyt-negat")
            axs[1].set(xlabel="Rundy rozmowy", ylabel="Skumulowane pozyt-negat")

            axs[0].title.set_text("Wykres żona")
            axs[1].title.set_text("Wykres mąż")

            pylab.plt.show()


        def Analiza(event):
            possib1 = [KategoriaPierwsza.WynikZK1 > KategoriaTrzecia.WynikZK3, KategoriaPierwsza.WynikMK1 > KategoriaTrzecia.WynikMK3]
            possib2 = [KategoriaPierwsza.WynikZK1 < KategoriaTrzecia.WynikZK3, KategoriaPierwsza.WynikMK1 < KategoriaTrzecia.WynikMK3]
            possib3 = [KategoriaPierwsza.WynikZK1 < KategoriaTrzecia.WynikZK3, KategoriaPierwsza.WynikMK1 > KategoriaTrzecia.WynikMK3]
            possib4 = [KategoriaPierwsza.WynikZK1 > KategoriaTrzecia.WynikZK3, KategoriaPierwsza.WynikMK1 < KategoriaTrzecia.WynikMK3]
            possib5 = [KategoriaPierwsza.WynikMK1 >= 3, KategoriaPiata.WynikMK5 >= 3, KategoriaDruga.WynikMK2 >= 3, KategoriaCzwarta.WynikMK4 >= 3, KategoriaTrzecia.WynikMK3 >= 3, KategoriaPierwsza.WynikZK1 >= 3,
            KategoriaPiata.WynikZK5 >= 3, KategoriaDruga.WynikZK2 >= 3, KategoriaCzwarta.WynikZK4 >= 3, KategoriaTrzecia.WynikZK3 >= 3]
            possib6 = [KategoriaPierwsza.WynikMK1 < 0, KategoriaPiata.WynikMK5 < 0, KategoriaDruga.WynikMK2 < 0, KategoriaCzwarta.WynikMK4 < 0, KategoriaTrzecia.WynikMK3 < 0, KategoriaPierwsza.WynikZK1 < 0, KategoriaPiata.WynikZK5 < 0,
            KategoriaDruga.WynikZK2< 0, KategoriaCzwarta.WynikZK4 < 0, KategoriaTrzecia.WynikZK3 < 0]

            if all(possib1):
                #print("Para niewyregulowana")
                messagebox.showinfo("Wyniki analizy","Para niewyregulowana")
            elif all(possib2) or all(possib5):
                #print("Para wyregulowana")
                messagebox.showinfo("Wyniki analizy", "Para wyregulowana")
            elif all(possib3) or all(possib6):
                #print("Wyniki analizy", "Występnują różnice w stosunkach mąż żona. "
                #"Wykres żony wskazuje na parę wyregulowaną, a wykres męża na niewyregulowaną. "
                #"Należy przeprowadzić kolejne badania.")
                messagebox.showinfo("Wyniki analizy", "Występnują różnice w stosunkach mąż żona. "
                "Wykres żony wskazuje na parę wyregulowaną, a wykres męża na niewyregulowaną. "
                "Należy przeprowadzić kolejne badania.")
            elif all(possib4):
                #print("Wyniki analizy", "Występnują różnice w stosunkach mąż - żona. "
                #"Wykres żony wskazuje na parę niewyregulowaną, a wykres męża na wyregulowaną. "
                #"Należy przeprowadzić kolejne badania.")
                messagebox.showinfo("Wyniki analizy", "Występnują różnice w stosunkach mąż - żona. "
                "Wykres żony wskazuje na parę niewyregulowaną, a wykres męża na wyregulowaną. "
                "Należy przeprowadzić kolejne badania")
            else:
                #print("Wyniki analiyz","Brak wystarczających informacji. Należy powtórzyć badanie")
                messagebox.showinfo("Wyniki analizy","Brak wystarczających informacji. Należy powtórzyć badanie")
            


        
        button_1 = Button(self, text="Wynik całościowy żony")
        button_1.bind("<Button-1>", calculateZ)
        button_1.pack(fill=X)
       

        button_1 = Button(self, text="Wynik całościowy męża")
        button_1.bind("<Button-1>", calculateM)
        button_1.pack(fill=X)


        button_1 = Button(self, text="Wykres")
        button_1.bind("<Button-1>", wykres)
        button_1.pack(fill=X)

        button_1 = Button(self, text="Analiza")
        button_1.bind("<Button-1>", Analiza)
        button_1.pack(fill=X)
        
        button_1 = Button(self, text="Wyjście")
        button_1.bind("<Button-1>", close_window)
        button_1.pack(fill=X)
        
if __name__ == "__main__":
    root=Proba()
    root.title("Modelowanie interakcji małżeńskich")
    root.mainloop()

