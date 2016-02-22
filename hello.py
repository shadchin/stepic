
def wsgi_application(environ, start_response):
    print('start')
    body = 'test'
    status = '200 OK'
    headers = [('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))]
    start_response(status, headers)
    return [body]
