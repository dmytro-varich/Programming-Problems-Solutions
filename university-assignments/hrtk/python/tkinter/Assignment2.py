import tkinter as tk # Library tkinter
import math # Library math
import numpy as np # Library nunmpy

# Function for Task_4.1
def the_find_y ():
    x = input_x.get()
    try: # Check: is x a number? 
        x1 = float(x)
        
    except ValueError: # IF NOT
        lbl_result.config(fg="red")
        lbl_result ["text"] = "Input Error"
        
    else:
        #first_condition
        if (np.exp(9.5) > np.exp(x1)):
            # Formula 1
            x = math.sin(np.exp(9.5)) + math.pow(x1, 2)
            x = x * 1000//1/1000
            # Output to interface
            lbl_result.config(fg="green") 
            lbl_result ["text"]  = x
            label1.config(fg="orange")
        #second_condition    
        elif (np.exp(1.45) == np.exp(x1)):
            # Formula 2
            x = math.acos(-0.35*1.8*-1.8) + math.pow(x1, 1/3)
            x = x * 1000//1/1000
            # Output to interface
            lbl_result.config(fg="green")
            lbl_result ["text"]  = x
            label1.config(fg="orange")
            
        #third_condition    
        elif (np.exp(2.2) < np.exp(x1)):
             # Formula 3
            x = math.cos(math.sqrt(abs(x1 + 2.8*-0.6*2)))
            x = x * 1000//1/1000
             # Output to interface
            lbl_result.config(fg="green")
            lbl_result ["text"]  = x
            label1.config(fg="orange")
            
# Function for Task_4.2
def the_find_z ():
    k = input_k.get()
    try: # Check: is k a number? 
        k1 = int(k)
        
    except ValueError: #IF NOT
        lbl_result2.config(fg="red")
        lbl_result2 ["text"] = "Input Error"
        
    else: #Problem solutions
        mult = 1
        j = -4
        for j in range(j, k1+1): #Find mult
            if (j == 3):
                continue
            mult *= ((j + 2)*j)/(j - 3)
        i = j
        suma = 0
        for i in range(i, k1+6): #Find suma
            suma += (math.pow(i + 5, 1/5))/(i - 11) + 5 * i
        # Output to interface   
        label1.config(fg="orange")
        lbl_result2.config(fg="green")
        lbl_result2 ["text"] = (mult * suma) * 1000//1/1000           
    
# Create window
window = tk.Tk ()
window["bg"] = "Black"
window.title ("Varich Company")
window.resizable (width = False, height = False)
print("Sucсess!") # Output in console

# Frame in code
frm = tk.Frame(master = window) # Frame Header
frm_txt1 = tk.Frame(master = window) # Frame "Task_4.1"
frament = tk.Frame(master = window) # Frame Task solution 4.1
frm_txt2 = tk.Frame(master = window) # Frame "Task_4.2"
frm2 = tk.Frame(master = window) # Frame Task solution 4.2

# Header in code - "Please, Enter your number"
label1 = tk.Label(master=frm, text="Please, Enter your number", fg="White", bg="Black")
label1.grid(row = 0, column = 0, pady = 10, sticky = "w")

# Name Task - "Task_4.1"
lbl_txt1 = tk.Label(master=frm_txt1, text="Task_4.1", fg="White", bg="Black")
lbl_txt1.grid(row = 0, column = 0)

# Task solution 4.1  
label2 = tk.Label(master=frament, text="X ", fg="White", bg="Black") # Label - Text "X"
input_x = tk.Entry(master=frament, width=10) # Entry - "Input"
button = tk.Button(master=frament, text="\N{RIGHTWARDS BLACK ARROW}", command = the_find_y) # Button 1
lbl_result = tk.Label (master = frament, text="Answer", fg="Orange", bg="Black") # Label - "Output"

# GRID 1 - Solution task 4.1
label2.grid (row = 2, column = 0) 
input_x.grid(row = 2, column = 1)
button.grid(row=2, column = 2, padx = 10, pady = 10)
lbl_result.grid (row = 2, column = 3, padx = 10)

# Name Task - "Task_4.2"
lbl_txt2 = tk.Label(master=frm_txt2, text="Task_4.2", fg="White", bg="Black")
lbl_txt2.grid(row = 0, column = 0)

# Task solution 4.2
label3 = label2 = tk.Label(master=frm2, text="K ", fg="White", bg="Black") # Label - Text "K"
input_k = tk.Entry(master=frm2, width=10) # Entry - "Input"
button2 = tk.Button(master=frm2, text="\N{RIGHTWARDS BLACK ARROW}", command = the_find_z) # Button 2
lbl_result2 = tk.Label (master = frm2, text="Answer", fg="Orange", bg="Black") # Label - "Output"

# GRID 1 - Solution task 4.2
label3.grid(row = 0, column = 0)
input_k.grid (row = 0, column = 1, pady = 10)
button2.grid (row = 0, column = 2, padx = 10, pady = 10)
lbl_result2.grid(row = 0, column = 3, padx = 10)

# Frame Layers (Grid)
frm.grid(row=0, column = 0) # Frame Header 
frm_txt1.grid(row = 1, column = 0) # Frame "Task_4.1"             
frament.grid(row = 2, column = 0, padx = 10) # Frame Task solution 4.1
frm_txt2.grid(row = 3, column = 0) # Frame "Task_4.2"
frm2.grid(row = 4, column = 0, sticky="w", padx = 10) # Frame Task solution 4.2

# Color for Frame in code
frm["bg"] = "Black"
frm2["bg"] = "Black"
frament["bg"] = "Black"
frm_txt1["bg"] = "Black"
frm_txt2["bg"] = "Black"

# Start code
window.mainloop ()