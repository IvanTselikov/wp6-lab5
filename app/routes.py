# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app.forms import LoginForm, SignupForm
from app import app

from app.static.mock import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.login.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Вход', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}'.format(
            form.login.data))
        return redirect('/index')
    return render_template('signup.html', title='Регистрация', form=form)
