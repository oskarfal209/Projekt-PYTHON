# =========================================================================
# PLIK: main.py
# OPIS: Główny plik sterujący. Łączy dane (dane.py) z interfejsem (interfejs.py)
# i obsługuje całą logikę gry (kliknięcia, zakupy, upływ czasu).
# =========================================================================
import random
import tkinter as tk

import dane  # Stąd main.py bierze zmienne, saldo i słownik ulepszeń
import interfejs  # Stąd main.py bierze funkcję rysującą okno

# Inicjalizacja głównego okna Tkinter
root = tk.Tk()


# --- Logika głównego przycisku ---
# Skąd się bierze? Jest uruchamiana za każdym razem, gdy gracz kliknie "Napisz kod".
def kliknij_kod():
  # Zwiększamy saldo BTC o siłę kliknięcia (bierzemy zmienną z pliku dane.py)
  dane.saldo_btc += dane.klik_sila

  # Losujemy jeden tekst z listy tekstów w pliku dane.py
  losowy_tekst = random.choice(dane.teksty_programistyczne)
  # Zmieniamy tekst w etykicie statusu (która pochodzi z interfejsu)
  label_status.config(text=losowy_tekst)

  # Odświeżamy widok na ekranie
  aktualizuj_interfejs()


# --- Logika zakupu ulepszeń ---
# Skąd się bierze? Jest uruchamiana po kliknięciu przycisku "Kup" w sklepie.
def kup_ulepszenie(klucz):
  # Bierzemy dane konkretnego ulepszenia ze słownika w dane.py (np. "monster")
  ul = dane.ulepszenia[klucz]

  # Sprawdzamy czy gracz ma dość kasy (saldo z dane.py >= cena z dane.py)
  if dane.saldo_btc >= ul["cena"]:
    dane.saldo_btc -= ul["cena"]  # Odejmujemy koszt z dane.py
    ul["poziom"] += 1  # Zwiększamy poziom ulepszenia w dane.py

    # Dodajemy bonus w zależności od typu ulepszenia
    if ul["typ"] == "pasywny":
      dane.pasywny_dochod_co_2s += ul["korzysc"]
    else:
      dane.klik_sila += ul["korzysc"]

    # Balans gry: cena rośnie x2, a korzyść x1.1 (zapisujemy to w dane.py)
    ul["cena"] = ul["cena"] * 2
    ul["korzysc"] = ul["korzysc"] * 1.1

    # Odświeżamy widok na ekranie
    aktualizuj_interfejs()


# --- Pętla pasywnego dochodu co 2 sekundy ---
def petla_pasywna():
  # Jeśli pasywny dochód z dane.py jest większy niż 0, dodajemy go do salda
  if dane.pasywny_dochod_co_2s > 0:
    dane.saldo_btc += dane.pasywny_dochod_co_2s
    aktualizuj_interfejs()

  # root.after sprawia, że ta funkcja wywoła sama siebie ponownie za dokładnie 2000 milisekund (2 sekundy)
  root.after(2000, petla_pasywna)


# --- Odświeżanie wyglądu ekranu ---
def aktualizuj_interfejs():
  # Aktualizujemy napis z ilością BTC na górze okna (bierzemy saldo z dane.py)
  label_saldo.config(text=f"Stan BTC: {dane.saldo_btc:.6f} BTC")

  # Aktualizujemy napisy na kafelkach sklepu (bierzemy nowe poziomy i ceny z dane.py)
  for klucz, ul in dane.ulepszenia.items():
    gui_elementy[klucz]["label_info"].config(
        text=(f"{ul['nazwa']}\nPoziom: {ul['poziom']}\nCena: {ul['cena']:.4f} BTC")
    )


# --- URUCHOMIENIE PROGRAMU ---
# Tworzymy interfejs: wywołujemy funkcję z pliku interfejs.py,
# przekazując jej okno (root), nasze funkcje logiki oraz dane o ulepszeniach z dane.py.
# W zamian plik main.py otrzymuje gotowe elementy graficzne do kontrolowania.
label_saldo, label_status, gui_elementy = interfejs.stworz_interfejs(
    root, kliknij_kod, kup_ulepszenie, dane.ulepszenia
)

# Uruchamiamy zegar pasywnego dochodu (odpali się pierwszy raz po 2 sekundach)
root.after(2000, petla_pasywna)

# Odpalenie głównej pętli okna Tkinter (to sprawia, że gra działa i nie zamyka się sama)
root.mainloop()