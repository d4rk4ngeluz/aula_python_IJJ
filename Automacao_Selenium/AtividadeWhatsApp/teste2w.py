from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import time
import mouse

def main():
    navegador = Firefox()
    navegador.get("https://web.whatsapp.com/")

    input("Tecle ENTER após a leitura do QRCode!")
    print("Automação em andamento! Favor aguardar!")

    _switch_to_browser_tab()

    grupo_nome = "[3] IJJ - BUGOU? QA TÁ ON!"
    pesquisar_contato(navegador, grupo_nome)

    resultado_grupo = navegador.find_element(By.XPATH, f"//span[@title='{grupo_nome}']")
    resultado_grupo.click()

    sleep(3)

    mensagem = "Teste automatizado de envio de mensagens para o WhatsApp *Squad Orion* Renato, Katie, Ester e Josie! *Codigo* *1*"

    _send_message(mensagem)

    sleep(3)

    navegador.quit()

def _switch_to_browser_tab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    sleep(3)

def pesquisar_contato(navegador, nome_contato):
    campo_pesquisa = navegador.find_element(
        By.XPATH, "//div[@contenteditable='true']")
    campo_pesquisa.send_keys(nome_contato)
    sleep(3)

def _send_message(mensagem):
    mouse.move(690, 900, absolute=True, duration=0.1)
    mouse.click('left')
    time.sleep(1)

    pyautogui.write(mensagem)
    pyautogui.press('enter')

if __name__ == "__main__":
    main()