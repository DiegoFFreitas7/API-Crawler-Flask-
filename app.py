from flask import Flask, request, json, render_template, make_response
import asyncio
import ast  # Para converter string em dicionario

from metodos import crawler_Async


loop = asyncio.get_event_loop()
app = Flask(__name__)


@app.route('/crawler', methods=['GET'])
def hello_WebCrawler():
    '''
    Metodo que recebe um JSON com uma lista de url e uma palavra
    e retorna a quantidade de repeticoes da palavra em cada url
    Exemplo: 
    Recebe  {
                urls : ['url1', 'url2, ... 'urln']
                palavra : 'qualquer_string'
            }

    Retorna {
                url1 : repeticao<int>
                url2 : repeticao<int>
                urln : repeticao<int>
                palavra : 'qualquer_string'
            }
    '''
    # Carrega o arquivo JSON recebido em um dicionario
    try:
        data = json.loads(request.data) # Carrega o arquivo JSON recebido em um dicionario
        lista_url = data['urls']        # Pega a lista de url do dicionario
        palavra = data['palavra']       # Pega a palavra do dicionario
    except:
        respota = make_response(json.dumps({'ERRO' : 'JSON incorreto ou inesistente!'}))
        respota.status_code = 400
        return respota
    
    resposta = {}
    
    # listTaks recebe uma lista de 'taks' contendo um dicionarios com a url e a repeticao da palavra
    listTaks = loop.run_until_complete(crawler_Async(lista_url, palavra))
    for taks in listTaks:
        resposta.update(taks.result())
    resposta.update({'palavra' : palavra})

    return json.dumps(resposta)


@app.route('/')
@app.route('/sobre')
def sobre():
    '''
    Notas do desenvolvedor o/
    '''
    visitas = request.cookies.get('visitas')

    if visitas == None:
        visitas = 1
    else:
        try:
            visitas = int(visitas) + 1
        except:
            visitas = 1

    resp = make_response(render_template('sobre.html', ck=visitas))
    resp.set_cookie('visitas', value=str(visitas))
    return resp


# Metodo/Rotas para teste automatico atravez do pytest
@app.route('/autoTest01')
def autoTeste01():
    return render_template('autoTest01.html')

@app.route('/autoTest02')
def autoTeste02():
    return render_template('autoTest02.html')

@app.route('/autoTest03')
def autoTeste03():
    return render_template('autoTest03.html')


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run()

loop.close()