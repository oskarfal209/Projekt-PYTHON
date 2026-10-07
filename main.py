
import random
import tkinter as tk

import dane  
import interfejs  

root = tk.Tk()

def kliknij_kod():
  dane.saldo_btc += dane.klik_sila
  losowy_tekst = random.choice(dane.teksty_programistyczne)
  label_status.config(text=losowy_tekst)
  aktualizuj_interfejs()

def kup_ulepszenie(klucz):
  ul = dane.ulepszenia[klucz]
  if dane.saldo_btc >= ul["cena"]:
    dane.saldo_btc -= ul["cena"]  
    ul["poziom"] += 1  

    if ul["typ"] == "pasywny":
      dane.pasywny_dochod_co_2s += ul["korzysc"]
    else:
      dane.klik_sila += ul["korzysc"]

    ul["cena"] = ul["cena"] * 1.1
    ul["korzysc"] = ul["korzysc"] * 1.1

    aktualizuj_interfejs()

def petla_pasywna():
  if dane.pasywny_dochod_co_2s > 0:
    dane.saldo_btc += dane.pasywny_dochod_co_2s
    aktualizuj_interfejs()

  root.after(2000, petla_pasywna)

def aktualizuj_interfejs():
  label_saldo.config(text=f"Stan BTC: {dane.saldo_btc:.6f} BTC")
  for klucz, ul in dane.ulepszenia.items():
    gui_elementy[klucz]["label_info"].config(
        text=(f"{ul['nazwa']}\nPoziom: {ul['poziom']}\nCena: {ul['cena']:.4f} BTC")
    )

label_saldo, label_status, gui_elementy = interfejs.create_GUI(
    root, kliknij_kod, kup_ulepszenie, dane.ulepszenia
)

root.after(2000, petla_pasywna)
root.mainloop()
