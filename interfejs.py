import tkinter as tk

def create_GUI(root, click, buy, ulepszenia):
    root.title("IT Clicker")
    root.geometry("1000x1000")
    root.config(bg="#1e1e1e")
    root.resizable(False, False)

    tytul = tk.Label(
        root,
        text="IT Clicker (totalne gowno)",
        font=("Arial", 30, "bold"),
        bg="black",
        fg="white"
    )
    tytul.pack(pady=15)

    saldo = tk.Label(
        root,
        text="Stan BTC: 0.000000",
        font=("Arial", 20, "bold"),
        bg="#1e1e1e",
        fg="#00ff00",
    )
    saldo.pack(pady=15)

    BTC_klik = tk.Button(
        root,
        text="Napisz coś spoceńcu",
        font=("Arial", 20, "bold"),
        bg="#007acc",
        fg="white",
        command=click,
        width=20,
        height=3
    )
    BTC_klik.pack(pady=5)

    teksty = tk.Label(
        root,
        text="No kliknij przycisk idioto",
        font=("Arial", 12, "bold"),
        bg="#1e1e1e",
        fg="white",
    )
    teksty.pack(pady=5)

    gui_elementy = {}
    
    for klucz, ul in ulepszenia.items():
            frame_kafelek = tk.Frame(root, bg="#2d2d2d", bd=2, relief="groove")
            frame_kafelek.pack(fill="x", padx=10, pady=6)
    
            kafelek_tekst = tk.Label(
                frame_kafelek,
                text=(f"{ul['nazwa']}\nPoziom: {ul['poziom']}\nCena: {ul['cena']:.2f} PLN"),
                font=("Arial", 10),
                bg="#2d2d2d",
                fg="white",
                justify="left",
            )
            kafelek_tekst.pack(side="left", padx=10, pady=8)
    
            kup_przycisk = tk.Button(
                frame_kafelek,
                text="Kup to jeśli cię stać!",
                font=("Arial", 15, "bold"),
                bg="#4caf50",
                fg="white",
                command=lambda k=klucz: buy(k),
            )
            kup_przycisk.pack(side="right", padx=10, pady=8)
    
            gui_elementy[klucz] = {"label_info": kafelek_tekst}
    
    return saldo, teksty, gui_elementy

    