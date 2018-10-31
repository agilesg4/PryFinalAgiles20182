import csv
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class kata_prueba_funcional(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('D:/chromedriver.exe')


    def tearDown(self):
        self.browser.quit()

    def test_ver_detalle_actividad(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('listar_actividades')
        link.click()
        self.browser.implicitly_wait(3)
        texto = self.browser.find_element_by_xpath("//*[contains(text(), 'Actividad 1')]")
        self.assertIn("Actividad 1", texto.text)