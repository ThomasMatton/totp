import pyotp
import tkinter as tk
import os
from dotenv import load_dotenv

# Variabelen
PAD = os.path.dirname(os.path.abspath(__file__))
    #.env file inladen voor we deze in de variable SECRET plaatsen
load_dotenv(os.path.join(PAD, '.env'))
SECRET = os.getenv('TOTP_SECRET')

# Variablen voor tkinter instellingen.
TITEL = "Authelia - Thomas"
FORMAAT = "250x180"
LETTERTYPE = ("Helvetica", 32)
KLEUR_FOUT = "red"
KNOP_TEKST = "Kopieer Code"

#Opvragen van de .env file
load_dotenv(os.path.join(PAD, '.env'))

# Functies
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(label.cget("text"))
    copy_btn.config(text="Gekopieerd!", fg="green")
    # Na 1.5 seconde resetten
    root.after(1500, lambda: copy_btn.config(text=KNOP_TEKST, fg="black"))

def update_code():
    if not SECRET:
        label.config(text="Geen Secret!", fg=KLEUR_FOUT, font=("Helvetica", 12))
        return
    
    # Verwijderen van spaties in secret om ervoor te zorgen dat pyotp de juiste format kan gebruiken.
    clean = SECRET.strip().replace(" ", "")
    totp = pyotp.TOTP(clean)
    
    label.config(text=totp.now(), fg="black")
    root.after(1000, update_code)

# GUI
root = tk.Tk()
root.title(TITEL)
root.geometry(FORMAAT)
root.attributes('-topmost', True)

label = tk.Label(root, text="...", font=LETTERTYPE, pady=15)
label.pack()

copy_btn = tk.Button(root, text=KNOP_TEKST, command=copy_to_clipboard, width=15)
copy_btn.pack(pady=10)

# Start de loop
os.chdir(PAD) 
update_code()
root.mainloop()