from tkinter import *

window = Tk()
window.title("tkinter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

def calculateBMI():
    height = entry_height.get()
    weight = entry_weight.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

weight_label = Label(text="enter your weight (kg)")
weight_label.config(padx=10, pady=10)
weight_label.pack()

entry_weight = Entry()
entry_weight.pack()

height_label = Label(text="enter your height (cm)")
height_label.config(padx=10, pady=10)
height_label.pack()

entry_height = Entry()
entry_height.pack()

calculate_button = Button(text="calculate BMI", command= calculateBMI)
calculate_button.pack()

result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if  bmi <= 18.5:
        result_string += "Underweight"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    else:
        result_string += "obese"
    return result_string

window.mainloop()
