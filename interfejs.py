# =========================================================================
# PLIK: interfejs.py
# OPIS: Odpowiada WYŁĄCZNIE za wizualną stronę okna (Tkinter).
# SKĄD WIE CO WYŚWIETLIĆ? Dostaje to w argumentach z pliku main.py
# podczas wywoływania funkcji stworz_interfejs().
# =========================================================================
import tkinter as tk


# Ta funkcja jest wywoływana z pliku main.py. Przyjmuje:
# - root: okno główne gry
# - funkcja_klikniecia: co zrobić po kliknięciu przycisku "Napisz kod"
# - funkcja_zakupu: co zrobić po kliknięciu przycisku "Kup" w sklepie
# - ulepszenia: dane o ulepszeniach z pliku dane.py
def stworz_interfejs(root, funkcja_klikniecia, funkcja_zakupu, ulepszenia):

  # Podstawowa konfiguracja okna (rozmiar i ciemny styl)
  root.title("IT Clicker")
  root.geometry("450x680")
  root.config(bg="#1e1e1e")

  # --- Górny panel (Saldo i Przycisk) ---
  # Etykieta salda - stąd bierze się początkowy napis na górze
  label_saldo = tk.Label(
      root,
      text="Stan BTC: 0.000000 BTC",
      font=("Arial", 16, "bold"),
      bg="#1e1e1e",
      fg="#00ff00",
  )
  label_saldo.pack(pady=15)

  # Główny przycisk "Napisz kod"
  # command=funkcja_klikniecia bierze się z pliku main.py (tam jest napisane, co się dzieje po kliknięciu)
  btn_klik = tk.Button(
      root,
      text="Napisz kod",
      font=("Arial", 14, "bold"),
      bg="#007acc",
      fg="white",
      command=funkcja_klikniecia,
      width=20,
      height=2,
  )
  btn_klik.pack(pady=5)

  # Etykieta statusu (tutaj pojawiają się losowe teksty o programowaniu)
  label_status = tk.Label(
      root,
      text="Kliknij 'Napisz kod', aby zacząć...",
      font=("Arial", 11, "italic"),
      bg="#1e1e1e",
      fg="white",
  )
  label_status.pack(pady=10)

  # --- Sekcja Sklep ---
  label_sklep = tk.Label(
      root,
      text="--- SKLEP ---",
      font=("Arial", 14, "bold"),
      bg="#1e1e1e",
      fg="orange",
  )
  label_sklep.pack(pady=10)

  # Pusty słownik, do którego zapiszemy elementy kafelków, żeby móc je potem aktualizować
  gui_elementy = {}

  # Pętla generująca kafelki na podstawie danych (ulepszenia) przekazanych z pliku dane.py przez main.py
  for klucz, ul in ulepszenia.items():
    # Ramka dla pojedynczego kafelka
    frame_kafelek = tk.Frame(root, bg="#2d2d2d", bd=2, relief="groove")
    frame_kafelek.pack(fill="x", padx=20, pady=6)

    # Napis w kafelku (nazwa, poziom, cena) - dane biorą się ze słownika w dane.py
    lbl_info = tk.Label(
        frame_kafelek,
        text=(
            f"{ul['nazwa']}\nPoziom: {ul['poziom']}\nCena: {ul['cena']:.4f} BTC"
        ),
        font=("Arial", 10),
        bg="#2d2d2d",
        fg="white",
        justify="left",
    )
    lbl_info.pack(side="left", padx=10, pady=8)

    # Przycisk "Kup" przy każdym kafelku
    # lambda k=klucz pozwala przekazać do pliku main.py informację, KTÓRE dokładnie ulepszenie gracz chce kupić
    btn_kup = tk.Button(
        frame_kafelek,
        text="Kup",
        font=("Arial", 10, "bold"),
        bg="#4caf50",
        fg="white",
        command=lambda k=klucz: funkcja_zakupu(k),
    )
    btn_kup.pack(side="right", padx=10, pady=8)

    # Zapisujemy etykietę do słownika, żeby main.py wiedział, jak ją później podmieniać
    gui_elementy[klucz] = {"label_info": lbl_info}

  # Zwracamy gotowe elementy z powrotem do pliku main.py
  return label_saldo, label_status, gui_elementy