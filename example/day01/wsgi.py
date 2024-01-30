def application(environ, start_response):
    # Processa o request
    # print(environ) # Irá printar variáveis de ambiente - WARN!

    # Monta o response
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    body =b'<strong>Hello World</strong>'

    # Chama função de callback
    start_response(status, headers)
    # Envia o iteravel para o 'cgi'
    return [body]

#  if __name__ == '__main__':
#   from wsgiref.simple_server import make_server
#   server = make_server('0.0.0.0', 8000, application)
#   server.serve_forever()
