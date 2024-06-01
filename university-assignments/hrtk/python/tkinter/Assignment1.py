import tkinter as tk
import math

N = 1000

def createNewWindow():
    def on_button_click():
        try:
            product = float(entry1.get())
            code = int(entry2.get())
            result = ah(product, code)
            label5.config(text=f"Ответ: {result}")
        except ValueError:
            label5.config(text="Ошибка: введите корректные данные.")

    def ctg(x):
        return 1 / math.tan(x)
        
    def ah(price, code):    
        if price > N:
            if code >= 100 and code <= 150:
                a = price - (price * 0.02)
                return a
            elif code in [210, 215, 220] :
                a = price - (price * 0.07)
                return a
            elif code >= 230 and code <= 300:
                a = price - (price * 0.09)
                return a
        return price

    newWindow = tk.Toplevel(window)
    newWindow.state('zoomed')
    newWindow.configure(bg='White')  # Синий цвет фона окна
    
    label1 = tk.Label(newWindow, text='VARICH SHOP')
    label1.config(font=('helvetica', 14))
    label1.pack(padx=125, pady=1)
    
    label2 = tk.Label(newWindow, text='Стоимость товара')
    label2.config(font=('helvetica', 14))
    label2.pack(padx=125, pady=2)
    
    entry1 = tk.Entry(newWindow)
    entry1.pack()
    
    label3 = tk.Label(newWindow, text='Введите код товара')
    label3.config(font=('helvetica', 14))
    label3.pack(padx=125, pady=3)
    
    entry2 = tk.Entry(newWindow)
    entry2.pack(padx=120, pady=10)
    
    label5 = tk.Label(newWindow, text="Ответ: ", font=("helvetica", 10))
    label5.pack(padx=120, pady=25)
    
    button1 = tk.Button(newWindow, text="Готово", bg="green", fg="white", font=('helvetica', 9, 'bold'), command=on_button_click)
    button1.pack(padx=120, pady=15)

window = tk.Tk()
window.state('zoomed')
window.configure(bg='Green')  # Синий цвет фона окна

label1 = tk.Label(window, text='VARICH SHOP', fg='Yellow', bg='Green')
label1.config(font=('helvetica', 50))
label1.pack(padx=125, pady=50)

label2 = tk.Label(window, text='1. Если общая стоимость покупки составляет более 1000 грн, то вы получите скидку - 5%')
label2.config(font=('helvetica', 14))
label2.pack(padx=125, pady=0)

label3 = tk.Label(window, text='2. Если вы используете промокод на товар - 100...150, то получите скидку - 2%')
label3.config(font=('helvetica', 14))
label3.pack(padx=105, pady=1)

label4 = tk.Label(window, text='3. Если вы используете промокод на товар - 210, 215 та 220, то получите скидку - 7%')
label4.config(font=('helvetica', 14))
label4.pack(padx=125, pady=2)

label5 = tk.Label(window, text='4. Если вы используете промокод на товар - 230..300, то получите скидку - 9%')
label5.config(font=('helvetica', 14))
label5.pack(padx=125, pady=3)

button1 = tk.Button(window, text="Начать", command=createNewWindow, bg="Yellow", fg="White", font=('helvetica', 9, 'bold'))
button1.pack(padx=125, pady=180)

window.mainloop()
