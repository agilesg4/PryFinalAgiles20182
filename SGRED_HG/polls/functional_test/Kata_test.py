import csv
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class Kata_test(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:\\chromedriver.exe')


    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('SGRED', self.browser.title)

    def test_detalle_actividad(self):
        self.browser.get('http://127.0.0.1:8000/listar_actividades/1/')
        titulo = self.browser.find_element_by_id("tituloactividad")
        self.assertIn("Actividad 1", titulo.text)

    def test_servicio_detalle_actividad(self):
        self.browser.get('http://127.0.0.1:8000/rest_actividades_id/1')
        texto = self.browser.find_element_by_xpath("//*[contains(text(), '\"nombre\": \"Actividad 1\"')]")
        self.assertIn("Actividad 1", texto.text)
        try:
            texto2 = self.browser.find_element_by_xpath("//*[contains(text(), '\"nombre\": \"Actividad 2\"')]")
        except:
            texto2 = "prueba"
        self.assertNotIn("Actividad 2", texto2)

    def test_detalle_actividad_2(self):
        self.browser.get('http://127.0.0.1:8000/listar_actividades/1/')
        nombre = self.browser.find_element_by_id("tituloactividad")
        self.assertIn("Actividad 1", nombre.text)
        descripcion = self.browser.find_element_by_id("descripcion")
        self.assertIn("Descripcion Actividad 1", descripcion.text)
        tipoact = self.browser.find_element_by_id("tipoactividad")
        self.assertNotIn(None, tipoact.text)
        idfase = self.browser.find_element_by_id("fase")
        self.assertNotIn(None, idfase.text)
        periodicidad = self.browser.find_element_by_id("periodicidad")
        self.assertIn("Diario", periodicidad.text)
        fecha_inicio = self.browser.find_element_by_id("fechainicio")
        self.assertNotIn(None, fecha_inicio)


