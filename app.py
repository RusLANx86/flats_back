from flask import Flask, render_template, session


app = Flask("domclick")
app.config['SECRET_KEY'] = 'mySecretKey.'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check')
def check():
    mail = 'ruslan@info.ru'
    if "mail" not in session:
        session["mail"] = mail
        session["session_count"] = 0
    else:
        session["session_count"] = session.get("session_count") + 1
        session["mail"] = f"{mail} {session['session_count']}"
    return session["mail"]


if __name__ == "__main__":
    app.run()
