from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import SkillUser


@app.route('/')
def index():
    list = SkillUser.query.order_by(SkillUser.id)
    return render_template('lista.html', skills=list)


@app.route('/new')
def new():
    if 'user' not in session or session['user'] == None:
        return redirect('/login')

    return render_template('form.html')


@app.route('/save', methods=['POST',])
def save():
    name = request.form['name']
    experience = request.form['experience']
    version = request.form['version']

    list.append(SkillUser(name, experience, version))

    return redirect('/')


@app.route('/update', methods=['POST',])
def update():
    name = request.form['name']
    experience = request.form['experience']
    version = request.form['version']

    list.append(SkillUser(name, experience, version))

    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user' not in session or session['user'] == None:
        return redirect('/login')

    skill = SkillUser.query.filter_by(id=id).first()
    return render_template('edit.html', edit=skill)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth', methods=['POST', ])
def authentication():
    if '123456' == request.form['pass']:
        session['user'] = request.form['user']
        flash('Success')
        return redirect('/')
    else:
        flash('Error authentication!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user'] = None
    flash('Logout success!')
    return redirect('/')