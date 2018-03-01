#!/usr/bin/python3

import sys
from sys import argv
import socket
import calculadorav2

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1235))
mySocket.listen(5)

NUM_ARGS = 3

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        petition = recvSocket.recv(2048).decode('utf-8', 'strict')
        print('PETITION: ' + petition)
        resource = petition.split()[1][1:]
        print('RESOURCE: ' + resource)
        list_param = resource.split('/')
        html_answer = '<html><body><h1>Bienvenido a la ' +
                    'calculadora-simple web</h1>'
        if len(list_param) != NUM_ARGS:
            print('ERROR!!')
            sol = "<num1> <operator> <num2>"
            html_answer += '<p>Usage error: num1/operator/num2 </p></body>'
        else:
            print('EXITO!!')
            try:
                num1, operador, num2 = list_param
                sol = num1 + " " + operador + " " + num2 + " = "
                sol += str(calculadorav2.funciones[operador](float(num1), float(num2)))
            except KeyError:
                print('KeyError!!')
                sol = "Operacion no permitida"
            except ZeroDivisionError:
                print('ZeroDivisionError!!')
                sol = "Error, division por cero"
            except:
                print('ERROR_DESC!!')
                sol = "Error, formato invalido"
            html_answer += '<p>Calculo:\r\t' + sol + '</p></body>'

        print('Answering back...')
        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        html_answer +
                        "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
