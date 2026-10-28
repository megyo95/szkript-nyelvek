
# Python MP3-lejátszó

## Hallgató adatai

- Név: Megyesi Dávid
- Neptun-kód: R5AA1E
- Tantárgy: Szkript nyelvek
- Fejlesztési környezet: PyCharm
- Programozási nyelv: Python 3.14.5

## 1. A feladat leírása
A beadandó feladat célja egy egyszerű, grafikus felülettel rendelkező MP3-lejátszó alkalmazás elkészítése Python programozási nyelven.
A program lehetővé teszi a számítógépen található MP3-fájlok megnyitását és lejátszását, valamint a lejátszás vezérlését.
A grafikus felület a tkinter modul segítségével készült, a hangfájlok lejátszását a pygame-ce csomag biztosítja.

### A program funkciói
- Egy vagy több MP3-fájl hozzáadása
- Lejátszási lista megjelenítése
- Kiválasztott zeneszám lejátszása
- Lejátszás szüneteltetése és folytatása
- Lejátszás leállítása
- Előző és következő zeneszám kiválasztása
- Hangerő szabályozása
- Zeneszám teljes hosszának kijelzése
- Aktuális lejátszási idő megjelenítése
- Lejátszási pozíció megváltoztatása csúszkával
- Zeneszám indítása dupla kattintással

## 2. Felhasznált modulok
### tkinter – grafikus felület
A tkinter a Python szabványos grafikus felületkezelő modulja.
Feladata az alkalmazás ablakának, gombjainak, listájának és csúszkáinak létrehozása.
Használt elemek és függvények:
- tkinter.Tk()
- tkinter.Label()
- tkinter.Button()
- tkinter.Frame()
- tkinter.Listbox()
- tkinter.Scale()
- filedialog.askopenfilenames()
- messagebox.showinfo()
- messagebox.showerror()
- root.after()

### pygame – bemutatandó modul
A pygame modul az MP3-fájlok lejátszásáért felel.
A program a pygame-ce csomagot használja, amely pygame néven importálható.
Használt függvények:
- pygame.mixer.init() – hangrendszer inicializálása
- pygame.mixer.music.load() – MP3-fájl betöltése
- pygame.mixer.music.play() – lejátszás indítása
- pygame.mixer.music.pause() – lejátszás szüneteltetése
- pygame.mixer.music.unpause() – lejátszás folytatása
- pygame.mixer.music.stop() – lejátszás leállítása
- pygame.mixer.music.set_volume() – hangerő beállítása
- pygame.mixer.music.get_busy() – lejátszási állapot lekérdezése
- pygame.mixer.quit() – hangrendszer leállítása
A bemutatandó modul legalább három függvényének használata teljesül.

### mutagen – MP3-információk kezelése
A mutagen külső Python-modul segítségével a program meghatározza a betöltött MP3-fájl hosszát.
Használt elem:
- mutagen.mp3.MP3()
- MP3.info.length

### time – időkezelés
A Python szabványos modulja.
Használt függvény:
- time.monotonic()
Feladata a lejátszási idő követése.

### os – fájlkezelés
A Python szabványos modulja.
Használt függvények:
- os.path.basename()
- os.path.splitext()
A modul segítségével a fájl teljes elérési útvonalából kinyerhető a zeneszám neve.

## 3. Saját modul
### md_zene.py
A program saját készítésű modulja.
A modul nevében szerepel az MD monogram.
Feladata a zeneszámok adatainak kezelése.

### Saját függvény
md_fajlnev(fajl_utvonal)
A függvény a megadott fájlútvonalból kinyeri a fájl nevét, és eltávolítja az MP3-kiterjesztést.
A függvény nevében szerepel az MD monogram.

## 4. Saját osztályok
### MDZene
A md_zene.py modulban található saját osztály.
Feladata egy zeneszám adatainak tárolása.
Attribútumai:
- fajl_utvonal
- cim
Metódusai:
- __init__()
- adatok()

### MDZenelejatszo
A main.py fájlban található saját osztály.
Feladata a grafikus felület létrehozása, az események kezelése és a lejátszás vezérlése.
Fontosabb metódusai:
- __init__()
- gomb()
- zene_hozzaadasa()
- inditas()
- lejatszas()
- szunet()
- stop()
- elozo()
- kovetkezo()
- dupla_kattintas()
- hangero_allitas()
- ido_formazas()
- ido_frissites()
- tekeres_kezdete()
- tekeres_vege()
- bezaras()
Mindkét saját osztály nevében szerepel az MD monogram.

## 5. Eseménykezelés
A program eseményvezérelt működésű.
Az eseménykezelés a tkinter segítségével valósul meg.
Példák:
- Gombnyomásra elindul vagy leáll a lejátszás.
- Dupla kattintással elindítható a kiválasztott zeneszám.
- A hangerőcsúszka mozgatásával változik a hangerő.
- A lejátszási csúszka segítségével a zeneszám másik részére lehet ugrani.
- Az ablak bezárásakor a hangrendszer szabályosan leáll.

## 6. A program felépítése
A projekt fájljai:
    Projekt_feladat_R5AA1E/
    |
    |-- main.py
    |-- md_zene.py
    |-- requirements.txt
    |-- README.md
    |-- teszt_zenek/
        |-- 3 darab teszt MP3-fájl
A fájlok szerepe:
- main.py: a grafikus felület és a lejátszás vezérlése
- md_zene.py: saját modul, zeneszámok adatainak kezelése
- requirements.txt: a szükséges külső Python-csomagok
- README.md: a program dokumentációja
- teszt_zenek/: a program teszteléséhez mellékelt három MP3-fájl
A program indítófájlja: main.py
Az alapablak változóneve: root
A program objektumának változóneve: app

## 7. Telepítés és indítás
A program Python 3.14.5 verzióval készült.
A szükséges külső csomagok a requirements.txt fájlban találhatók.
Telepítés terminálból:
    python -m pip install -r requirements.txt
A program indítása:
    python main.py
A program grafikus ablaka automatikusan megnyílik.

## 8. Teszt MP3-fájlok
A projekthez 3 darab teszt MP3-fájl tartozik.
A tesztfájlok a projekt teszt_zenek nevű mappájában találhatók.
A tesztfájlok célja, hogy a program működése saját zenefájlok nélkül is kipróbálható legyen.

### Tesztelés menete
1. Indítsuk el a main.py fájlt.
2. Kattintsunk az "MP3 hozzáadása" gombra.
3. Nyissuk meg a teszt_zenek mappát.
4. Jelöljük ki a három MP3-fájlt.
5. Kattintsunk a "Lejátszás" gombra.
6. Próbáljuk ki a szüneteltetést és a folytatást.
7. Próbáljuk ki az előző és következő zeneszám gombokat.
8. Állítsuk a hangerőt a csúszkával.
9. Próbáljuk ki a zeneszámon belüli tekerést.
10. Állítsuk le a lejátszást.

## 9. Összegzés
A beadandó során egy működő, grafikus Python MP3-lejátszó alkalmazás készült.
A projekt bemutatja a Python-modulok használatát, a saját modul, függvény és osztály létrehozását, valamint a grafikus eseménykezelést.
A program egyszerűen kezelhető, és a mellékelt teszt MP3-fájlok segítségével kipróbálható.