import pyautogui
import pyperclip
import time

# Lista de coordenadas (substitua pelos seus valores)
click_positions = [
    (506, 356),  # Coordenada do primeiro clique
    (472, 400),  # Coordenada do segundo clique
    (807, 470),  # Coordenada para validar a opção do texto
]

# Lista de textos para o primeiro clique
first_texts = [
    "10011", "10021", "10031", "10041", "10051",
    "10061", "10071", "10081", "10091", "10101",
    "10111", "10121", "10131", "10141", "10151",
    "10161", "10171", "10181", "10191", "10201",
    "10211", "10221", "10231", "10241", "10251",
    "10261", "10271", "10281", "10291", "10301",
    "10311", "10321", "10331", "10341", "10351",
    "10361", "10371", "10381", "10391", "10401",
    "10411", "10421", "10431", "10441", "10451",
    "10461", "10471", "10481", "10491", "10501",
    "10511", "10521", "10531", "10541", "10551",
    "10561", "10571", "10581",
]

# Texto fixo para o segundo clique
second_text = "Perfil Fiscal/Contábil - Orçamentos"

# Número de iterações com base no comprimento da lista de primeiros textos
num_iterations = len(first_texts)

# Loop para repetir o processo
for iteration in range(num_iterations):
    print(f"Iniciando iteração {iteration + 1} de {num_iterations}.")

    # Primeiro clique: abre o dropdown
    pyautogui.click(click_positions[0])
    time.sleep(2)  # Espera 2 segundos

    # Digita o texto da lista
    pyautogui.write(first_texts[iteration])
    pyautogui.press('enter')  # Pressiona Enter após digitar
    time.sleep(2)  # Espera 2 segundos

    # Segundo clique: campo para o texto fixo
    pyautogui.click(click_positions[1])
    time.sleep(1)  # Espera 1 segundo

    # Copia o texto fixo para a área de transferência
    pyperclip.copy(second_text)
    time.sleep(1)  # Espera 1 segundo para garantir que o texto foi copiado

    # Cola o texto fixo
    pyautogui.hotkey('ctrl', 'v')  # Cola o texto fixo
    pyautogui.press('enter');
    time.sleep(1)  # Espera 1 segundo

    # Clique para validar a opção do texto
    pyautogui.click(click_positions[2])  # Clica na coordenada de validação
    time.sleep(2)  # Espera 2 segundos

print("Processo concluído.")
