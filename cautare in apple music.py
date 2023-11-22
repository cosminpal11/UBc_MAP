import pyautogui
import keyboard
import time
import requests
from bs4 import BeautifulSoup
import openpyxl
import pyperclip

#functia de accesare buton de cautare, introducere text pentru cautare
def search(src):
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\search.png", confidence = 0.8) != None:
        pressSearch = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\search.png", confidence =0.8)
        pyautogui.click(pressSearch)
        time.sleep(0.3)
        if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\deleteText.png", confidence = 0.9) != None:
             pressX = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\deleteText.png", confidence = 0.9)
             pyautogui.click(pressX)
        time.sleep(0.5)
        pyautogui.write(src)
        pyautogui.press("enter")
        time.sleep(4)

#functia de cautare artist
def searchArtist():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\artist.png", confidence = 0.8) != None:
        touchTheArtist = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\artist.png", confidence = 0.8)
        pyautogui.click(touchTheArtist)

#functie de cautare melodie (fara cont/doar pe Apple Music)
def searchSong():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\song.png", confidence = 0.8) != None:
        pressTheSong = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\song.png", confidence = 0.8)
        pyautogui.click(pressTheSong)

#functie de cautare album
def searchAlbum():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\album.png", confidence = 0.8) != None:
        pressTheAlbum = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\album.png", confidence = 0.8)
        pyautogui.click(pressTheAlbum)

#functie de afisare top melodiiale unui artist
def topSongs(url, lim = 5):
    raspuns = requests.get(url)
    if raspuns.status_code == 200:
        soup = BeautifulSoup(raspuns.text, "html.parser")
        elementeNume = soup.find_all("a", class_ = "click-action svelte-1nh012k")
        infoMelodii = []
        index = 0
        for numeMelodie in elementeNume:
            nume = numeMelodie.get_text(strip = True)
            infoMelodii.append({"nume":nume})
            index +=1
            if(index >= lim):
                return infoMelodii
        return infoMelodii
    else:
        print("Cerere HTTP esuata!")
        return None

#functie de adaugare intr-un fisier Excel melodiile din top
def excelFile(infoMelodii, fisier=r"C:\Users\theda\Desktop\MAP\apple music\topMelodii.xlsx"):
     if infoMelodii:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Melodie"
        sheet["A1"] = "Nume melodie"
        row = 2
        for song in infoMelodii:
            melodie = song["nume"].split("\n")
            nume = melodie
            sheet[f"A{row}"] = f"{nume}"
            row += 1
        workbook.save("topMelodii.xlsx")
        print(f"Fisier salvat cu succes")

#functie de redare a melodiei si afisare a versurilor
def playTheSong():
    q1 = pyautogui.confirm("Doriti sa redati melodia?")
    if q1 == "OK":
        pyautogui.press("enter")
        time.sleep(2)
        q2 = pyautogui.confirm("Doriti sa afisati versurile melodiei?")
        if q2 == "OK":
            if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\lyrics.png", confidence = 0.9) != None:
                showTheLyrics = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\lyrics.png", confidence = 0.9)
                pyautogui.click(showTheLyrics)


#alegere in terminal optiune de cautare
print("Pentru a cauta un artist introduceti <1>")
print("Pentru a cauta un album introduceti <2>")
print("Pentru a cauta o melodie introduceti <3>")
srcOption = int(input("Raspuns: "))
if srcOption == 1:
    src = input("Introduceti artistul pe care vreti sa-l cautati: ")
elif srcOption == 2:
    src = input("Introduceti albumul pe care vreti sa-l cautati: ")
elif srcOption == 3:
    src = input("Introduceti melodia pe care vreti sa o cautati: ")
else:
     print("optiune invalida")
     quit()
time.sleep(3)

#detectare disponibilate cont Apple Music
if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\sign_in.png", confidence = 0.8) != None:
        signInButton = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\sign_in.png", confidence = 0.8)
        account =0
else:
    account = 1

#afisare disponibilitate cont
if account == 0:
    ignore = pyautogui.confirm("Nu exista cont de Apple Music")
else:
    ignore = pyautogui.confirm("Exista cont de Apple Music")

#rulare program in functie de optiunea aleasa
if srcOption == 1:
    search(src)
    searchArtist()
    time.sleep(2)
    q = pyautogui.confirm("Doriti sa vedeti melodiile din top ale artistului?")
    if q == "OK":
        if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9) != None:
            pressURL = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9)
            pyautogui.click(pressURL)
            time.sleep(2)
            pyautogui.hotkey("ctrl", "a")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "c")
            url = pyperclip.paste()
            infoMelodii = topSongs(url, lim = 5)
            for i in infoMelodii:
                melodie=i["nume"]
                print("Nume melodie: ", melodie)
            ignorare = pyautogui.confirm("Melodiile s-au afisat in terminal si in excel")
            excelFile(infoMelodii)
elif srcOption == 2:
    search(src)
    searchAlbum()
elif srcOption == 3:
    if account == 0:
        search(src)
        searchSong()
        time.sleep(3)
        playTheSong()
    else:
        search(src)
        al = pyautogui.confirm("Daca doriti sa cautati in Apple Music apasati <OK>. Pentru Library apasati <Cancel>")
        if al == "OK":
            if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\LibraryTabSelected.png", confidence = 0.9) != None:
                pressAMTab = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\AMTab.png", confidence = 0.9)
                pyautogui.click(pressAMTab)
                time.sleep(3)
                searchSong()
                time.sleep(3)
                playTheSong()
        elif al == "Cancel":
            if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\AMTabSelected.png", confidence = 0.9) != None:
                pressLibraryTab = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\LibraryTab.png", confidence = 0.9)
                pyautogui.click(pressLibraryTab)
                time.sleep(3)
                searchSong()
