from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired('Пожалуйста, введите имя пользователя.')
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired('Пожалуйста, введите пароль.')
    ])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class SignupForm(FlaskForm):
    username = StringField(
        label='Имя пользователя',
        description='имя пользователя - не менее 6 символов',
        validators=[
            DataRequired('Пожалуйста, введите имя пользователя.'),
            validators.Length(
                min=6, message='Слишком короткое имя пользователя.'
            )
        ]
    )

    password = PasswordField(
        label='Пароль',
        description='пароль - не менее 8 символов',
        validators=[
            DataRequired('Пожалуйста, введите пароль.'),
            validators.Length(
                min=8, message='Пароль слишком короткий.'
            ),
            validators.EqualTo('confirm_password',
                               message='Пароли должны совпадать.')
        ]
    )

    confirm_password = PasswordField('Повторите пароль')

    email = StringField('Email', validators=[
                        DataRequired('Пожалуйста, введите email.'), Email(message='Неправильный email адрес.')])

    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                'Пользователь с таким именем уже существует.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Данный email уже используется.')


class PostForm(FlaskForm):
    body = TextAreaField(
        label='Пост',
        description='Длина поста - от 1 до 140 символов.',
        validators=[
            DataRequired('Текст поста не должен быть пустым.'),
            validators.Length(
                max=140, message='Слишком длинный пост.'
            )
        ]
    )

    submit = SubmitField('Опубликовать')
