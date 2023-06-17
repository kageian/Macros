import keyboard
import time
import pyautogui
import cv2
import win32api
import win32con

#uma função para dar um click com variáveis indefinidas por ora
def click(x,y):
    #um click nas coordenadas x e y
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q')==False:
    if pyautogui.locateOnScreen('pokemon.png', confidence= 0.6) !=None:
        #movimentação do personagem no mato
        keyboard.press('left')
        time.sleep(1.5)
        keyboard.release('left')
        keyboard.press('right')
        time.sleep(1.5)
        keyboard.release('right')
        keyboard.press('down')
        time.sleep(0.01)
        keyboard.release('down')
    else:
        #caso fique com pouco hp ele irá se curar automaticamente
        if pyautogui.pixel(1100, 528)[0] == 80:
            pyautogui.moveTo(873, 595)
            click(873, 595)
            time.sleep(1)
            pyautogui.moveTo(790, 618)
            click(790, 618)
            time.sleep(1)
            pyautogui.moveTo(857, 628)
            click(857, 628)

        else:
            #isso serviu para desbugar o personagem caso o computador n reconheça ele
            time.sleep(1)
            keyboard.press('down')
            keyboard.release('down')
            keyboard.press('up')
            keyboard.release('up')

            pyautogui.moveTo(937, 663)
            click(937, 663)


            #atacar com o 3 quadrante
            if pyautogui.pixel(789,306)[1]==58:
                time.sleep(4)
                pyautogui.moveTo(743,591)
                click(743,591)
                time.sleep(1)
                pyautogui.moveTo(744,646)
                click(744,646)
                time.sleep(0.5)
                pyautogui.moveTo(937,663)
                click(937, 663)
                time.sleep(4)



