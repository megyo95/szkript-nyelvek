
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import time

from mutagen.mp3 import MP3
from md_zene import MDZene


class MDZenelejatszo:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3-lejátszó")
        self.root.geometry("520x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#172234")

        pygame.mixer.init()

        self.zenek = []
        self.aktualis = None
        self.szuneteltetve = False
        self.hossz = 0
        self.kezdes = 0
        self.eltelt = 0
        self.csuszka_mozgatas = False

        tk.Label(
            root,
            text="MP3-lejátszó",
            font=("Arial", 19, "bold"),
            bg="#172234",
            fg="white"
        ).pack(pady=(15, 10))

        self.lista = tk.Listbox(
            root,
            width=49,
            height=9,
            font=("Arial", 10),
            bg="#24344a",
            fg="white",
            selectbackground="#3679b5",
            relief="flat",
            borderwidth=0
        )
        self.lista.pack(pady=8)
        self.lista.bind("<Double-Button-1>", self.dupla_kattintas)

        tk.Button(
            root,
            text="MP3 hozzáadása",
            command=self.zene_hozzaadasa,
            font=("Arial", 10),
            bg="#344b66",
            fg="white",
            activebackground="#45658a",
            activeforeground="white",
            relief="flat",
            padx=15,
            pady=6
        ).pack(pady=8)

        self.vezerlok = tk.Frame(root, bg="#172234")
        self.vezerlok.pack(pady=10)

        self.gomb("⏮", self.elozo)
        self.gomb("▶", self.lejatszas)
        self.gomb("⏸", self.szunet)
        self.gomb("■", self.stop)
        self.gomb("⏭", self.kovetkezo)

        self.ido_keret = tk.Frame(root, bg="#172234")
        self.ido_keret.pack(pady=5)

        self.aktualis_ido = tk.Label(
            self.ido_keret,
            text="00:00",
            bg="#172234",
            fg="white",
            font=("Arial", 9)
        )
        self.aktualis_ido.pack(side="left")

        self.folyamat = tk.Scale(
            self.ido_keret,
            from_=0,
            to=100,
            orient="horizontal",
            showvalue=False,
            length=330,
            bg="#172234",
            fg="white",
            highlightthickness=0,
            troughcolor="#526075",
            activebackground="#5ba9e5"
        )
        self.folyamat.pack(side="left", padx=8)
        self.folyamat.bind("<ButtonPress-1>", self.tekeres_kezdete)
        self.folyamat.bind("<ButtonRelease-1>", self.tekeres_vege)

        self.teljes_ido = tk.Label(
            self.ido_keret,
            text="00:00",
            bg="#172234",
            fg="white",
            font=("Arial", 9)
        )
        self.teljes_ido.pack(side="left")

        self.hangero_keret = tk.Frame(root, bg="#172234")
        self.hangero_keret.pack(pady=5)

        tk.Label(
            self.hangero_keret,
            text="♪",
            font=("Arial", 16),
            bg="#172234",
            fg="white"
        ).pack(side="left", padx=5)

        self.hangero = tk.Scale(
            self.hangero_keret,
            from_=0,
            to=100,
            orient="horizontal",
            showvalue=False,
            bg="#172234",
            highlightthickness=0,
            troughcolor="#526075",
            length=160,
            command=self.hangero_allitas
        )
        self.hangero.set(70)
        self.hangero.pack(side="left")

        self.allapot = tk.Label(
            root,
            text="Nincs kiválasztott zeneszám",
            bg="#172234",
            fg="#aab8cb",
            font=("Arial", 9)
        )
        self.allapot.pack(pady=5)

        pygame.mixer.music.set_volume(0.7)
        self.root.protocol("WM_DELETE_WINDOW", self.bezaras)
        self.ido_frissites()

    def gomb(self, felirat, parancs):
        tk.Button(
            self.vezerlok,
            text=felirat,
            command=parancs,
            font=("Segoe UI Symbol", 17),
            width=3,
            bg="#344b66",
            fg="white",
            activebackground="#5ba9e5",
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        ).pack(side="left", padx=5)

    def zene_hozzaadasa(self):
        fajlok = filedialog.askopenfilenames(
            title="MP3-fájlok kiválasztása",
            filetypes=[("MP3 fájlok", "*.mp3")]
        )

        for fajl in fajlok:
            zene = MDZene(fajl)
            self.zenek.append(zene)
            self.lista.insert(tk.END, zene.adatok())

    def inditas(self, index, pozicio=0):
        if not 0 <= index < len(self.zenek):
            return

        try:
            zene = self.zenek[index]
            hossz = MP3(zene.fajl_utvonal).info.length

            pygame.mixer.music.load(zene.fajl_utvonal)
            pygame.mixer.music.play(start=pozicio)

            self.aktualis = index
            self.szuneteltetve = False
            self.hossz = hossz
            self.kezdes = time.monotonic()
            self.eltelt = pozicio

            self.folyamat.config(to=max(1, int(hossz)))
            self.folyamat.set(int(pozicio))
            self.aktualis_ido.config(text=self.ido_formazas(pozicio))
            self.teljes_ido.config(text=self.ido_formazas(hossz))

            self.lista.selection_clear(0, tk.END)
            self.lista.selection_set(index)
            self.lista.activate(index)

            self.allapot.config(text="Lejátszás: " + zene.cim)

        except (pygame.error, Exception) as hiba:
            messagebox.showerror("Lejátszási hiba", str(hiba))

    def lejatszas(self):
        if self.szuneteltetve:
            pygame.mixer.music.unpause()
            self.szuneteltetve = False
            self.kezdes = time.monotonic()
            self.allapot.config(text="Lejátszás folytatva")
            return

        kijeloles = self.lista.curselection()

        if kijeloles:
            self.inditas(kijeloles[0])
        elif self.zenek:
            self.inditas(0)
        else:
            messagebox.showinfo(
                "Információ",
                "Először adj hozzá egy MP3-fájlt!"
            )

    def szunet(self):
        if pygame.mixer.music.get_busy():
            self.eltelt += time.monotonic() - self.kezdes
            pygame.mixer.music.pause()
            self.szuneteltetve = True
            self.allapot.config(text="Lejátszás szüneteltetve")

    def stop(self):
        pygame.mixer.music.stop()
        self.szuneteltetve = False
        self.eltelt = 0
        self.folyamat.set(0)
        self.aktualis_ido.config(text="00:00")
        self.allapot.config(text="Lejátszás leállítva")

    def elozo(self):
        if self.zenek:
            index = self.aktualis if self.aktualis is not None else 0
            self.inditas((index - 1) % len(self.zenek))

    def kovetkezo(self):
        if self.zenek:
            index = self.aktualis if self.aktualis is not None else -1
            self.inditas((index + 1) % len(self.zenek))

    def dupla_kattintas(self, event):
        kijeloles = self.lista.curselection()
        if kijeloles:
            self.inditas(kijeloles[0])

    def hangero_allitas(self, ertek):
        pygame.mixer.music.set_volume(int(ertek) / 100)

    def ido_formazas(self, masodperc):
        masodperc = int(masodperc)
        perc = masodperc // 60
        mp = masodperc % 60
        return f"{perc:02d}:{mp:02d}"

    def ido_frissites(self):
        if self.aktualis is not None and not self.szuneteltetve:
            if pygame.mixer.music.get_busy():
                pozicio = self.eltelt + time.monotonic() - self.kezdes
                pozicio = min(pozicio, self.hossz)

                if not self.csuszka_mozgatas:
                    self.folyamat.set(int(pozicio))
                    self.aktualis_ido.config(
                        text=self.ido_formazas(pozicio)
                    )

        self.root.after(250, self.ido_frissites)

    def tekeres_kezdete(self, event):
        self.csuszka_mozgatas = True

    def tekeres_vege(self, event):
        if self.aktualis is not None:
            pozicio = min(float(self.folyamat.get()), self.hossz)
            index = self.aktualis
            self.inditas(index, pozicio)

        self.csuszka_mozgatas = False

    def bezaras(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.root.destroy()


root = tk.Tk()
app = MDZenelejatszo(root)
root.mainloop()
