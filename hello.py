
def wsgi_application(environ, start_response):
    body = environ['QUERY_STRING']
    body = '\n'.join(body.split('&'))
    status = '200 OK'
    headers = [('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))]
    start_response(status, headers)
    return [body]
