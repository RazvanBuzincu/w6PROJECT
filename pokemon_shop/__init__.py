from flask import Flask
from config import Config
from .blueprints.site.routes import site

app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(site)