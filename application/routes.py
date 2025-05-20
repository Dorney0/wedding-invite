# routes.py
import requests

from application import application, db
from flask import render_template, redirect, flash, current_app, request, jsonify, url_for
from application.forms import UnitedForm
from flask_login import current_user, login_user
from application.models import User, Alcohol, Music, Wish, UserChoice
from bot import send_message_to_telegram

@application.before_request
def check_user_key():
    user_key = request.args.get('user_key')
    if user_key and not current_user.is_authenticated:
        # Пример: если user_key не найден в сессии, авторизуем пользователя
        user = User.query.filter_by(username=user_key).first()

        if user:
            login_user(user)
        else:
            flash("Неверный ключ пользователя!")
            return redirect(url_for('login'))

@application.route('/', methods=['GET', 'POST'])
def cabinet():
    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()

    form_uni = UnitedForm(prefix="form_uni")
    if form_uni.validate_on_submit():
        if form_uni.checkbox1.data and form_uni.checkbox2.data:
            user_choice = UserChoice(
                id_user=current_user.id,
                transfer=dict(form_uni.transfer.choices).get(form_uni.transfer.data),
                confirmation=dict(form_uni.confirmation.choices).get(form_uni.confirmation.data),
                bed_flag=dict(form_uni.bed.choices).get(form_uni.bed.data),
                telegram_chat_id=720065938
            )
            db.session.add(user_choice)
            db.session.commit()

            alcohol = Alcohol(alcohol=dict(form_uni.alcohol.choices).get(form_uni.alcohol.data), id_user=current_user.id)
            db.session.add(alcohol)
            db.session.commit()

            music = Music(text=form_uni.text.data, id_user=current_user.id)
            db.session.add(music)
            db.session.commit()

            wish = Wish(wish=form_uni.wish.data, id_user=current_user.id)
            db.session.add(wish)
            db.session.commit()

            # Формируем сообщение с данными из user_choice
            message = f"Новый выбор пользователя {current_user.username}:\n"
            message += f"На каком транспорте удобнее добраться?: {user_choice.transfer}\n"
            message += f"Получится ли приехать?: {user_choice.confirmation}\n"
            message += f"Хотел бы переночевать в Мини-отеле Таежный: {user_choice.bed_flag}"

            # Отправляем сообщение в Telegram
            send_message_to_telegram(720065938, message)  # Используем chat_id вашего бота

            # Отправляем сообщение пользователю в Telegram
            if current_user.telegram_chat_id:
                send_message_to_telegram(current_user.telegram_chat_id, "Спасибо за отправку формы!")
            else:
                flash('Ошибка! У пользователя нет Telegram chat_id.')

            return redirect('/finish')
        else:
            flash('Нужно принять условия соглашения!')
    return render_template('invitation.html', title='Приглашение на свадьбу', form_uni=form_uni, username=current_user.username)


@application.route('/send_message_to_bot', methods=['POST'])
def send_message_to_bot():
    data = request.get_json()  # Получаем данные из формы

    # Формируем сообщение
    message = f"Новая форма: \n{data}"

    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{7907708312:AAH5dgEu7InL-nv1FG0xyK--adSkKQEj5sc}/sendMessage"
    payload = {
        'chat_id': 720065938,
        'text': message
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@application.route('/finish')
def finish():
	return render_template('finish.html')
@application.route('/visual')
def visual():
	queries_c = db.session.query(User.username, UserChoice.confirmation,UserChoice.transfer, UserChoice.bed_flag).join(UserChoice).all()
	queries_alc = db.session.query(Alcohol.alcohol).all()
	queries_wishes = db.session.query(User.username, Wish.wish).join(Wish).all()
	queries_music = db.session.query(User.username, Music.text).join(Music).all()
	return render_template('visual.html', title='Статистика', queries=queries_c, queries_alc=queries_alc, queries_wishes=queries_wishes, queries_music=queries_music)