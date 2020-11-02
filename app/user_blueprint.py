import os

from flask import (Flask, url_for, render_template,
                   request, session, redirect, make_response)
from sqlalchemy.orm import sessionmaker

from db.users import Users, engine
from utils.verify_code import CaptchaTool

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.urandom(16)


@app.route("/")
def index():
    """首页"""
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """登录"""
    # 获取用户名、密码、验证码
    username = request.form.get("username")
    pwd = request.form.get('pwd', None)
    code = request.form.get('code', None)
    # 判断各项数据是否为空，通常前端会做这类判断并且验证数据格式，但是重要数据后端依然要做验证，防止恶意数据
    if not (username and pwd and code):
        return redirect(url_for('error_page',
                                message='username, password or code cannot be none'))
    """
    先判断验证码是否正确，不正确则打回（先判断原因：减少访问数据库次数，削减数据库压力，减少不必要的资源浪费）
    正常的业务逻辑是在用户输入用户名或者密码或者验证码后使用ajax 或者axios 等发送异步请求查询是否有该用户，没有则局部刷新给用户提示信息
    而不是现在这样直接打到错误页面，用户体验极差
    """
    if code == session['code']:
        try:
            Session = sessionmaker(bind=engine)
            session_db = Session()
            user = session_db.query(Users.username, Users.pwd)\
                .filter(Users.username == username, Users.pwd == pwd)\
                .first()
        except Exception:
            # 通常这类异常需要交给全局异常处理器来处理，并且要细粒度捕捉，
            # 然后根据异常跳转到某个提示页面，优化用户体验
            return redirect(url_for('error_page', message='unknown error occured'))

        # 若表中有该用户，则在session中存储该用户信息
        if user:
            session['username'] = username
            session['user'] = user
            # flask 要求每个分支都要有返回值，可优化
            return redirect(url_for('go_main', username=username))
        return redirect(url_for('error_page', message='no user'))
    return redirect(url_for('error_page', message='wrong code'))


@app.route('/main', methods=['GET'])
def go_main():
    """主页"""
    # 判断session中是否有'user'属性，没有则表示当前客户端未登录，打回到登录页面
    if not session.get('user', None):
        return render_template('login.html')
    return render_template('main.html', username=session['username'])


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """退出"""
    if session.get('username') is not None:
        session.clear()
        return redirect(url_for('index'))
    return render_template('error.html', message='please login first!')


@app.route('/errorPage/<message>', methods=['GET', 'POST'])
def error_page(message):
    """错误页面"""
    return render_template('error.html', message=message)


@app.route('/getCaptcha', methods=["GET"])
def test_get_captcha():
    """
    获取图形验证码
    :return:
    """
    new_captcha = CaptchaTool()
    # 获取图形验证码
    img, code = new_captcha.get_verify_code()
    response = make_response(img)
    response.headers['Content-Type'] = 'image/gif'
    # 存入session
    session["code"] = code
    print(code)
    return response
