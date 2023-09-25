# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# import os
# import urllib3

# #espera aparecer o elemento que tem o id de "side", aguardo de leitura do QR.
# navegador = webdriver.Firefox()
# navegador.get("https://web.whatsapp.com/")

# #while len(navegador.find_elements_by_id("side")) < 1:

# sleep:(1)

# # já estamos com o login feito no whatsapp web.
# tabela = pd.read_excel(f"Enviar.xlsx")
# # DisplayStyle(tabela=[['contato', 'mensagem']])
# print(tabela)

# # enviar uma mensagem para a pessoa


# for linha in tabela.index:
#     contato = tabela.loc[linha, 'contato']
#     telefone = tabela.loc[linha, 'telefone']
#     mensagem = tabela.loc[linha, 'mensagem']
   
#     texto = mensagem.replace("fulano", contato)
#     texto =  urllib3.parse.quote(texto)
# #enviar a mensagem   
#     link= f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    
#     navegador.get(link)
    
# #   while len(navegador.find_elements_by_id("side")) < 1:
# sleep:(1)
# #no espaço que digita a mensagem, faz um xpath e copia para colar entre as chaves e aspas 
# navegador.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/sp')
# sleep:(10)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
import os
import urllib

#espera aparecer o elemento que tem o id de "side", aguardo de leitura do QR.
navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com/")

time.sleep(1)

# já estamos com o login feito no whatsapp web.
tabela = pd.read_excel(f"Enviar.xlsx")
print(tabela)

# enviar uma mensagem para a pessoa
for linha in tabela.index:
    contato = tabela.loc[linha, 'contato']
    # telefone = tabela.loc[linha, 'telefone']
    mensagem = tabela.loc[linha, 'mensagem']
   
    texto = mensagem.replace("fulano", contato)
    texto =  urllib.parse.quote(texto)
    link= f"https://web.whatsapp.com/send?phone={contato}&text={texto}"
    
    navegador.get(link)
    
    time.sleep(1)
    element = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/sp'))
)
    # Fazer algo com o elemento aqui, por exemplo:
    # element.send_keys(Keys.RETURN)
    
time.sleep(10)
