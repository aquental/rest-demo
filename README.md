# serviço REST ação POST

servidor REST /demo/api/v1.0/soma

ação POST

## Dependencias

Para rodar este programa vc precisa:

* Python 2.7.10
* pip 1.5.6
* virtualenv 1.11.6

## Criando o projeto

1. Verifique as dependencias acima
2. `$ git clone git@github.com:aquental/rest-demo.git rest-demo` - Clone o projeto
3. `$ cd rest-demo` - entre no diretório do projeto


## Preparando o ambiente (Ubuntu)
`$ sudo apt-get install python`

`$ sudo apt-get install python-pip python-dev build-essential`

`$ sudo apt-get install virtualenv`

`$ sudo apt-get install curl`

`$ virtualenv flask`

`$ flask/bin/pip install flask`

`$ flask/bin/pip install flask-httpauth`

`$ chmod a+x demo-flask.py`

## Rodando o servidor
`$ ./demo-flask.py`

$ * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

$ * Restarting with stat

$ * Debugger is active!

$ * Debugger pin code: 203-638-325



## Rodando o teste
`$ curl -u cliente:s3nh@ -H "Content-Type: application/json" í -X POST -d '{ "a":4, "b":"3"}' http://localhost:5000/demo/api/v1.0/soma` - chama a api REST

## Resultado esperado
`$HTTP/1.0 200 OK`

`$Content-Type: application/json`

`$Content-Length: 14`

`$Server: Werkzeug/0.11.4 Python/2.7.10`

`$Date: Tue, 15 Mar 2016 17:47:14 GMT`

`$ `

`${`

`$  "res": 7`

`$}`

