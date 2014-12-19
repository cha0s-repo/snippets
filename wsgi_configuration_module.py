#!/usr/bin/env python	

import os
import sys

sys.path.append('/srv/www/android/application')

os.environ['PYTHON_EGG_CACHE'] = '/srv/www/android/.python-egg'

def application(environ, start_response):
    status = '200 OK'
    output = ""

    with open('/srv/www/android/public_html/404.html') as f:
        output = f.read()

    response_headers = [('Content-type', 'text/html'),
                    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return output
