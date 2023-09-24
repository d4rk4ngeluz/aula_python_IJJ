from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#ABRIR NAVEGADOR
navegador = Firefox()

url = "https://www.jogajuntoinstituto.org/"

#ACESSAR SITE
navegador.get(url)


form_name = navegador.find_element(By.NAME, "nome")

form_name.send_keys("Matheus")

form_email = navegador.find_element(By.NAME, "email").send_keys("mgeambastiane@gmail.com")
form_body = navegador.find_element(By.NAME, "body").send_keys("Automação com Selenium Web Driver")
form_select = navegador.find_element(By.NAME, "assunto")


select = Select(form_select)

select.select_by_visible_text("Contratar profissionais")

form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

print(form_btn)

form_btn.submit()

# resultados.click()