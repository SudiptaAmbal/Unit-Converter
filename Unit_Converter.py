import tkinter as tk
import math

def E(num):
    return math.pow(10,num)

def convert(val, unit_in, unit_out):
    units = {
             #Distance
             'Meter':1, 'Millimeter':0.001, 'Centimeter':0.01, 'Decimeter':0.1, 'Kilometer':1000,
             'Inch':0.0254, 'Foot':0.3048, 'Yard':0.9144, 'Miles':1609.35,
             #Area
             'Sq Meter':1, 'Sq Millimeter':E(-6), 'Sq Centimeter':E(-4), 'Sq Kilometer':E(6),
             'Hactare': E(4), 'Sq Feet':0.09290304, 'Sq Yard':0.83612736, 'Acre':4046.8564224,
             #Mass
             'Grams':1, 'Milligram':0.001, 'Kilogram':1000, 'Quintals':E(5), 'Tonnes':E(6),
             'Pounds':453.59237, 'Carat':0.2,
             #Volume
             'Litre':1, 'Millileter':0.001, 'Cubic Meter':1000, 'Gallon':4.54609, 'Barrel':158.9872949,
             #Speed
             'Kmph':1, 'M/S':3.6, 'M/Min':0.06, 'Mph':1.609344, 'Mach':1193.76,
             #Temperature
             'Celsius':1, 'Fahrenheit':-17.222222, 'Kelvin':-272.15,
             #Pressure
             'Atm':1, 'Pascal':9.86923266*E(-6), 'Kilo Pascal':9.86923266*E(-3), 'Bar':0.986923266,
             'mmHg':1.3157858*E(-3), 'Psi':0.0680459,
             #Time
             'Second':1, 'Millisecond':0.001, 'Minute':60, 'Hour':3600, 'Day':86400, 'Week':604800,
             'Month':2.628*E(6), 'Year':3.154*E(7)
             }

    return val*units[unit_in]/units[unit_out]

def change_unit(value):
    input_opt.set('Select Option',)
    input_opt_menu['menu'].delete(0, 'end')
    input_value.delete(0, tk.END)
    output_opt.set('Select Option',)
    output_opt_menu['menu'].delete(0, 'end')
    result.delete(0, tk.END)

    if value=='Distance':
        for choice in Distance:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Area':
        for choice in Area:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Mass':
        for choice in Mass:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Volume':
        for choice in Volume:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Speed':
        for choice in Speed:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Temperature':
        for choice in Temperature:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Pressure':
        for choice in Pressure:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

    if value=='Time':
        for choice in Time:
            input_opt_menu['menu'].add_command(label=choice, command=tk._setit(input_opt, choice))
            output_opt_menu['menu'].add_command(label=choice, command=tk._setit(output_opt, choice))

def converter():
    measurement1=input_opt.get()
    measurement2=output_opt.get()
    inp = float(input_value.get())

    result.delete(0, tk.END)
    result.insert(0, round(convert(inp, measurement1, measurement2), 4))

choices = ('Select Option',)

Distance = ["Millimeter", "Centimeter", "Decimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Miles",]
Area = ["Sq Millimeter", "Sq Centimeter", "Sq Meter", "Sq Kilometer", "Hactare", "Sq Feet", "Sq Yard", "Acre",]
Mass = ["Milligram", "Grams", "Kilogram", "Quintals", "Tonnes", "Pounds", "Carat",]
Volume = ["Millileter", "Litre", "Cubic Meter", "Gallon", "Barrel"]
Speed = ["M/S", "M/Min", "Kmph", "Mph", "Mach"]
Temperature = ["Celsius", "Fahrenheit", "Kelvin"]
Pressure = ["Atm", "Pascal", "Kilo Pascal", "Bar", "mmHg", "Psi"]
Time = ["Millisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]

root = tk.Tk()
root.title('Unit Converter')
root.geometry('503x235')
root.resizable(width=False,height=False)
root.iconbitmap("unit_converter.ico")

Quantity = ['Distance', 'Area', 'Mass', 'Volume', 'Speed', 'Temperature', 'Pressure', 'Time']
row = 0
col = 0
for i in Quantity:
    button = tk.Button(root, width=15, height=1, relief='raised', text=i, bg='teal', fg='white', 
    font=('arial', 8, 'bold'), activebackground='Aquamarine', command=lambda button=i: change_unit(button))
    button.grid(row=row, column=col, padx=5, pady=8)
    col += 1
    if col > 3:
        row += 1
        col = 0

tk.Label(root, text="Input", font=('arial', 15, 'bold')).grid(row=2, column=0, pady=10)
tk.Label(root, text="Output", font=('arial', 15, 'bold')).grid(row=3, column=0, pady=10)

input_value = tk.Entry(root, width=25, justify = "center")
input_value.grid(row=2, column=1,columnspan=2,)
result = tk.Entry(root, width=25, justify = "center")
result.grid(row=3, column=1,columnspan=2,)

input_opt = tk.StringVar()
input_opt.set('Select Option',)
input_opt_menu = tk.OptionMenu(root, input_opt, *choices)
input_opt_menu.grid(row=2,column=3)

output_opt = tk.StringVar()
output_opt.set('Select Option',)
output_opt_menu = tk.OptionMenu(root, output_opt, *choices)
output_opt_menu.grid(row=3,column=3)

cnvbtn = tk.Button(root, width=11, height=1, relief='raised', text='Convert', bg='teal', fg='white', 
                font=('arial', 10, 'bold'), activebackground='Aquamarine', command=converter)
cnvbtn.grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()