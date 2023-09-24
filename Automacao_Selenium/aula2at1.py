# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from time import sleep

# navegador = Firefox()

# link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

# navegador.get(link)

# adicionar = navegador.find_element(By.ID, "addElement")

# contador = 0
# while contador <= 10:

#     adicionar.click()
#     contador += 1

# checkboxes = navegador.find_elements(By.TAG_NAME, "input")


# for checkbox in checkboxes:
    
#     checkbox.click()

# sleep(5)
# navegador.quit()

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = Firefox()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

navegador.get(link)

adicionar = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "addElement")))

for _ in range(10):
    adicionar.click()

checkboxes = WebDriverWait(navegador, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))

for checkbox in checkboxes:
    checkbox.click()

input("Pressione Enter para fechar o navegador")

navegador.quit()
