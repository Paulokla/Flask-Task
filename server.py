from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return '<H1> Hello User</H1>'

@app.route('/login', Methods=['POST',])
def login_page():   
    return ""
    
@app.route('/register', methods=['POST',])
def register_page():
    return ""
    

@app.route('/profile')
def user_profile():
    return ''


if __name__ == '__main__':
    app.run(debug=True)