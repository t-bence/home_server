#!/usr/bin/python
from app import app
app.jinja_env.add_extension('jinja2.ext.do')
app.run(host='0.0.0.0', port=80, debug=True)