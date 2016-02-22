
def wsgi_application(environ, start_response):
    body = 'test'
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [body]
