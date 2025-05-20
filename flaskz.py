# -*- coding: utf-8 -*-
import app as app

from application  import application , db
from application .models import User, Alcohol, Music, Wish, UserChoice

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Alcohol': Alcohol, 'Music': Music, 'Wish': Wish, 'UserChoice': UserChoice}