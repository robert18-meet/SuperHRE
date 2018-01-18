from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from DB import *
app = Flask(__name__)

import views

