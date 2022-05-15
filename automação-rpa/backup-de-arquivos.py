import pyautogui
import time
# automatizar um backup
#primeiro passo, anotar como o processo é feiito manualmente:
pyautogui.alert("o codigo vai começar, ao mexa em nada")
# entrar na área de trabalho,
pyautogui.hotkey('winleft', 'd')
# abrir o google drive
pyautogui.moveTo(609, y=39)
pyautogui.doubleClick()
time.sleep(2)
# pegar o arquivo
pyautogui.moveTo(x=1078, y=240)
pyautogui.mouseDown()
#  arrastar para o google drive
pyautogui.moveTo(x=721, y=367)
pyautogui.mouseUp()
time.sleep(1.5)
pyautogui.alert("acabou")
