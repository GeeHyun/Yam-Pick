from flask import Blueprint, render_template, request, g, session
from functions.base_database import base_database
from yp.models import tb_user

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=["GET", "POST"])
def admin():
    if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("admin/admin.html", username = user.user_name, login = True)
    else:
      return render_template("admin/admin.html", login = False)

@bp.route('/upload')
def upload():
    if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("admin/upload.html", username = user.user_name, login = True)
    else:
      return render_template("admin/admin.html", login = False)