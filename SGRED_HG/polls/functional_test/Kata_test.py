import csv
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class Kata_test(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('D://chromedriver.exe')


    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('SGRED', self.browser.title)

    def test_detalle_actividad(self):
        self.browser.get('http://127.0.0.1:8000/listar_actividades/1/verActividad')
        titulo = self.browser.find_element_by_css_selector("h4")
        self.assertIn("Actividad 1", titulo.text)
