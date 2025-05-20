from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import login

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@login.request_loader
def load_user_from_request(request):
    # first, try to login using the username url arg
    username = request.args.get('user_key')  # Переименуем user_key в username
    if username:
        user = User.query.filter_by(username=username).first()  # Используем поле username
        if user:
            return user
    return None

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    realname = db.Column(db.String(120))
    alcohols = db.relationship('Alcohol', backref='author', lazy='dynamic')
    musics = db.relationship('Music', backref='author', lazy='dynamic')
    wishes = db.relationship('Wish', backref='author', lazy='dynamic')
    choices = db.relationship('UserChoice', backref='author', lazy='dynamic')
    telegram_chat_id = db.Column(db.String(255), nullable=True)  # Добавьте это поле
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
    	return '<User {}>'.format(self.username)

class UserChoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    transfer = db.Column(db.String(100))
    bed_flag = db.Column(db.String(100))
    confirmation = db.Column(db.String(100))
    telegram_chat_id = db.Column(db.String(255), nullable=True)  # Добавьте это поле

    def __repr__(self):
    	return '<UserChoice {}>'.format(self.id_user, self.transfer, self.bed_flag, self.confirmation) 


class Alcohol(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
	alcohol = db.Column(db.String(64), index=True, unique=False)
	def __repr__(self):
		return '<Alcohol {}>'.format(self.alcohol) 

class Music(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
	text = db.Column(db.String(4000), index=True, unique=False)	
	def __repr__(self):
		return '<Music {}>'.format(self.text) 

class Wish(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
	wish = db.Column(db.String(4000), index=True, unique=False)
	
	def __repr__(self):
		return '<Wish {}>'.format(self.wish) 