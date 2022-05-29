# -*- coding: utf-8 -*-
from app import app
from flask_wtf.csrf import CSRFProtect
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test__CSRFProtect(self):
        self.csrf = CSRFProtect(app.csrf)

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(app.pagina_inicial, "Grupo 22 4Winds\n1-Danilo Caporal\n2-Gicele Castro\n3-Jeremias Oliveira\n4-Rodrigo Pestana")