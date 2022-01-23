from email.policy import default
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models.user import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    fullname = StringField('Nama Lengkap', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    umur = IntegerField('Usia', validators=[DataRequired()])
    jeniskelamin = SelectField('Jenis Kelamin', validators=[DataRequired()], choices=[('Laki-Laki'), ('Perempuan')])
    confirm_password = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username telah digunakan.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email telah digunakan.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Masuk')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    fullname = StringField('Nama Lengkap', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    umur = IntegerField('Usia', validators=[DataRequired()])
    jeniskelamin = SelectField('Jenis Kelamin', validators=[DataRequired()], choices=[('Laki-Laki'), ('Perempuan')])
    picture = FileField('Foto Profil', validators=[FileAllowed(['jpg', 'png', 'svg'])])

    submit = SubmitField('Ubah Profil')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username telah digunakan.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email telah digunakan.')

class AdminAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    fullname = StringField('Nama Lengkap', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    umur = IntegerField('Usia', validators=[DataRequired()])
    roles = SelectField('Roles', validators=[DataRequired()], choices=[('Admin'),('User')])
    jeniskelamin = SelectField('Jenis Kelamin', validators=[DataRequired()], choices=[('Laki-Laki'), ('Perempuan')])
    picture = FileField('Foto Profil', validators=[FileAllowed(['jpg', 'png', 'svg'])])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Ubah Profil')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username telah digunakan.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email telah digunakan.')
