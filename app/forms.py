from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[
        DataRequired('Пожалуйста, введите логин.')
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired('Пожалуйста, введите пароль.')
    ])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class SignupForm(FlaskForm):
    first_name = StringField('Имя', validators=[
        DataRequired('Пожалуйста, введите имя.')
    ])

    last_name = StringField('Фамилия', validators=[
        DataRequired('Пожалуйста, введите фамилию.')
    ])

    login = StringField(
        label='Логин',
        description='логин - не менее 6 символов',
        validators=[
            DataRequired('Пожалуйста, введите логин.'),
            validators.Length(
                min=6, message='Логин слишком короткий.'
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
    submit = SubmitField('Зарегистрироваться')
