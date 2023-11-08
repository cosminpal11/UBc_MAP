import pyautogui
import keyboard
import time
import requests
from bs4 import BeautifulSoup
import openpyxl
import pyperclip

def search(cautare):
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\search.png", confidence=0.8)!=None:
        searchMusic = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\search.png", confidence=0.8)
        pyautogui.click(searchMusic)
        time.sleep(1)
        if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\ctrlA.png", confidence=0.9)!=None:
             ctrlABack = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\ctrlA.png", confidence=0.9)
             pyautogui.click(ctrlABack)
        time.sleep(1)
        pyautogui.write(cautare)
        pyautogui.press("enter")
        time.sleep(4)
def searchArtist():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\artist.png", confidence = 0.6) != None:
        touchTheArtist = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\artist.png", confidence = 0.6)
        pyautogui.click(touchTheArtist)

def searchSong():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\song.png", confidence = 0.8) != None:
        touchTheArtist = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\song.png", confidence = 0.8)
        pyautogui.click(touchTheArtist)
        time.sleep(2)
        qPlay = pyautogui.confirm("Doriti sa dati play la melodie?")
        if qPlay == "OK":
             pyautogui.press("enter")

def searchAlbum():
    if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\album.png", confidence = 0.8) != None:
        pressTheAlbum = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\album.png", confidence = 0.8)
        pyautogui.click(pressTheAlbum)

def melodiiOnTop(url, lim = 5):
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

def extragereMelodiiAlbum(url, lim = 20):
     raspuns = requests.get(url)
     if raspuns.status_code == 200:
          soup = BeautifulSoup(raspuns.text, "html.parser")
          elementeMelodii = soup.find_all("div", class_ = "songs-list-row__song-name svelte-4hjdmk")
          infoMelodii = []
          index = 0
          for numeMelodie in elementeMelodii:
               nume = numeMelodie.get_text(strip = True)
               infoMelodii.append({"nume": nume})
               index += 1
               if(index >= lim):
                    return infoMelodii
          return infoMelodii
     else:
          print("Cerere HTTP esuata")
          return None

def scriereExcel(infoMelodii, fisier=r"C:\Users\theda\Desktop\MAP\apple music\topMelodii.xlsx"):
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

print("Pentru a cauta un artist introduceti <1>")
print("Pentru a cauta un album introduceti <2>")
print("Pentru a cauta o melodie introduceti <3>")

optiune = int(input("Raspuns: "))

if optiune == 1:
        cautare = input("Introduceti artistul pe care vreti sa-l cautati: ")
elif optiune == 2:
        cautare = input("Introduceti albumul pe care vreti sa-l cautati: ")
elif optiune == 3:
    cautare = input("Introduceti melodia pe care vreti sa o cautati: ")
else:
     print("optiune invalida")
     quit()

response = pyautogui.confirm("doriti sa rulati programul?","cautare")
if response == "OK":
    if optiune == 1:
        search(cautare)
        searchArtist()
        time.sleep(2)
        q = pyautogui.confirm("Doriti sa vedeti melodiile din top ale artistului?")
        if q == "OK":
             #if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\topSongs.png", confidence=0.7) != None:
                  #press = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\topSongs.png", confidence=0.7)
                  #pyautogui.click(press)
                  if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9) != None:
                    pressURL = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9)
                    pyautogui.click(pressURL)
                    time.sleep(2)
                    pyautogui.hotkey("ctrl", "a")
                    time.sleep(1)
                    pyautogui.hotkey("ctrl", "c")
                    url = pyperclip.paste()
                    infoMelodii = melodiiOnTop(url, lim = 5)
                    for i in infoMelodii:
                        melodie=i["nume"]
                        print("Nume melodie: ", melodie)
                    ignorare = pyautogui.confirm("Melodiile s-au afisat in terminal")
                    scriereExcel(infoMelodii)

    elif optiune == 2:
        search(cautare)
        searchAlbum()
        q = pyautogui.confirm("Doriti sa afisati melodiile din album in terminal?")
        if q == "OK":
             if pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9) != None:
                pressURL = pyautogui.locateOnScreen(r"C:\Users\theda\Desktop\MAP\apple music\url.png", confidence=0.9)
                pyautogui.click(pressURL)
                time.sleep(1)
                pyautogui.hotkey("ctrl", "a")
                time.sleep(1)
                pyautogui.hotkey("ctrl", "c")
                url = pyperclip.paste()
                infoMelodii = extragereMelodiiAlbum(url, lim = 20)
                for i in infoMelodii:
                    melodie=i["nume"]
                    print("Nume melodie: ", melodie)
    elif optiune == 3:
        search(cautare)
        searchSong()