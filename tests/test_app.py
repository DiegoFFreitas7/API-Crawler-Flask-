import sys
sys.path.append("../")

import unittest
import requests
import ast

#url = 'http://localhost:5000'
url = 'http://127.0.0.1:5000'

class Test_Conexao(unittest.TestCase):
    '''
    Testa os status das conexoes do app
    '''

    def test_conexoes_01(self):
        r = requests.get(url + '/crawler', json={})
        self.assertEqual(r.status_code, 400)

    def test_conexoes_02(self):
        r = requests.get(url + '/sobre')
        self.assertEqual(r.status_code, 200)

    def test_conexoes_03(self):
        r = requests.get(url + '/')
        self.assertEqual(r.status_code, 200)

    def test_conexoes_04(self):
        r = requests.get(url + '/autoTest01')
        self.assertEqual(r.status_code, 200)

    def test_conexoes_05(self):
        r = requests.get(url + '/autoTest02')
        self.assertEqual(r.status_code, 200)

    def test_conexoes_06(self):
        r = requests.get(url + '/autoTest03')
        self.assertEqual(r.status_code, 200)


class Teste_app(unittest.TestCase):
    '''
    Testa as respota das URLs '/crawler'
    '''

    def test_crawler_01(self):
        # Faz a requisicao
        r = requests.get(url + '/crawler', json={'urls' : ['url_invalida_01', 'url_invalida_02', 'url_invalida_03'], 'palavra' : 'palavra'})
        # Converte a respota da requisicao de string para dicionario
        dictRequest = ast.literal_eval(r.text)
        # Dicionario esperado como respota
        dictEsperado = ast.literal_eval('{"palavra": "palavra", "url_invalida_01": -1, "url_invalida_02": -1, "url_invalida_03": -1}')
        # Compara dicionarios ao inves de strings, pois a ordem nao importa
        self.assertEqual(dictRequest, dictEsperado)

    def test_crawler_02(self):
        r = requests.get(url + '/crawler', json={'urls' : [url + '/autoTest01', url + '/autoTest02', url + '/autoTest03'], 'palavra' : 'Python'})
        dictRequest = ast.literal_eval(r.text)
        dictEsperado = ast.literal_eval('{"' + url + '/autoTest01": 1, "' + url + '/autoTest02": 4, "' + url + '/autoTest03": 4, "palavra": "Python"}')
        self.assertEqual(dictRequest, dictEsperado)

    def test_crawler_03(self):
        r = requests.get(url + '/crawler', json={'urls' : [url + '/autoTest02', 'invalida_url', 'invalida_url'], 'palavra' : 'CrAwLeR'})
        dictRequest = ast.literal_eval(r.text)
        dictEsperado = ast.literal_eval('{"' + url + '/autoTest02": 0, "invalida_url": -1, "palavra": "CrAwLeR"}')
        self.assertEqual(dictRequest, dictEsperado)

    def test_crawler_04(self):
        r = requests.get(url + '/crawler', json={'urls' : [url + '/autoTest02', 'invalida_url', url + '/autoTest01', url + '/autoTest03'], 'palavra' : 'CrAwLeR'})
        dictRequest = ast.literal_eval(r.text)
        dictEsperado = ast.literal_eval('{"' + url + '/autoTest01": 3, "' + url + '/autoTest02": 0, "' + url + '/autoTest03": 3, "invalida_url": -1, "palavra": "CrAwLeR"}')
        self.assertEqual(dictRequest, dictEsperado)

if __name__ == '__main__':
    unittest.main()

    