# API-Crawler-Flask-

'Contador de palavras - Web Crawler'
=

Esta API recebe um JSON via GET com uma lista de URLs e uma palavra. E retorna um JSON com as URLs passada e o numero de repetições dessa palavra em cada site.

---

 Ela foi desenvolvida com o python 3.7 e para testar ou usar é precisso ter instalar:
 
	Flask==1.0.2
  
	beautifulsoup4==4.6.3
  
	requests==2.19.1
  
	pytest==3.8.2
  
 Que pode ser obtido atravez dos comandos:
 
	pip install flask
  
	pip install beautifulsoup4
  
	pip install requests
  
	pip install pytest
  
  
---

Para testar basta rodar o arquivo app.py:

	python app.py
  
---


E em um terminal python:
 
	import requests
	
	url = 'http://localhost:5000'
	
	url_1 = "Coloque aqui a url do site"
	url_2 = "Coloque aqui a url do outro site"
	url_n = "Coloque aqui a url de quantos sites quiser"
	
	palavra = "A palavra ou frase que sera pesquisada nos sites"
	
	# Rota de acesso a API
	rota = '/crawler'
  
	# Faz a requisição para a API via GET
 	r = requests.get(url + rota, json={'urls' : [url_1, url_2, url_n], 'palavra' : palavra})
	# Com r.stato_code verifica se a respota da API foi 200, indicando tudo ok
	r.status_code
	
	# Para ver o resultado:
	r.text
	
	# Respota é dada como no exemplo a baixo
	# {
	#  url_1 : numero de repetições <int>
	#  url_2 : numero de repetições <int>
	#  url_n : numero de repetições <int>
	#  palavra : 'A palavra ou frase que foi pesquisada nos sites'
	# }
	# Um 'numero de repetições' negativo indica que não foi possivel acessar a url informada.
  
 ---
