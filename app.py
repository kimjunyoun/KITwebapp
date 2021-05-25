from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else: 
        # post 로 들어오는 데이터를 받아보자
        search=request.form['fname']
        print("전달된 값:", search)
        return '당신이 검색한 키워드(post) <br>{}입니다.'.format(search)

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else: 
        # post 로 들어오는 데이터를 받아보자
        email =request.form['email']
        pwd =request.form['pwd']
        print("전달된 값:", email, pwd)
        return '회원가입 데이터 (post)'

@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template("login.html")
    else: 
        # post 로 들어오는 데이터를 받아보자
        email =request.form['email']
        pwd =request.form['pwd']
        print("전달된 값:", email, pwd)
        # 만약에 이메일과 패스워드가 같다면
        if email =='a@a.com' and pwd=='1234':
            return "로그인 성공"
        else:
        #아니면
            return "아이디 패스워드를 확인해보세요"
        return '로그인 데이터 (post)'

@app.route('/hello')
def hello():
    return '안녕하세요'

if __name__ == '__main__':
    app.run()