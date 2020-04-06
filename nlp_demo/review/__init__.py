from flask import Flask
app = Flask(__name__)

app.config.from_pyfile('default_config.py')   #Works exactly like a dict but provides ways to fill it from files or special dictionaries. There are two common patterns to populate the config.
#Either you can fill the config from a config file:

from review import views