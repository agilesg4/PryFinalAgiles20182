from unittest import TestCase
from selenium import webdriver

# Cargar el archivo RecursoTestFixture antes de correr los tests
# python manage.py loaddata RecursoTestFixture
class RecursoTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_detalle_recurso_artefactos(self):
        self.browser.get('http://127.0.0.1:8000/polls/recursos/1')
        self.browser.implicitly_wait(5)
        btn_add_artefacto = self.browser.find_element_by_id("btn_add_artefacto")
        artefacto_list = self.browser.find_element_by_id("artefacto_list")
        self.assertIsNotNone(btn_add_artefacto.text)
        self.assertEqual("Agregar Nuevo Artefacto", btn_add_artefacto.text)
        self.assertIsNotNone(artefacto_list.is_displayed())
        self.assertEqual(True, artefacto_list.is_displayed())
        self.assertIsNotNone(artefacto_list.find_elements_by_class_name("artefacto_card"))
