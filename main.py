from flask import Flask, render_template, request, redirect, session, flash


class Skill:
    def __init__(self, name, experience, version):
        self.name=name
        self.experience=experience
        self.version=version


skill1 = Skill('Java', '5 years', '1.8')
skill2 = Skill('Python', '2 years', '3')
skill3 = Skill('NodeJs', '1 year', '18')
list = [skill1, skill2, skill3]

app = Flask(__name__)
app.secret_key = 'teste'


@app.route('/')
def hello():
    return render_template('lista.html', skills=list)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/save', methods=['POST',])
def save():
    name = request.form['name']
    experience = request.form['experience']
    version = request.form['version']

    list.append(Skill(name, experience, version))

    return redirect('/')


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
        return redirect('/login')


@app.route('/logout')
def logout():
    session['user'] = None
    flash('Logout success!')
    return redirect('/')


app.run(host='0.0.0.0', port=8080, debug=True)