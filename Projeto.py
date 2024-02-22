# 1 passo: importar as bibliotecas
import pyautogui  
import time
import pandas as pd

# 2 passo: ler a tabela

tabela = pd.read_csv("produtos.csv")
print(tabela)

# 3 passo: entrar no site

pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")
time.sleep(6)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press("enter")

# 4 passo: logar no site
time.sleep(3)
pyautogui.click(x=438, y=385)

pyautogui.write("gabrielrodrigues@gmail.com")

time.sleep(3)
pyautogui.press("tab")
pyautogui.write("lalala")
time.sleep(3)
pyautogui.press("enter")

# 5 passo: cadastrar os produtos


for linha in tabela.index:
    
    time.sleep(3)
    pyautogui.click(x=332, y=293)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    time.sleep(4)
    pyautogui.press('tab')


    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')
    
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.scroll(200)      