# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm, PostForm
from app import app, db

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post

from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    form = PostForm()
    return render_template('index.html', title='Главная', all_users=User.query.all(), form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!')
        login_user(user)
        return redirect(url_for('index'))
    return render_template('signup.html', title='Регистрация', form=form)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Пользователь {} не найден.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('Вы не можете подписаться на себя.')
        return redirect(url_for('index'))
    current_user.follow(user)
    db.session.commit()
    flash('Вы успешно подписались на {}.'.format(username))
    return redirect(url_for('index'))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Пользователь {} не найден.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('Вы не можете отписаться от себя.')
        return redirect(url_for('user'))
    current_user.unfollow(user)
    db.session.commit()
    flash('Вы успешно отписались от {}.'.format(username))
    return redirect(url_for('index'))


@app.route('/new_post', methods=['POST'])
@login_required
def new_post():
    form = PostForm()
    post = Post(body=form.body.data)
    current_user.create_post(post)
    db.session.commit()
    flash('Новый пост успешно создан.')
    return redirect(url_for('index'))


@app.route('/delete_post/<post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    current_user.delete_post(post_id)
    db.session.commit()
    flash('Пост успешно удалён.')
    return redirect(url_for('index'))


@app.route('/edit_post/<post_id>', methods=['POST'])
@login_required
def edit_post(post_id):
    form = PostForm()
    current_user.edit_post(post_id, form.body.data)
    db.session.commit()
    flash('Пост успешно изменён.')
    return redirect(url_for('index'))