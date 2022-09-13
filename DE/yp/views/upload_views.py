from flask import Blueprint, render_template, redirect, request, session, g
from yp.models import tb_user_img, tb_food_img
from yp import db
from sqlalchemy import func, and_
from functions import func_ml, func_user__nutrient

import config
import os


bp = Blueprint('upload', __name__, url_prefix='/upload')
NEW_IMG = None


@bp.route('/')
def upload():
    return render_template("upload/upload.html", login = True)

@bp.route("/", methods=["GET","POST"])
def upload_done():
    try:
        global NEW_IMG
        NEW_IMG = tb_user_img()
        NEW_IMG.upload_index = db.session.query(func.count(tb_user_img.upload_index)).all()[0][0] + 1
        NEW_IMG.upload_user = g.user.user_email
        NEW_IMG.upload_location = os.path.join(config.BASE_DIR, f"yp/static/img/user_upload/{NEW_IMG.upload_index}.jpg")

        uploaded_files = request.files["food_img"]
        uploaded_files.save(NEW_IMG.upload_location)

        # DS 결과
        global model_result
        model_result = func_ml.image_prediction_result(NEW_IMG.upload_location, config.BASE_DIR, '/DenseNet201_129menu.h5')

        return render_template("upload/upload_check.html", first = model_result["TOP1"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg", login = True)

    except:
        return render_template("error_submit.html", login = True)

@bp.route("/re", methods=["GET","POST"])
def double_check():
    if NEW_IMG:
        return render_template("upload/upload_check2.html", food_list = model_result["TOP2to5"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg", login = True)

    else:
        return render_template("error.html", login = True)


@bp.route("/how", methods=["GET","POST"])
def how():
    if NEW_IMG:
        NEW_IMG.upload_foodname = request.form["food_name"].replace(" ", "")

        # 이미 가지고 있는 음식 목록에 있다면
        food_being = tb_food_img.query.filter_by(food_name=NEW_IMG.upload_foodname).first()
        if food_being:
            NEW_IMG.upload_isnew = False
            return render_template("upload/upload_how.html", photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg", login = True)
        else:
            NEW_IMG.upload_isnew = True
            db.session.add(NEW_IMG)
            db.session.commit()
            return render_template("upload/upload_isnew.html", login = True)

    else:
        return render_template("error.html", login = True)

@bp.route("/result", methods=["POST"])
def result():
    food_being = tb_food_img.query.filter_by(food_name=NEW_IMG.upload_foodname).first()

    NEW_IMG.upload_percent = float(request.form["ratio"])
    db.session.add(NEW_IMG)
    db.session.commit()

    return redirect('/dashboard/')