from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret' 

user = {"username": "abc", "password": "xyz"}

@app.route('/')
def main():
  if('user' in session and session['user'] == user['username']):
    return render_template('index.html')
    
  return '<h1>You are not logged in.</h1><br><a href="https://stalegentleserverapplication.sas2k.repl.co/login">log-in</a>'

@app.route('/login', methods=['GET','POST'])
def login():
  if(request.method == 'POST'):
    username = request.form.get('username')
    password = request.form.get('password')     
    if username == user['username'] and password == user['password']:
              
      session['user'] = username
      return redirect('/')

    return "<body style='background-color: lightgray;'><h1>Wrong username or password</h1></body>"#if the username or password does not matches 

  return render_template("sign-in.html")

@app.route('/logout')
def logout():
  session.pop('user')         
  return redirect('/login')

if __name__ == '__main__':
  app.run('0.0.0.0', 1234, False)