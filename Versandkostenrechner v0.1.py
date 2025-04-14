import tkinter as tk
from datetime import datetime
import re
from functools import partial


class MyGUI:
    
    global VersandL
    VersandL = []

    def updateDisplay(self):
        global VersandL
        temp = sum(VersandL)
        if self.abzInput.get() == "":
            pass
        else:
            temp = temp - (int(self.abzInput.get()) * 85)
        temp = temp/100

        self.display.config(text = temp)
    
    def save(self):
        global VersandL
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time = re.sub(r'[^\w_. -]', '_', time)  
        file_path = "./results/" + time + '.txt'
        
        with open(file_path, "w") as fp:
            fp.write(str(VersandL) + "\n")
            tSumme = str(sum(VersandL)/100)
            fp.write("Summe: " + tSumme + "\n")
            if self.abzInput.get() == "":
                tAbgezogen = "0"
            else:
                tAbgezogen = str( ( int(self.abzInput.get()) *-85 ) /100 )
            fp.write("Abzug: " + tAbgezogen + "\n")

            tTotal = str( ( sum(VersandL) + (int(self.abzInput.get()) *-85) ) /100 )
            fp.write("Total: " + tTotal + "\n")


    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Versandkostenrechner")
        self.window.geometry("260x400")

        self.vVersandkosten = tk.StringVar(self.window)

        self.display = tk.Label(self.window, text=self.vVersandkosten, font=("Arial", "18"))
        self.display.grid(row=0, column=1, sticky=tk.W+tk.E)


        self.label1 = tk.Label(self.window, text="Abzug:", font=("Arial", "18"))
        self.label1.grid(row=10, column=0, sticky=tk.W+tk.E)

        self.abzInput = tk.Entry(self.window, font=("Arial", "18"), width=2)
        self.abzInput.grid(row=10, column=1, sticky=tk.W+tk.E)


        self.label1 = tk.Label(self.window, text="Custom:", font=("Arial", "18"))
        self.label1.grid(row=9, column=0, sticky=tk.W+tk.E)

        self.customInput = tk.Entry(self.window, font=("Arial", "18"), width=2)
        self.customInput.grid(row=9, column=1, sticky=tk.W+tk.E)

        self.btnAddCustom = tk.Button(self.window, text="+",font=("Arial", "18"), command=self.addCustom)
        self.btnAddCustom.grid(row=9, column=2, sticky=tk.W+tk.E)

        self.btnSave = tk.Button(self.window, text="SAVE",font=("Arial", "18"), command=self.save)
        self.btnSave.grid(row=11, column=1, sticky=tk.W+tk.E)

        # Reset Display
        self.display.config(text = "0,00")

        # BUTTON EDIT
        Kosten = [125, 140, 155,
                   230, 260, 340,
                   395, 649, 799,
                   1149, 1549, 1899,
                   0, 0, 0
                   ]
        
        def kosten_in_str(nr):
            k = str(Kosten[nr])
            l = len(k)
            if l > 2:
                k = k[:l-2]+ "," + k[l-2:]
            return k
        
        KostenFormatiert = [kosten_in_str(x) for x in range(len(Kosten))]
        
        
        self.btn1 = tk.Button(self.window, text=KostenFormatiert[0],font=("Arial", "18"), command=partial(self.add_amount, Kosten[0]))
        self.btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.window, text=KostenFormatiert[1],font=("Arial", "18"), command=partial(self.add_amount, Kosten[1]))
        self.btn2.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.window, text=KostenFormatiert[2],font=("Arial", "18"), command=partial(self.add_amount, Kosten[2]))
        self.btn3.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.window, text=KostenFormatiert[3],font=("Arial", "18"), command=partial(self.add_amount, Kosten[3]))
        self.btn4.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.window, text=KostenFormatiert[4],font=("Arial", "18"), command=partial(self.add_amount, Kosten[4]))
        self.btn5.grid(row=3, column=1, sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.window, text=KostenFormatiert[5],font=("Arial", "18"), command=partial(self.add_amount, Kosten[5]))
        self.btn6.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.btn7 = tk.Button(self.window, text=KostenFormatiert[6],font=("Arial", "18"), command=partial(self.add_amount, Kosten[6]))
        self.btn7.grid(row=4, column=0, sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.window, text=KostenFormatiert[7],font=("Arial", "18"), command=partial(self.add_amount, Kosten[7]))
        self.btn8.grid(row=4, column=1, sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.window, text=KostenFormatiert[8],font=("Arial", "18"), command=partial(self.add_amount, Kosten[8]))
        self.btn9.grid(row=4, column=2, sticky=tk.W+tk.E)

        self.btn10 = tk.Button(self.window, text=KostenFormatiert[9],font=("Arial", "18"), command=partial(self.add_amount, Kosten[9]))
        self.btn10.grid(row=5, column=0, sticky=tk.W+tk.E)
        
        self.btn11 = tk.Button(self.window, text=KostenFormatiert[10],font=("Arial", "18"), command=partial(self.add_amount, Kosten[10]))
        self.btn11.grid(row=5, column=1, sticky=tk.W+tk.E)

        self.btn12 = tk.Button(self.window, text=KostenFormatiert[11],font=("Arial", "18"), command=partial(self.add_amount, Kosten[11]))
        self.btn12.grid(row=5, column=2, sticky=tk.W+tk.E)

        self.btn13 = tk.Button(self.window, text=KostenFormatiert[12],font=("Arial", "18"), command=partial(self.add_amount, Kosten[12]))
        self.btn13.grid(row=6, column=0, sticky=tk.W+tk.E)

        self.btn14 = tk.Button(self.window, text=KostenFormatiert[13],font=("Arial", "18"), command=partial(self.add_amount, Kosten[13]))
        self.btn14.grid(row=6, column=1, sticky=tk.W+tk.E)

        self.btn15 = tk.Button(self.window, text=KostenFormatiert[14],font=("Arial", "18"), command=partial(self.add_amount, Kosten[14]))
        self.btn15.grid(row=6, column=2, sticky=tk.W+tk.E)

        self.window.mainloop()

    def add_amount(self, kosten):
        global VersandL
        VersandL.append(kosten)
        self.updateDisplay()

    def addCustom(self):
        global VersandL
        if self.customInput.get() == "":
            pass
        else:
            CustomAmount = float(str(self.customInput.get()).replace(',', '.')) *100
            VersandL.append(CustomAmount)
        self.updateDisplay()
    
    


MyGUI()