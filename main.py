import unittest
from datetime import datetime
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AsteriskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_and_reserve(self):
        driver = self.driver
        driver.get('https://bookings-asterisk.000webhostapp.com/')
        driver.save_screenshot('capturas/captura_1.png')

        # Log in
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login_btn"))
        )
        signin_button.click()
        driver.save_screenshot('capturas/captura_2.png')

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "emailUserLogin"))
        )
        username_input.send_keys('gartza.io@gmail.com')
        driver.save_screenshot('capturas/captura_3.png')

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "passUserLogin"))
        )
        password_input.send_keys('geronimo')
        driver.save_screenshot('capturas/captura_4.png')

        signin_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submitUserLogin"))
        )
        signin_submit_button.click()
        driver.save_screenshot('capturas/captura_5.png')

        # tap on the reserve button to open the reserve popup
        book_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bookUp"))
        )
        book_button.click()
        driver.save_screenshot('capturas/captura_6.png')

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        name_input.send_keys('Prueba Geronimo')
        driver.save_screenshot('capturas/captura_7.png')

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys('gartza.io@gmail.com')
        driver.save_screenshot('capturas/captura_8.png')

        date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "date"))
        )
        date_input.send_keys('05082023')
        driver.save_screenshot('capturas/captura_9.png')

        time_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "time"))
        )
        time_input.send_keys('0852AM')
        driver.save_screenshot('capturas/captura_10.png')

        reserve_attempt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bookBtn"))
        )
        reserve_attempt.click()
        driver.save_screenshot('capturas/captura_11.png')

        go_back = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "go_back"))
        )
        go_back.click()
        driver.save_screenshot('capturas/captura_12.png')

        # logout de la página
        open_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "profile_btn"))
        )
        open_menu.click()
        driver.save_screenshot('capturas/captura_13.png')

        # logout attempt
        logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "logout"))
        )
        logout.click()
        driver.save_screenshot('capturas/captura_14.png')


if __name__ == '__main__':
    # Crea un objeto TestSuite y agrega la clase de prueba a la misma
    suite = unittest.TestSuite()
    suite.addTest(AsteriskTestCase('test_login_and_reserve'))

    # Abre el archivo de informe en modo de escritura
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_name = f'asterisk_report_{now}.html'
    f = open(report_name, 'w')

    # Configura los parámetros del corredor HTML
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='Asterisk Bookings Test Report', description='Pruebas de automatización en Asterisk Bookings')

    # Ejecuta la suite de pruebas y genera el reporte HTML
    runner.run(suite)

    # Cierra el archivo de informe
    f.close()

    # Abre el archivo de informe en modo de lectura
    f = open(report_name, 'r')
    report_content = f.read()
    f.close()

    # Agrega el enlace a la hoja de estilo en la cadena generada
    report_content = report_content.replace('<head>', '<head><link rel="stylesheet" type="text/css" href="styles.css">')

    # Guarda la cadena generada en el archivo de informe
    f = open(report_name, 'w')
    f.write(report_content)
    f.close()

