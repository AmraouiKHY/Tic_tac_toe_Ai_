from tkinter import *
from pyswip import Prolog

# Create a Prolog instance
prolog = Prolog()
prolog.consult("Diag.pl")  # Load the Prolog knowledge base

def diagnose_condition():
    symptoms = []
    if fever_var.get():
        symptoms.append('fever')
    if headache_var.get():
        symptoms.append('headache')
    if sore_throat_var.get():
        symptoms.append('sore_throat')
    if cough_var.get():
        symptoms.append('cough')
    if fatigue_var.get():
        symptoms.append('fatigue')
    if wheezing_var.get():
        symptoms.append('wheezing')
    if runny_nose_var.get():
        symptoms.append('runny_nose')
    if chest_pain_var.get():
        symptoms.append('chest_pain')
    if congestion_var.get():
        symptoms.append('congestion')
    if difficulty_breathing_var.get():
        symptoms.append('difficulty_breathing')
    if shortness_of_breath_var.get():
        symptoms.append('shortness_of_breath')
    if chest_tightness_var.get():
        symptoms.append('chest_tightness')
    if coughing_var.get():
        symptoms.append('coughing')
    if sneezing_var.get():
        symptoms.append('sneezing')
    # Query the Prolog knowledge base
    query = "diagnose(X), has_symptoms(X, " + str(symptoms) + ")"
    solutions = list(prolog.query(query))
    
    conditions = [solution['X'] for solution in solutions]
    if conditions:
        result_text.set("Possible conditions: " + ", ".join(conditions))
    else:
        result_text.set("No matching conditions found.")

           


# Create the Tkinter window
window = Tk()
window.title("Medical Condition Diagnosis")
window.config(background='white')
MyLabel=Label(window,text='Welcom to xs',font='Poppins 28 bold',bg='white',fg='#333333')
MyLabel.pack()
window.geometry('950x500+300+200')
img=PhotoImage(file='Artboard 1.png')
Label(window,image=img,bg='white').place(x=50,y=90)
# Create symptom checkboxes
fever_var = BooleanVar()
fever_checkbox = Checkbutton(window, text="Fever",font='popins 12',fg='#333333',bg='white', variable=fever_var).place(x=850,y=50)

headache_var = BooleanVar()
headache_checkbox = Checkbutton(window, text="Headache",font='popins 12',fg='#333333',bg='white', variable=headache_var).place(x=850,y=80)


sore_throat_var = BooleanVar()
sore_throat_checkbox = Checkbutton(window, text="Sore Throat",font='popins 12',fg='#333333',bg='white', variable=sore_throat_var).place(x=850,y=110)


cough_var = BooleanVar()
cough_checkbox = Checkbutton(window, text="Cough",font='popins 12',fg='#333333',bg='white', variable=cough_var).place(x=850,y=140)


fatigue_var = BooleanVar()
fatigue_checkbox = Checkbutton(window, text="Fatigue",font='popins 12',fg='#333333',bg='white', variable=fatigue_var).place(x=850,y=170)

wheezing_var = BooleanVar()
wheezing_checkbox = Checkbutton(window, text="Wheezing",font='popins 12',fg='#333333',bg='white', variable=wheezing_var).place(x=850,y=200)

runny_nose_var = BooleanVar()
runny_nose_checkbox = Checkbutton(window, text="Runny Nose",font='popins 12',fg='#333333',bg='white', variable=runny_nose_var).place(x=850,y=230)


chest_pain_var= BooleanVar()
chest_pain_checkbox = Checkbutton(window, text="Chest pain",font='popins 12',fg='#333333',bg='white', variable=chest_pain_var).place(x=850,y=260)


congestion_var = BooleanVar()
congestion_checkbox = Checkbutton(window, text="Congestion",font='popins 12',fg='#333333',bg='white', variable=congestion_var).place(x=850,y=290)

difficulty_breathing_var = BooleanVar()
difficulty_breathing_checkbox = Checkbutton(window, text="Difficulty Breathing",font='popins 12',fg='#333333',bg='white', variable=difficulty_breathing_var).place(x=850,y=320)

shortness_of_breath_var = BooleanVar()
shortness_of_breath_checkbox = Checkbutton(window, text="Shortness of Breath",font='popins 12',fg='#333333',bg='white', variable=shortness_of_breath_var).place(x=850,y=350)


chest_tightness_var = BooleanVar()
chest_tightness_checkbox = Checkbutton(window, text="Chest Tightness",font='popins 12',fg='#333333',bg='white', variable=chest_tightness_var).place(x=850,y=380)


coughing_var = BooleanVar()
coughing_checkbox = Checkbutton(window, text="Coughing",font='popins 12',fg='#333333',bg='white', variable=coughing_var).place(x=850,y=410)

sneezing_var = BooleanVar()
sneezing_checkbox = Checkbutton(window, text="Sneezing",font='popins 12',fg='#333333',bg='white', variable=sneezing_var).place(x=850,y=440)


# Create the diagnose button
diagnose_button = Button(window, text="Diagnose",font='popins 20',fg='#333333',bg='white', command=diagnose_condition).place(x=850,y=500)

# Create the result label
result_text = StringVar()
result_label = Label(window, textvariable=result_text,font='popins 18',fg='#333333',bg='white').place(x=690,y=600)


window.mainloop()