from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from datetime import datetime

from yp import db
from yp.forms import UserCreateForm, UserInfoForm, UserLoginForm
from yp.models import tb_user, tb_user_info

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = tb_user.query.filter_by(user_email=form.email.data).first()
        if not email:
            user = tb_user(user_name=form.username.data,
                        user_pw=generate_password_hash(form.password1.data),
                        user_email=form.email.data,
                        user_status=1)
            db.session.add(user)
            db.session.commit()

            session.clear()
            session['user'] = user.user_email
            return redirect(url_for('auth.more_info'))
        else:
            flash('이미 존재하는 이메일입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/more_info/', methods=('GET', 'POST'))
def more_info():
    form = UserInfoForm()
    today = datetime.now().date()
    if request.method == 'POST' and form.validate_on_submit():
        user = tb_user_info(user_email=session['user'],
                            user_weight=int(form.user_weight.data),
                            user_height=int(form.user_height.data),
                            user_birth=form.user_birth.data,
                            user_cal=form.user_cal.data,
                            user_goal=int(form.user_goal.data),
                            user_sex=form.user_sex.data,
                            user_pa=form.user_pa.data
                            )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.main'))
    return render_template('auth/more_info.html', form=form, today=today)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = tb_user.query.filter_by(user_email=form.email.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.user_pw, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        elif user.user_email == "miso324@naver.com":
            session.clear()
            session['user'] = user.user_email
            return redirect(url_for('admin.admin'))
        elif error is None:
            session.clear()
            session['user'] = user.user_email
            return redirect(url_for('main.main'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_email = session.get('user')
    if user_email is None:
        g.user = None
        g.user_info = None
    else:
        g.user = tb_user.query.get(user_email)
        g.user_info = tb_user_info.query.get(user_email)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.main'))


@bp.route('/signout/', methods=('GET', 'POST'))
def signout():
    if g.user:
        if request.method == 'POST':
            user = db.session.query(tb_user).filter_by(user_email=g.user.user_email).first()
            db.session.delete(user)
            db.session.commit()
            session.clear()
            return render_template('main.html')
        return render_template('auth/signout.html', login = True)
    else:
        return render_template("error.html", login = True)