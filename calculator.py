import customtkinter as ctk

def button_click(number):
    current = calculator_display.get()
    calculator_display.delete(0, ctk.END)
    calculator_display.insert(0, current + str(number))

def do_calculation():
    try:
        result = eval(calculator_display.get())
        calculator_display.delete(0, ctk.END)
        calculator_display.insert(0, str(result))
    except Exception:
        calculator_display.delete(0, ctk.END)
        calculator_display.insert(0, "Error")

def remove_last():
    current = calculator_display.get()
    calculator_display.delete(0, ctk.END)
    calculator_display.insert(0, current[:-1])

def open_calculator():
    global calculator_display
    calculator = ctk.CTk()
    calculator.geometry("600x925")
    calculator.title("Calculator")
    calculator.attributes("-topmost", True)

    calculator_display = ctk.CTkEntry(calculator, bg_color="transparent", width=600, font=("Helvetica", 50))
    calculator_display.place(y=10)
    calculator_display.focus_force()


    calculator_num1 = ctk.CTkButton(calculator, text="1", width=75, height=75, command=lambda: button_click(1))
    calculator_num2 = ctk.CTkButton(calculator, text="2", width=75, height=75, command=lambda: button_click(2))
    calculator_num3 = ctk.CTkButton(calculator, text="3", width=75, height=75, command=lambda: button_click(3))
    calculator_num4 = ctk.CTkButton(calculator, text="4", width=15, height=75, command=lambda: button_click(4))
    calculator_num5 = ctk.CTkButton(calculator, text="5", width=15, height=75, command=lambda: button_click(5))
    calculator_num6 = ctk.CTkButton(calculator, text="6", width=15, height=75, command=lambda: button_click(6))
    calculator_num7 = ctk.CTkButton(calculator, text="7", width=15, height=75, command=lambda: button_click(7))
    calculator_num8 = ctk.CTkButton(calculator, text="8", width=15, height=75, command=lambda: button_click(8))
    calculator_num9 = ctk.CTkButton(calculator, text="9", width=75, height=75, command=lambda: button_click(9))
    calculator_num0 = ctk.CTkButton(calculator, text="0", width=75, height=75, command=lambda: button_click(0))

    calculator_remove = ctk.CTkButton(calculator, text="<", width=15, height=5, command=remove_last)
    calculator_add = ctk.CTkButton(calculator, text="+", width=15, height=5, command=lambda: button_click("+"))
    calculator_minus = ctk.CTkButton(calculator, text="-", width=15, height=5, command=lambda: button_click("-"))
    calculator_times = ctk.CTkButton(calculator, text="*", width=15, height=5, command=lambda: button_click("*"))
    calculator_divide = ctk.CTkButton(calculator, text="/", width=15, height=5, command=lambda: button_click("/"))
    calculator_equal = ctk.CTkButton(calculator, text="=", width=15, height=5, command=do_calculation)

    calculator_num1.place(y=200, x=50)
    calculator_num2.place(y=200, x=200)
    calculator_num3.place(y=200, x=350)
    calculator_num4.place(y=350, x=50)
    calculator_num5.place(y=350, x=200)
    calculator_num6.place(y=350, x=350)
    calculator_num7.place(y=500, x=50)
    calculator_num8.place(y=500, x=200)
    calculator_num9.place(y=500, x=350)
    calculator_num0.place(y=650, x=200)

    calculator_remove.place(y=700, x=475)
    calculator_add.place(y=200, x=475)
    calculator_minus.place(y=300, x=475)
    calculator_times.place(y=400, x=475)
    calculator_divide.place(y=500, x=475)
    calculator_equal.place(y=600, x=475)

    calculator.mainloop()

open_calculator()