#!/usr/bin/env python3
import optparse


def flaskrun(app, default_host='127.0.0.1', default_port='500'):
    parser = optparse.OptionParser()
    parser.add_option('-H', '--host', default=default_host)
    parser.add_option('-P', '--port', default=default_port)
    options, _ = parser.parse_args()

    app.run(host=options.host, port=int(options.port))
