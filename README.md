
# MP3-lejátszó

**Készítette:** Megyesi Dávid  
**Neptun-kód:** R5AA1E  
**Tantárgy:** Szkript nyelvek

## A program bemutatása

A projekt egy Python nyelven készült, grafikus felületű MP3-lejátszó.

A program funkciói:
- MP3-fájlok hozzáadása és lejátszási lista kezelése
- Lejátszás, szüneteltetés és leállítás
- Előző és következő zeneszám kiválasztása
- Hangerőszabályzás
- Lejátszási idő kijelzése és tekerés

## Felhasznált modulok

- **tkinter:** grafikus felület és eseménykezelés
- **pygame:** MP3-lejátszás (`load`, `play`, `pause`, `stop`, `set_volume`)
- **mutagen:** MP3-fájlok hosszának lekérdezése
- **time:** lejátszási idő követése
- **os:** fájlnevek kezelése
- **md_zene:** saját modul a zeneszámok adatainak kezeléséhez

## Saját függvények és osztályok

- **md_fajlnev():** fájlnév kinyerése az elérési útvonalból
- **MDZene:** a zeneszám adatainak tárolása
- **MDZenelejatszo:** a grafikus felület és a lejátszás vezérlése

A saját modul, függvény és osztályok nevében szerepel az MD monogram.

## A projekt fájljai

- `main.py` – a program indítása és grafikus felülete
- `md_zene.py` – saját modul
- `requirements.txt` – szükséges külső csomagok
- `teszt_zenek/` – 3 darab teszt MP3-fájl

## Telepítés és futtatás

A szükséges csomagok telepítése:

    python -m pip install -r requirements.txt

A program indítása:

    python main.py

A program kipróbálásához a `teszt_zenek` mappában található három MP3-fájl használható.
