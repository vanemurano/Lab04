import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary() #il multidictionary è il nostro modello
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self, e):
        self._view._lvOut.controls.clear()
        inputFrase=self._view._txtInFrase.value
        lingua=self._view._dropDownLanguage.value
        modalità=self._view._dropDownModality.value
        if inputFrase=="":
            self._view._lvOut.controls.append(ft.Text("Devi inserire una frase!", color="red"))
            self._view.update()
            return
        for c in inputFrase:
            if c.isdigit():
                self._view._lvOut.controls.append(ft.Text("La frase non deve contenere numeri!", color="red"))
                self._view.update()
                return
        if lingua=="":
            self._view._lvOut.controls.append(ft.Text("Devi scegliere una lingua!", color="red"))
            self._view.update()
            return
        if modalità=="":
            self._view._lvOut.controls.append(ft.Text("Devi scegliere una modalità!", color="red"))
            self._view.update()
            return
        self._view._lvOut.controls.append(ft.Text(f"Frase inserita: \n{inputFrase}"))
        #se non imposto il colore, viene impostato automaticamente nero
        parole_prova, tempo=self.handleSentence(inputFrase, lingua, modalità)
        parole=replaceChars(parole_prova).split()
        if not parole: #se la lista parole è vuota
            self._view._lvOut.controls.append(ft.Text("La frase è corretta!", color="green"))
        else:
            lista=ft.Text("Parole errate: \n", color="blue")
            self._view._lvOut.controls.append(lista)
            for p in parole:
                lista.value+=f"{p} " #aggiungo stringhe al ft.Text già esistente
        self._view._lvOut.controls.append(ft.Text(f"Tempo impiegato per la correzione: \n{tempo}"))
        self._view._txtInFrase.value=""
        self._view._dropDownLanguage.value=""
        self._view._dropDownModality.value="" #ripulisco i campi dopo la ricerca
        self._view.update()
        return



def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text