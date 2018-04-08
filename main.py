
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['POST', 'GET'])
def index():
    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    title = 'SignUp'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if username == " ":
                username_error = 'Invalid username'
                username = ''
        else:
            if (len(username) < 3) or (len(username) > 20):
                username_error = 'Invalid username'
                username = ''
        if password == " " :
                password_error = 'Invalid passcode.'
        else:
                if (len(password)< 3) or (len(password) > 20):
                    password_error = 'Invaild password'
        if not len(password):
            password_error = 'Invalid password'
        if (verify.strip()==""):
             verify_error = 'Passwords do not match.'
        else:
            if password != verify:
                verify_error = 'Passwords do not match.'
          
        if ('@' not in email) or ('.' not in email):
            email_error = 'Invalid email'
            email = ''
        if (not username_error) and (not password_error) and (not verify_error) and (not email_error):
            return redirect('/valid-signup?username={0}'.format(username))
    return render_template('base.html', title=title, username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           verify_error=verify_error, email_error=email_error)
@app.route('/valid-signup')
def valid_signup():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('validsignup.html', title=title, username=username)
if __name__ == '__main__':
 app.run()

