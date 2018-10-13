import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:/chromedriver.exe')


    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('SGRED', self.browser.title)

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
        self.browser.find_element_by_xpath("//select[@id='id_id_proyecto']/option[text()='Web']").click()
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()


