# -*- coding: utf-8 -*-
from flask import render_template
from app import app

from app.static.mock import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', user=user, posts=posts)
