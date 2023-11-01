import requests
from bs4 import BeautifulSoup
import openpyxl

def extrage_informatii_produse(url, limita=5):
    raspuns= requests.get(url)

    if raspuns.status_code == 200 :
        soup= BeautifulSoup(raspuns.text, "html.parser")
        elemente_nume=soup.find_all("a", class_="font-bold d-block mt-md-2 mb-1")
        elemente_pret= soup.find_all("div", class_="real-price font-bold")

        informatii_produse=[]

        index=0
        for nume_element, pret_element in zip(elemente_nume,elemente_pret):
            nume=nume_element.get_text(strip=True)
            pret=pret_element.find("span").get_text(strip=True)
            informatii_produse.append({"nume":nume,"pret":pret})

            index+=1

            if(index>=limita):
                return informatii_produse
        return informatii_produse
    else:
        print("Cerere HTTP a esuat.Cod de stare:",raspuns.status_code)
        return None
    
url="https://flip.ro/magazin/apple/iphone-14/"

informatii_produse=extrage_informatii_produse(url, limita=5)
for i in informatii_produse:
    nume_produs=i["nume"]
    pret=format(round(float(i["pret"])*1000))
    print("Nume produs:",nume_produs)
    print("Pret:",pret)

def scriere(informatii_produse, fisier=r"C:\Users\theda\Desktop\MAP\lab4.xlsx"):
    if informatii_produse:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Produse"

        sheet["A1"] = "Nume Produs"
        sheet["B1"] = "Capacitate"
        sheet["C1"] = "Culoare"
        sheet["D1"] = "Pret"

        row=2
        for produs in informatii_produse:
            nume_produs = produs["nume"].split("\n")
            if len(nume_produs) == 3:
                nume, capacitate, culoare = nume_produs
                sheet[f"A{row}"] = f"{nume}"
                sheet[f"B{row}"] = f"{capacitate}"
                sheet[f"C{row}"] = f"{culoare}"
                sheet[f"D{row}"] = f"{pret}"
            else:
                sheet[f"A{row}"] = "Nume produs: " + nume_produs[0]
                sheet[f"B{row}"] = "Capacitate N/A"
                sheet[f"C{row}"] = "Culoare N/A"
                sheet[f"D{row}"] = f"Pret: {produs['pret']}"
            row+=1
        workbook.save("lab4.xlsx")
        print (f"Fisier salvat cu succes")
    else:
        print("Nu s-au gasit info despre produse")
scriere(informatii_produse)