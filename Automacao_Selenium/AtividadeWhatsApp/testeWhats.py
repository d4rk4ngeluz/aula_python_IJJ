from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import mouse



# Inicializando o navegador
navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com/")

# Fazendo login no WhatsApp Web
input("Tecle ENTER após a leitura do QRCode!")
print("Automação em andamento! Favor aguardar!")

# Alternando para a próxima aba
body = navegador.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.ALT, Keys.TAB)
sleep(3)

# Pesquisando pelo grupo
grupo_nome = "[3] IJJ - BUGOU? QA TÁ ON!"
from selenium.webdriver.common.by import By

campo_pesquisa = navegador.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
campo_pesquisa.send_keys(grupo_nome)
sleep(3)

# Selecionando o grupo nos resultados da pesquisa
resultado_grupo = navegador.find_element(By.XPATH, f"//span[@title='{grupo_nome}']")
resultado_grupo.click()
sleep(5)

mensagem = "Teste automatizado de envio de mensagens para o WhatsApp *Squad Orion* Renato, Katie, Ester e Josie! *Código* *2*!"
campo_mensagem = navegador.find_element(By.CSS_SELECTOR, "._3Uu1_ > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)")
ActionChains(navegador).move_to_element(campo_mensagem).click(campo_mensagem).send_keys(mensagem).perform()
buton_send = navegador.find_element(By.CSS_SELECTOR, "button.tvf2evcx").click()
print("Mensagem enviada com Sucesso, agora é só correr para o abraço!!")

sleep(10)

# Fechando o navegador
navegador.quit()
