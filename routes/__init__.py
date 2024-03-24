from flask import *

app = Flask(__name__, template_folder='../template', static_folder="../static")
from routes import menu_route
