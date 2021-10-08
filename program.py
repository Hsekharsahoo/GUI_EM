from tkinter import*
import math

project = Tk()

# reading values
ammeter1 = DoubleVar()
voltmeter1 = DoubleVar()
wattmeter1 = DoubleVar()

ammeter2 = DoubleVar()
voltmeter2 = DoubleVar()
wattmeter2 = DoubleVar()

coreloss_resistance = DoubleVar()
coreloss_reactance = DoubleVar()

equivalent_resistance = DoubleVar()
equivalent_reactance = DoubleVar()
impedance = DoubleVar()
sine_angle = DoubleVar()
noload_pf = DoubleVar()
# reading values end here

# types of tests
def SC():
    global equivalent_reactance
    global equivalent_resistance
    global impedance

    equivalent_reactance.set(math.sqrt((impedance.get()*impedance.get())-(equivalent_resistance.get()*equivalent_resistance.get())))
    impedance.set(wattmeter2.get()/(ammeter2.get()*voltmeter2.get()))
    equivalent_resistance.set(wattmeter2.get()/(ammeter2.get()*ammeter2.get()))

def OC():
    global noload_pf
    global coreloss_reactance
    global coreloss_resistance
    global sine_angle

    noload_pf.set(wattmeter1.get()/(ammeter1.get()*voltmeter1.get()))
    sine_angle.set(math.sqrt(1-(noload_pf.get()*noload_pf.get())))
    coreloss_resistance.set(voltmeter1.get()/(ammeter1.get()*noload_pf.get()))
    coreloss_reactance.set(voltmeter1.get()/(ammeter1.get()*sine_angle.get()))
# end of tests

# definition of logic function
def logic(event=None):
    OC()
    SC()
    value1.config(text="Core Loss Resistance : {a}".format(a=coreloss_resistance.get()))
    value2.config(text="Core Loss Reactance : {a}".format(a=coreloss_resistance.get()))
    value3.config(text="Copper Loss Resistance : {a}".format(a=equivalent_resistance.get()))
    value4.config(text="Copper Loss Reactance : {a}".format(a=equivalent_reactance.get()))
    value5.config(text="No Load Power Factor : {a}".format(a=noload_pf.get()))
# definition of logic ends here

project.geometry("800x800")
project.maxsize(1000, 1000)
project.minsize(700, 700)

# frames definition
main = Frame(project)
main.pack(fill="both")
project.title("Short Circuit and Open Circuit parameters")
title_name = Label(main,text="Circuit parameters for short circuit and open circuit",font="arial 14 bold",
                    bg="blue",fg="white",padx=3, pady=3).grid()

oc_window = Frame(main)

Label(oc_window, text="Open Circuit Test Values : ", font="arial 14 bold",
      bg= "red",fg = "white",padx=10, pady=10, relief=RIDGE).grid(row=1, column=3,padx=15,pady=15)

Label(oc_window, text="Ammeter Reading (A) :").grid(row=2, column=3)
Label(oc_window, text="Voltmeter Reading (V) :").grid(row=3, column=3)
Label(oc_window, text="Wattmeter Reading (W) :").grid(row=4, column=3)

Entry(oc_window, textvariable=ammeter1).grid(row=2, column=4)
Entry(oc_window, textvariable=voltmeter1).grid(row=3, column=4)
Entry(oc_window, textvariable=wattmeter1).grid(row=4, column=4)

oc_window.grid(padx=90, pady=25)

sc_window = Frame(main)

Label(sc_window, text="Short Circuit Test Values : ", font="arial 14 bold",
      bg="red",fg="white", padx=10, pady=10, relief=RIDGE).grid(row=1, column=3,padx=15,pady=15)
Label(sc_window, text="Ammeter Reading (A) :").grid(row=2, column=3)
Label(sc_window, text="Voltmeter Reading (V) :").grid(row=3, column=3)
Label(sc_window, text="Wattmeter Reading (W) :").grid(row=4, column=3)

ammeter_value2 = Entry(sc_window, textvariable=ammeter2).grid(row=2, column=4)
voltmeter_value2 = Entry(sc_window, textvariable=voltmeter2).grid(row=3, column=4)
wattmeter_value2 = Entry(sc_window, textvariable=wattmeter2).grid(row=4, column=4)

sc_window.grid(padx=90, pady=25)

icon = Button(main,bg="Blue", text="Compute Values",font="arial 12 bold",fg="white",pady=10,padx=10,command=logic).grid()

output_window = Frame(main)
output_window.grid(padx=40, pady=20)

Label(output_window,text="The final results of circuit parameters are : ",
      font="arial 12 bold ",fg="white",bg="green",padx=5, pady=5).grid(column= 2)

# output

value1 = Label(output_window, text="Core Loss Resistance : {a}".format(a=coreloss_resistance.get()))
value1.grid(row=3, column=2)

value3 = Label(output_window, text="Copper Loss Resistance : {a}".format(a=equivalent_resistance.get()))
value3.grid(row=5, column=2)

value2 = Label(output_window, text="Core Loss Reactance : {a}".format(a=coreloss_resistance.get()))
value2.grid(row=4, column=2)

value4 = Label(output_window, text="Copper Loss Reactance : {a}".format(a=equivalent_reactance.get()))
value4.grid(row=6, column=2)

value5 = Label(output_window, text="No Load Power Factor : {a}".format(a=noload_pf.get()))
value5.grid(row=7, column=2)

project.mainloop()
