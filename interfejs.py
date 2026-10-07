import tkinter as tk

def create_GUI(root, click, buy, ulepszenia):
    root.title("IT Clicker")
    root.geometry("1000x1000")
    root.config(bg="#1e1e1e")
    root.resizable(False, False)

    tytul = tk.Label(
        root,
        text="IT Clicker (totalne gowno)",
        font=("Arial", 30, "bolder"),
        bg="black"
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

    