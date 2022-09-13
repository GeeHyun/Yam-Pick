from flask import Blueprint, render_template, session
from yp.models import tb_user

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
   if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("main.html", username = user.user_name, login = True)
   else:
      return render_template("main.html", login = False)

@bp.route("/aboutus")
def aboutus():
   if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("aboutus.html", username = user.user_name, login = True)
   else:
      return render_template("aboutus.html", login = False)

@bp.route("/data")
def data():
      return render_template("data.html", login = False)

@bp.route("/error")
def error():
   if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("error.html", username = user.user_name, login = True)
   else:
      return render_template("error.html", login = False)