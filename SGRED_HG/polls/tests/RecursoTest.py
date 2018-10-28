from unittest import TestCase
from selenium import webdriver

# Cargar el archivo RecursoTestFixture antes de correr los tests
# python manage.py loaddata RecursoTestFixture
class RecursoTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_detalle_recurso_list(self):
        self.browser.get('http://127.0.0.1:8000/polls/recurso/list')
        self.browser.implicitly_wait(5)
        for i in (1,6):
            id = "recurso" + str(i)
            recurso = self.browser.find_element_by_id(id)
            self.assertNotEqual(None, recurso)

    def test_detalle_recurso_con_ubicacion(self):
        self.browser.get('http://127.0.0.1:8000/polls/recurso/list')
        self.browser.implicitly_wait(5)
        recurso = self.browser.find_element_by_id("recurso3")
        recurso.click()
        self.browser.implicitly_wait(5)
        titulo = self.browser.find_element_by_id("recurso_titulo")
        tipo = self.browser.find_element_by_id("recurso_tipo_select")
        descripcion = self.browser.find_element_by_id("recurso_descripcion")
        ubicacion = self.browser.find_element_by_id("load_file_name_input")
        cargar_button = self.browser.find_element_by_id("file_dialog_button")
        self.assertEqual("Tercero", titulo.get_attribute("value"))
        self.assertEqual("true", titulo.get_attribute("disabled"))
        self.assertEqual("3", tipo.get_attribute("value"))
        self.assertEqual("true", tipo.get_attribute("disabled"))
        self.assertEqual("Test", descripcion.get_attribute("value"))
        self.assertEqual("true", descripcion.get_attribute("disabled"))
        self.assertEqual("documento.docx", ubicacion.get_attribute("value"))
        self.assertEqual("true", ubicacion.get_attribute("disabled"))
        self.assertEqual("hidden", cargar_button.value_of_css_property("visibility"))

    def test_detalle_recurso_sin_ubicacion(self):
        self.browser.get('http://127.0.0.1:8000/polls/recurso/list')
        self.browser.implicitly_wait(5)
        recurso = self.browser.find_element_by_id("recurso1")
        recurso.click()
        self.browser.implicitly_wait(5)
        titulo = self.browser.find_element_by_id("recurso_titulo")
        tipo = self.browser.find_element_by_id("recurso_tipo_select")
        descripcion = self.browser.find_element_by_id("recurso_descripcion")
        ubicacion = self.browser.find_element_by_id("load_file_name_input")
        cargar_button = self.browser.find_element_by_id("file_dialog_button")
        self.assertEqual("Prueba", titulo.get_attribute("value"))
        self.assertEqual("true", titulo.get_attribute("disabled"))
        self.assertEqual("2", tipo.get_attribute("value"))
        self.assertEqual("true", tipo.get_attribute("disabled"))
        self.assertEqual("Test", descripcion.get_attribute("value"))
        self.assertEqual("true", descripcion.get_attribute("disabled"))
        self.assertEqual("", ubicacion.get_attribute("value"))
        self.assertEqual(None, ubicacion.get_attribute("disabled"))
        self.assertEqual("visible", cargar_button.value_of_css_property("visibility"))

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