# -*- coding: utf-8 -*- 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Телефонный номер', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Sign In')



class AlcoholForm(FlaskForm):
    alcohol = SelectField('Алкоголь', choices=[('1', 'Водочка'), ('2', 'Винишко'), ('3', 'Коньячок')])
    submit = SubmitField('Добавить алкоголь')

class MusicForm(FlaskForm):
    singer = StringField('Исполнитель', validators=[DataRequired()])
    song = StringField('Песня', validators=[DataRequired()])
    submit = SubmitField('Добавить песню')


class WishForm(FlaskForm):
    wish = StringField('Пожелание', validators=[DataRequired()])
    submit = SubmitField('Добавить пожелание')


class UnitedForm(FlaskForm):
	confirmation =  SelectField(label='Получится ли приехать?', choices=[('1', '-'),('Да', 'Да'), ('Нет', 'Нет'), ('Хз','Не уверен, напишу лично')])
	transfer = SelectField(label='На каком транспорте удобнее добраться?', choices=[('1', '-'),('Сам', 'На своей машине'), ('Запрыгну', 'На машине одного из гостей'), ('Нужно', 'Нужен трансфер'), ('Хз','Не знаю')])
	bed = SelectField(label='Хотел бы переночевать в Деревенских просторах', choices=[('1', '-'), ('Да', 'Да'), ('Нет', 'Нет'), ('ХЗ','Не знаю')])
	alcohol = SelectField(label='Что предпочитаешь выпить?', choices=[('0', '-'), ('1', 'Красное вино'), ('2', 'Белое вино'), ('3', 'Игристое вино')
		, ('4', 'Водка'), ('5', 'Я не пью')])
	text = StringField(label='Какие песни хотел бы услышать на празднике?')
	wish = StringField(label='Есть ли аллергия или пожелания по еде?')
	#, description='Введи ингридиент или блюдо')
	checkbox1=BooleanField(label='С требованием к цветам одежды ознакомился')
	checkbox2=BooleanField(label='Ответы заполнил')
	submit = SubmitField('Отправить')