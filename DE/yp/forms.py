from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, DecimalField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=8)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserInfoForm(FlaskForm):
    user_weight = DecimalField('몸무게', places=1)
    user_height = DecimalField('키', places=1)
    user_birth = DateField('생일', format='%Y-%m-%d')
    user_cal = DecimalField('칼로리', places=1)
    user_goal = DecimalField('목표체중', places=1)
    user_sex = BooleanField()
    user_pa = IntegerField('활동량')

class UserLoginForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])