from pickle import TRUE
from time import sleep
import this
from tkinter.messagebox import NO
import pyautogui
import keyboard  

class Pescador:

    posicaoPokePescado = (1739,310)
    posicaoMar = (953,682)
    
    def inicia():
        Pescador.cumprimenta()
        Pescador.pesca()
        Pescador.atacaPokemons()
            
            
    def atacaPokemons():
        pyautogui.click(Pescador.posicaoPokePescado)
        keyboard.press_and_release('F1')
        sleep(0.1)
        keyboard.press_and_release('F2')
        sleep(0.1)
        keyboard.press_and_release('F3')
        sleep(0.1)
        keyboard.press_and_release('F4')
        sleep(0.1)
        keyboard.press_and_release('F5')
        sleep(0.1)
        keyboard.press_and_release('F6')
        sleep(0.1)
        keyboard.press_and_release('F7')
        sleep(0.1)
        keyboard.press_and_release('F8')
        sleep(0.1)
        keyboard.press_and_release('F9')
        sleep(0.1)
        keyboard.press_and_release('F10')
    def pesca():
        posicaoVara = Pescador.buscaVara()
        if (posicaoVara != None):
            pyautogui.click(posicaoVara)
            pyautogui.click(Pescador.posicaoMar)
            print("anzol no mar, aguardando peixe fisgar.")
            while (Pescador.buscaPeixeVerde() == None):
                sleep(0.1)
            print("o peixe fisgou!")
            pyautogui.click(Pescador.buscaPeixeVerde())
            print("o peixe ta por ai")
        else:
            print("vara nao encontrada.")
    
    
    def posicaoDoMouse():
        pyautogui.displayMousePosition()

    def cumprimenta():
        print('oi')
    
    def buscaVara():
        return pyautogui.locateOnScreen('./public/rod.png', grayscale=True)

    def buscaKrab():
        return pyautogui.locateOnScreen('./public/krab.png', grayscale=True)
    def buscaCarvanha():
        return pyautogui.locateOnScreen('./public/carvanha.png', grayscale=True)
    
    def buscaPeixeVerde():
        return pyautogui.locateOnScreen('./public/peixe-verde.png', grayscale=True)
    
    def buscaLinhaBranca():
        return pyautogui.locateOnScreen('./public/linha-branca.png', grayscale=False)
    

    def clicaNaVara():
        print("oi")
            
    