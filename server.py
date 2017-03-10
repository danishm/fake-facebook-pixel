"""
A  module to serve as an endpoint point for Facebook advertising pixel end point to simple log
the query strings. This allows you to test / develop facebook integration without hitting
facebook
"""

import ssl
import urlparse
import BaseHTTPServer


class MyHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """A simple HTTP hander for logging query params"""

    def do_GET(self):
        """ Handler for GET """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Fake Facebook")

        url_parts = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(url_parts.query)
        for key, val in params.iteritems():
            print "  - %-10s: %s" % (key, val[0])
        print '---------------'
        return

if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(('localhost', 443), MyHTTPHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='www.facebook.com.pem', server_side=True)
    httpd.serve_forever()
