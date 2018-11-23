from unittest import TestCase
from selenium import webdriver

# Cargar el archivo RecursoTestFixture antes de correr los tests
# python manage.py loaddata RecursoTestFixture
class RecursoTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\\chromedriver.exe')



    def tearDown(self):
        self.browser.quit()

    def test_detalle_recurso_list(self):
        self.browser.get('http://127.0.0.1:8000/polls/recurso/list')
        self.browser.implicitly_wait(5)
        for i in (1,6):
            id = "recurso" + str(i)
            recurso = self.browser.find_element_by_id(id)
            self.assertNotEqual(None, recurso)

    def test_agregar_recurso(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('add_recurso')
        link.click()
        self.browser.implicitly_wait(3)
        titulo = self.browser.find_element_by_id('id_titulo')

        titulo.send_keys('Graficos de barras  1')
        self.browser.implicitly_wait(3)
        tipo = self.browser.find_element_by_id('id_tipo')
        tipo.send_keys('Visualizacion')
        self.browser.implicitly_wait(3)
        descripcion = self.browser.find_element_by_id('id_descripcion')
        descripcion.send_keys('Ejemplo de como realizar un grafico de barras')
        self.browser.implicitly_wait(3)
        ubicacion = self.browser.find_element_by_id('id_ubicacion')
        ubicacion.send_keys('https://github.com/jc-mojicap/PryFinalAgiles20182')
        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath("//select[@id='id_id_proyecto']/option[text()='Primero']").click()
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()


    def test_recurso_etiqueta(self):
        self.browser.get('http://127.0.0.1:8000/polls/recurso/')
        self.browser.implicitly_wait(3)
        tags = self.browser.find_element_by_id('id_etiquetas')
        sendtags = self.browser.find_element_by_class_name('select2-search__field')
        sendtags.send_keys('Graficos barras')
        self.browser.implicitly_wait(10)


