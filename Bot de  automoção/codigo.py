# pip install 
import pyautogui
import time

#sistema: https://dlp.hasthagtreinamentos.com/python/intensivao/login
#Passo 1: abrir o sistema da empresa
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=774, y=314)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")

#Passo 2: Fazer login
time.sleep(3)
pyautogui.click(x=465, y=379)

pyautogui.write("marcelonasantos.27@gmail.com")
pyautogui.press("tab")
pyautogui.write("010203")
pyautogui.press("enter")

#Passo 3: importar a base de dados dos produtos
import pandas as pd

tabela = pd.read_csv(r"C:\Users\Cliente\Desktop\Marcelo imersão\Jornada Pyton\Bot de  automoção\produtos.csv")

print(tabela)

time.sleep(2)

#Passo 4: cadastrar 1 produto

for linha in tabela.index:

    pyautogui.click(x=785, y=258)

    # Código
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    time.sleep(0.5)

    # Marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    time.sleep(0.5)

    # Tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    time.sleep(0.5)

    # Categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria)) # str -> string = texto
    pyautogui.press("tab")
    time.sleep(0.5)

    # Preço_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    time.sleep(0.5)

    # Custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    time.sleep(0.5)

    # Obs
    obs = str(tabela.loc[linha,"obs"])


    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.press("enter")
    pyautogui.scroll(10000)

#Passo 5: repetir o passo 4 até acabar todos os produtos



