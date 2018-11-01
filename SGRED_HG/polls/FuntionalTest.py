import csv
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('D:/chromedriver.exe')


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
        # Debe existir un proyecto Web
        self.browser.find_element_by_xpath("//select[@id='id_id_proyecto']/option[text()='Web']").click()
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

    # Caso en el que un proyecto no tiene recursos
    def test_ver_recursos_proyecto(self):
        self.browser.get('http://127.0.0.1:8000/polls/proyectos/1')
        titulo = self.browser.find_element_by_css_selector("h4")
        boton = self.browser.find_element_by_class_name("agregar_recurso")
        self.assertIn("Recursos", titulo.text)
        self.assertIn("Agregar Nuevo Recurso", boton.text)

    def generate_file(self):
        try:
            myfile = open('test.csv', 'wb')
            wr = csv.writer(myfile)
            wr.writerow(('Paper ID', 'Paper Title', 'Authors'))
            wr.writerow(('1', 'Title1', 'Author1'))
            wr.writerow(('2', 'Title2', 'Author2'))
            wr.writerow(('3', 'Title3', 'Author3'))
        finally:
            myfile.close()

        return myfile
    
    def test_agregar_artefacto(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('add_artefacto')
        link.click()
        self.browser.implicitly_wait(3)

        titulo = self.browser.find_element_by_id('nombre_mostrar')
        titulo.send_keys('prueba artefacto 1')
        descripcion = self.browser.find_element_by_id('descripcion')
        descripcion.send_keys('descripcion')
        tipo_artefacto = self.browser.find_element_by_id('tipo_artefacto')
        # HTML debe existir previamente en la base de datos.
        tipo_artefacto.send_keys('HTML')
        recurso = self.browser.find_element_by_id('recurso')
        recurso.send_keys('Graficos de barras  1')
        archivo = self.browser.find_element_by_id('archivo')

        myfile = self.generate_file()
        file_path = os.path.abspath(myfile.name)
        archivo.send_keys(file_path)
        self.browser.implicitly_wait(5)
        botonGrabar = self.browser.find_element_by_id('grabar')
        botonGrabar.click()

    def test_listar_actividades(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('listar_actividades')
        link.click()
        self.browser.implicitly_wait(3)
        texto = self.browser.find_element_by_xpath("//*[contains(text(), 'Actividad 1')]")
        self.assertIn("Actividad 1", texto.text)

    def test_login_usuario(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('logIn')
        link.click()

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('dazak')

        contrasena = self.browser.find_element_by_id('password')
        contrasena.send_keys('Password123')

        botonAceptar = self.browser.find_element_by_id('aceptar')
        botonAceptar.click()

        self.browser.implicitly_wait(3)

        span = self.browser.find_element_by_id('userlogged')

        self.assertIn('dazak', span.text)





