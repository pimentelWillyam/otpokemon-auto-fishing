import pyautogui
import keyboard  
import mouse
from time import sleep




class PescadorAutomatico:

    posicaoVara = None
    posicaoPokePescado = (1738,307)
    posicaoMar = (968,708)
    posicaoPeixeVerde = None
    
    def inicia():
        while keyboard.is_pressed('space') == False:
            PescadorAutomatico.pesca()
            PescadorAutomatico.SelecionaPokemon()
            PescadorAutomatico.ataca()
            #PescadorAutomatico.SelecionaPokemon()
            #while (PescadorAutomatico.existePokemonSelecionado()): 
                #PescadorAutomatico.ataca()
            #if (PescadorAutomatico.existePokemonSelecionado()):
                #PescadorAutomatico.ataca()
                #print("existe")
            #else:
                #print("nao existe")
                #PescadorAutomatico.SelecionaPokemon()
                #PescadorAutomatico.ataca()

    def pesca():
        PescadorAutomatico.posicaoVara = PescadorAutomatico.buscaVara() 
        if (PescadorAutomatico.buscaVara() == None):
            print("erro na hora de achar a vara")
            return
        mouse.move(PescadorAutomatico.posicaoVara[0],PescadorAutomatico.posicaoVara[1], duration=0.1)
        mouse.click()
        mouse.move(PescadorAutomatico.posicaoMar[0],PescadorAutomatico.posicaoMar[1], duration=0.1)
        mouse.click()
        print("anzol no mar, aguardando peixe fisgar.")
        PescadorAutomatico.posicaoPeixeVerde = PescadorAutomatico.buscaPeixeVerde()
        while (PescadorAutomatico.posicaoPeixeVerde == None):
            #if (PescadorAutomatico.existePokemonSelecionado()):
                #PescadorAutomatico.ataca()
                sleep(0.1)
                PescadorAutomatico.posicaoPeixeVerde = PescadorAutomatico.buscaPeixeVerde()
        print("o peixe fisgou!")
        mouse.move(PescadorAutomatico.posicaoPeixeVerde[0],PescadorAutomatico.posicaoPeixeVerde[1], duration = 0.1)
        mouse.click()
        #PescadorAutomatico.SelecionaPokemon()
        print("o peixe ta por ai") 
        
            
    def ataca():
        keyboard.press_and_release('F1')
        keyboard.press_and_release('F2')
        sleep(0.1)
        keyboard.press_and_release('F3')
        keyboard.press_and_release('F4')
        sleep(0.1)
        keyboard.press_and_release('F5')
        keyboard.press_and_release('F6')
        sleep(0.1)
        keyboard.press_and_release('F7')
        keyboard.press_and_release('F8')
        sleep(0.1)
        keyboard.press_and_release('F9')
        keyboard.press_and_release('F10')
        sleep(0.1)

    

    def posicaoDoMouse():
        pyautogui.displayMousePosition()

    def existePokemonSelecionado():
        if (PescadorAutomatico.buscaPokemonSelecionado() == None):
            return False
        else:
            return True
    def SelecionaPokemon():
        mouse.move(PescadorAutomatico.posicaoPokePescado[0],PescadorAutomatico.posicaoPokePescado[1], duration = 0.6)
        mouse.click()
    
    def buscaVara():
        return pyautogui.locateOnScreen('./public/vara.png', grayscale=False)

    def buscaKrab():
        return pyautogui.locateOnScreen('./public/krab.png', grayscale=True, confidence = 0.9)

    def buscaCarvanha():
        return pyautogui.locateOnScreen('./public/carvanha.png', grayscale=True, confidence = 0.9)

    def buscaPeixeVerde():
        return pyautogui.locateOnScreen('./public/peixe-verde.png', grayscale=False)
    
    def buscaLinhaBranca():
        return pyautogui.locateOnScreen('./public/linha-branca.png', grayscale=True, confidence = 0.9)

    def buscaTangela():
        return pyautogui.locateOnScreen('./public/tangela.png', grayscale=True, confidence = 0.9)

    def buscaPokemonSelecionado():
        return pyautogui.locateOnScreen('./public/pokemon-selecionado.png', grayscale=False, confidence = 0.9)
    

    def buscaPokemonNaoSelecionado():
        return pyautogui.locateOnScreen('./public/pokemon-nao-selecionado.png', grayscale=False, confidence = 0.9)
            
    