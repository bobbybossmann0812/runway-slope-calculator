import tkinter as tk
from tkinter import messagebox

def button_click():
    input1_text = entry1.get()
    input2_text = entry2.get()
    input3_text = entry3.get()

    try:
        input1_val = float(input1_text)
        input2_val = float(input2_text)
        input3_val = float(input3_text)

        ergebnishoehe = input2_val - input1_val
        ergebnisgesamt = (ergebnishoehe / input3_val) * 10

        result_label.config(text=f"Ergebnis: {ergebnisgesamt:.2f}")
    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie gültige Zahlen ein!")

root = tk.Tk()
root.title("Runway Slope Calculator")
root.geometry("400x400")
# Setze das App-Icon (Ersetze 'icon.ico' mit dem Pfad zu deinem Icon-Datei)
#('./icon.ico')
root.iconbitmap(r'V:\Projekte\runway-slope-calculator\icon.ico')
#root.wm_iconphoto(False, photo)


label_lorem = tk.Label(root, text="Höhe des Startbahnanfang in ft")
label_lorem.grid(row=0, column=0)
label_lorem = tk.Label(root, text="Höhe des Startbahnendes in ft")
label_lorem.grid(row=1, column=0)
label_lorem = tk.Label(root, text="Länge der Startbahn in Metern")
label_lorem.grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

button = tk.Button(root, text="Berechnen", command=button_click)

result_label = tk.Label(root, text="Hier wird das Ergebnis angezeigt.")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
