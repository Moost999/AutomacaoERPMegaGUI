import pyautogui
import time
import pygetwindow as gw

# Minimizar a janela do terminal
# Minimizar a janela ativa (o terminal)
active_window = gw.getActiveWindow()
if active_window:
    active_window.minimize()
else:
    print("Nenhuma janela ativa encontrada.")


#CLICK NO DROPDOWN PARA ABRIR OPÇOES DE PESSOAS FISICAS
pyautogui.moveTo(299, 303)
pyautogui.click()
pyautogui.click()
pyautogui.click()
#SELECIONAR PESSOA FISICA
pyautogui.moveTo(220, 320)
pyautogui.click()
time.sleep(2)
#click para inserir o cpf
pyautogui.moveTo(322, 302)
pyautogui.click()
time.sleep(2)

pyautogui.typewrite("56388324835")
pyautogui.press('enter')

#move se para preenchero nome na abas (AGENTES)

pyautogui.moveTo(203, 340)
pyautogui.click()
pyautogui.typewrite("JOAO VITOR GIONDA")
pyautogui.press('enter')

time.sleep(2)

#trocar de aba (DADOS DE CONTATO)
pyautogui.moveTo(264, 260)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('jvgionda@hotmail.com') # INSIRA O EMAIL

time.sleep(2)

pyautogui.moveTo(474, 232)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('jvgionda@hotmail.com')
time.sleep(2)

pyautogui.moveTo(734, 229)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('jvgionda@hotmail.com')
time.sleep(2)
pyautogui.moveTo(533, 279)
time.sleep(2)

#troca de aba endereçamentos

pyautogui.moveTo(303, 162)
pyautogui.click()

pyautogui.moveTo(591, 202)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('05001200') # INSERE O CEP DO ALLIANZ, Avenida Francisco Mattarazo 1705.

time.sleep(2)

#click numero de endereço
pyautogui.moveTo(186, 344)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('1705') # INSERE O NUMERO 1705 
time.sleep(2)
pyautogui.moveTo(271, 337)
pyautogui.click()
time.sleep(2)
pyautogui.click()
pyautogui.typewrite('ANDAR 1 SALA 7')

#trocar de aba pessoa fisica
pyautogui.moveTo(382, 159)
pyautogui.click()
pyautogui.click()
time.sleep(2)

pyautogui.moveTo(190, 235)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite("Joao Vitor Gionda") # INSERE O NOME DO FUNCIONARIO
time.sleep(2)

pyautogui.moveTo(190, 330)
pyautogui.click()
pyautogui.typewrite('PlaceHolder Mae') # Insere o Nome Da Mãe, caso nao precise apague ate a linha 91
time.sleep(2)

# Troca Para Aba Colaborador

pyautogui.moveTo(483, 154)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(189, 292)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('10') # CADASTRA CENTRO DE CUSTO
time.sleep(2)

pyautogui.moveTo(620, 293)
pyautogui.click()
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('1') # INSERE O NUMERO DA ORGANIZAÇÂO
time.sleep(2)
pyautogui.moveTo(181, 341)
pyautogui.click()
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('1033')# INSERE A THAIS COMO GESTOR RESPONSAVEL
pyautogui.press('enter')

time.sleep(2)

# FINALIZAR E SALVAR

pyautogui.moveTo(1183, 670)
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.tripleClick()
pyautogui.click()
pyautogui.moveTo(1037, 668)
pyautogui.click()
