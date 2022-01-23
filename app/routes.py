
from distutils.log import error
from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.models.data_tk import data_tipekepribadian
from app.models.form import RegistrationForm, LoginForm, UpdateAccountForm, AdminAccountForm
from app.controllers import soalController, admin, ml, decisiontree
from app.models.user import User, Hasiltes
from app.models.soal import Soal
from flask_login import login_user, current_user, logout_user, login_required
import numpy as np
import secrets
import os
#############################################################

@app.route('/')
def home():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='img/' + current_user.image_file)
        return render_template("user/beranda.html", image_file=image_file)
    return render_template("user/beranda.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Gagal melakukan login. Cek kembali Email dan Password anda', 'danger')
    return render_template("auth/login.html", form=form)

@app.route('/forgot')
def forgot():
    return render_template("auth/forgot.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_password, jenis_kelamin=form.jeniskelamin.data, umur=form.umur.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Akun Berhasil dibuat!', 'success')
        return redirect(url_for('login'))
    return render_template("auth/register.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/reset')
def reset():
    return render_template("auth/reset.html")

@app.route('/aturan')
@login_required
def aturan():
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("user/aturan.html", image_file=image_file)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', 'picture_fn')
    form_picture.save(picture_path)

    return picture_fn

@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil():
    id = current_user.id
    form = UpdateAccountForm()
    name_to_update = User.query.get(id)
    if request.method == 'POST':
        name_to_update.fullname = form.fullname.data
        name_to_update.username = form.username.data
        name_to_update.email = form.email.data
        name_to_update.jenis_kelamin = form.jeniskelamin.data
        name_to_update.umur = form.umur.data
        try:
            db.session.commit()
            flash(f'Akun anda berhasil diperbarui.', 'success')
            return redirect(url_for('profil'))
        except:
            flash(f'Akun gagal diperbarui', 'Danger')
            return redirect(url_for('profil'))
    if request.method == 'GET':
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.jeniskelamin.data = current_user.jenis_kelamin
        form.umur.data = current_user.umur
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("user/profile.html", image_file=image_file, form=form, name_to_update=name_to_update)

@app.route('/profil/info_hasil/<int:id_hasil>')
@login_required
def profil_infohasil(id_hasil):
    image_file = url_for('static', filename='img/' + current_user.image_file)
    hasil = Hasiltes.query.get_or_404(id_hasil)
    deskripsi = data_tipekepribadian.query.all()
    for deskripsi in deskripsi:
        if deskripsi.tipe_kepribadian == hasil.hasil_tipekepribadian:
            hasil_deskripsi = [deskripsi.deskripsi, deskripsi.ciri_umum, deskripsi.nilai_dalam_team, deskripsi.kemungkinan_kelemahan, deskripsi.ketakutan_terbesar]
    if current_user.id != hasil.user_id:
        return redirect(url_for('hasiltes_user'))
    else:
        return render_template("user/infohasil_user.html", image_file=image_file, hasil=hasil, hasil_deskripsi=hasil_deskripsi)
        

@app.route('/hasiltes_user', methods=['GET'])
@login_required
def hasiltes_user():
    image_file = url_for('static', filename='img/' + current_user.image_file)
    hasil = Hasiltes.query.filter_by(user_id=current_user.id).all()
    return render_template("user/hasiltes_user.html", image_file=image_file, hasil=hasil)

@app.route('/tentang')
def tentang():
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("user/tentang.html", image_file=image_file)

@app.route('/lamantes', methods=['GET', 'POST'])
@login_required
def lamantes():
    data = soalController.index()
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("user/lamantes.html", data=data, image_file=image_file)

@app.route('/jawaban_error')
@login_required
def jawab_error():
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("user/jawab_error.html", image_file=image_file)
    
@app.route('/hasiltes', methods=['GET', 'POST'])
@login_required
def hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]

    for data in data:
        # 1
        lsoal_1 = request.values.get('l['+ str(data[0]) +']')
        msoal_1 = request.values.get('m['+ str(data[0]) +']')
        if msoal_1 == lsoal_1:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.1, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_1 == '#D' and lsoal_1 == 'D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.1, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_1 or not lsoal_1.strip():
            flash('Terdapat jawaban yang kosong pada soal No.1, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_1 or not msoal_1.strip():
            flash('Terdapat jawaban yang kosong pada soal No.1, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 2
        msoal_2 = request.values.get('m['+ str(data[1]) +']')
        lsoal_2 = request.values.get('l['+ str(data[1]) +']')
        if msoal_2 == lsoal_2:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan mengosongkan jawaban atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.2, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_2 == '#I' and lsoal_2 == 'I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.2, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_2 == 'C' and lsoal_2 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.2, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_2 or not msoal_2.strip():
            flash('Terdapat jawaban yang kosong pada soal No.2, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_2 or not lsoal_2.strip():
            flash('Terdapat jawaban yang kosong pada soal No.2, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 3
        msoal_3 = request.values.get('m['+ str(data[2]) +']')
        lsoal_3 = request.values.get('l['+ str(data[2]) +']')
        if msoal_3 == lsoal_3:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.3, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_3 == '#C' and lsoal_3 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.3, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_3 == '#S' and lsoal_3 == 'S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.3, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_3 or not msoal_3.strip():
            flash('Terdapat jawaban yang kosong pada soal No.3, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_3 or not lsoal_3.strip():
            flash('Terdapat jawaban yang kosong pada soal No.3, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 4
        msoal_4 = request.values.get('m['+ str(data[3]) +']')
        lsoal_4 = request.values.get('l['+ str(data[3]) +']')
        if msoal_4 == lsoal_4:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.4, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_4 == '#I' and lsoal_4 == 'I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.4, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_4 or not msoal_4.strip():
            flash('Terdapat jawaban yang kosong pada soal No.4, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_4 or not lsoal_4.strip():
            flash('Terdapat jawaban yang kosong pada soal No.4, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 5
        msoal_5 = request.values.get('m['+ str(data[4]) +']')
        lsoal_5 = request.values.get('l['+ str(data[4]) +']')
        if msoal_5 == lsoal_5:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.5, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_5 == '#C' and lsoal_5 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.5, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_5 == 'I' and lsoal_5 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.5, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_5 or not msoal_5.strip():
            flash('Terdapat jawaban yang kosong pada soal No.5, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_5 or not lsoal_5.strip():
            flash('Terdapat jawaban yang kosong pada soal No.5, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 6
        msoal_6 = request.values.get('m['+ str(data[5]) +']')
        lsoal_6 = request.values.get('l['+ str(data[5]) +']')
        if msoal_6 == lsoal_6:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.6, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_6 == 'C' and lsoal_6 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.6, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_6 or not msoal_6.strip():
            flash('Terdapat jawaban yang kosong pada soal No.6, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_6 or not lsoal_6.strip():
            flash('Terdapat jawaban yang kosong pada soal No.6, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 7
        msoal_7 = request.values.get('m['+ str(data[6]) +']')
        lsoal_7 = request.values.get('l['+ str(data[6]) +']')
        if msoal_7 == lsoal_7:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_7 == '#C' and lsoal_7 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_7 == '#D' and lsoal_7 == 'D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_7 == 'S' and lsoal_7 == '#S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_7 or not msoal_7.strip():
            flash('Terdapat jawaban yang kosong pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_7 or not lsoal_7.strip():
            flash('Terdapat jawaban yang kosong pada soal No.7, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 8
        msoal_8 = request.values.get('m['+ str(data[7]) +']')
        lsoal_8 = request.values.get('l['+ str(data[7]) +']')
        if msoal_8 == lsoal_8:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.8, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_8 or not msoal_8.strip():
            flash('Terdapat jawaban yang kosong pada soal No.8, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_8 or not lsoal_8.strip():
            flash('Terdapat jawaban yang kosong pada soal No.8, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 9
        msoal_9 = request.values.get('m['+ str(data[8]) +']')
        lsoal_9 = request.values.get('l['+ str(data[8]) +']')
        if msoal_9 == lsoal_9:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.9, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_9 == '#I' and lsoal_9 == 'I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.9, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_9 == '#S' and lsoal_9 == 'S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.9, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_9 or not msoal_9.strip():
            flash('Terdapat jawaban yang kosong pada soal No.9, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_9 or not lsoal_9.strip():
            flash('Terdapat jawaban yang kosong pada soal No.9, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 10
        msoal_10 = request.values.get('m['+ str(data[9]) +']')
        lsoal_10 = request.values.get('l['+ str(data[9]) +']')
        if msoal_10 == lsoal_10:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.10, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_10 == '#C' and lsoal_10 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.10, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_10 == 'I' and lsoal_10 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.10, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_10 or not msoal_10.strip():
            flash('Terdapat jawaban yang kosong pada soal No.10, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_10 or not lsoal_10.strip():
            flash('Terdapat jawaban yang kosong pada soal No.10, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 11
        msoal_11 = request.values.get('m['+ str(data[10]) +']')
        lsoal_11 = request.values.get('l['+ str(data[10]) +']')
        if msoal_11 == lsoal_11:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.11, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_11 == '#C' and lsoal_11 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.11, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_11 == 'I' and lsoal_11 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.11, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_11 or not msoal_11.strip():
            flash('Terdapat jawaban yang kosong pada soal No.11, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_11 or not lsoal_11.strip():
            flash('Terdapat jawaban yang kosong pada soal No.11, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 12
        msoal_12 = request.values.get('m['+ str(data[11]) +']')
        lsoal_12 = request.values.get('l['+ str(data[11]) +']')
        if msoal_12 == lsoal_12:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.12, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_12 == '#S' and lsoal_12 == 'S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.12, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_12 == 'C' and lsoal_12 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.12, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_12 or not msoal_12.strip():
            flash('Terdapat jawaban yang kosong pada soal No.12, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_12 or not lsoal_12.strip():
            flash('Terdapat jawaban yang kosong pada soal No.12, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 13
        msoal_13 = request.values.get('m['+ str(data[12]) +']')
        lsoal_13 = request.values.get('l['+ str(data[12]) +']')
        if msoal_13 == lsoal_13:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_13 == '#C' and lsoal_13 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_13 == 'S' and lsoal_13 == '#S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_13 == 'I' and lsoal_13 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_13 or not msoal_13.strip():
            flash('Terdapat jawaban yang kosong pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_13 or not lsoal_13.strip():
            flash('Terdapat jawaban yang kosong pada soal No.13, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 14
        msoal_14 = request.values.get('m['+ str(data[13]) +']')
        lsoal_14 = request.values.get('l['+ str(data[13]) +']')
        if msoal_14 == lsoal_14:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.14, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_14 == 'S' and lsoal_14 == '#S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.14, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_14 or not msoal_14.strip():
            flash('Terdapat jawaban yang kosong pada soal No.14, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_14 or not lsoal_14.strip():
            flash('Terdapat jawaban yang kosong pada soal No.14, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 15
        msoal_15 = request.values.get('m['+ str(data[14]) +']')
        lsoal_15 = request.values.get('l['+ str(data[14]) +']')
        if msoal_15 == lsoal_15:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.15, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_15 == 'C' and lsoal_15 == '#C':
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.15, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_15 or not msoal_15.strip():
            flash('Terdapat jawaban yang kosong pada soal No.15, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_15 or not lsoal_15.strip():
            flash('Terdapat jawaban yang kosong pada soal No.15, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 16
        msoal_16 = request.values.get('m['+ str(data[15]) +']')
        lsoal_16 = request.values.get('l['+ str(data[15]) +']')
        if msoal_16 == lsoal_16:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.16, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_16 == '#D' and lsoal_16 == 'D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.16, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_16 == 'C' and lsoal_16 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.16, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_16 or not msoal_16.strip():
            flash('Terdapat jawaban yang kosong pada soal No.16, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_16 or not lsoal_16.strip():
            flash('Terdapat jawaban yang kosong pada soal No.16, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 17
        msoal_17 = request.values.get('m['+ str(data[16]) +']')
        lsoal_17 = request.values.get('l['+ str(data[16]) +']')
        if msoal_17 == lsoal_17:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.17, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_17 == '#C' and lsoal_17 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.17, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_17 == 'I' and lsoal_17 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.17, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_17 or not msoal_17.strip():
            flash('Terdapat jawaban yang kosong pada soal No.17, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_17 or not lsoal_17.strip():
            flash('Terdapat jawaban yang kosong pada soal No.17, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 18
        msoal_18 = request.values.get('m['+ str(data[17]) +']')
        lsoal_18 = request.values.get('l['+ str(data[17]) +']')
        if msoal_18 == lsoal_18:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_18 == '#I' and lsoal_18 == 'I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_18 == '#S' and lsoal_18 == 'S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_18 == 'C' and lsoal_18 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_18 or not msoal_18.strip():
            flash('Terdapat jawaban yang kosong pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_18 or not lsoal_18.strip():
            flash('Terdapat jawaban yang kosong pada soal No.18, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 19
        msoal_19 = request.values.get('m['+ str(data[18]) +']')
        lsoal_19 = request.values.get('l['+ str(data[18]) +']')
        if msoal_19 == lsoal_19:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.19, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_19 == '#C' and lsoal_19 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.19, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_19 == 'S' and lsoal_19 == '#S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.19, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_19 or not msoal_19.strip():
            flash('Terdapat jawaban yang kosong pada soal No.19, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_19 or not lsoal_19.strip():
            flash('Terdapat jawaban yang kosong pada soal No.19, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 20
        msoal_20 = request.values.get('m['+ str(data[19]) +']')
        lsoal_20 = request.values.get('l['+ str(data[19]) +']')
        if msoal_20 == lsoal_20:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.20, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_20 == 'C' and lsoal_20 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.20, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_20 == 'D' and lsoal_20 == '#D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.20, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_20 or not msoal_20.strip():
            flash('Terdapat jawaban yang kosong pada soal No.20, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_20 or not lsoal_20.strip():
            flash('Terdapat jawaban yang kosong pada soal No.20, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 21
        msoal_21 = request.values.get('m['+ str(data[20]) +']')
        lsoal_21 = request.values.get('l['+ str(data[20]) +']')
        if msoal_21 == lsoal_21:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.21, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_21 == '#C' and lsoal_21 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.21, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_21 or not msoal_21.strip():
            flash('Terdapat jawaban yang kosong pada soal No.21, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_21 or not lsoal_21.strip():
            flash('Terdapat jawaban yang kosong pada soal No.21, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 22
        msoal_22 = request.values.get('m['+ str(data[21]) +']')
        lsoal_22 = request.values.get('l['+ str(data[21]) +']')
        if msoal_22 == lsoal_22:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.22, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_22 == '#I' and lsoal_22 == 'I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.22, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_22 or not msoal_22.strip():
            flash('Terdapat jawaban yang kosong pada soal No.22, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_22 or not lsoal_22.strip():
            flash('Terdapat jawaban yang kosong pada soal No.22, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 23
        msoal_23 = request.values.get('m['+ str(data[22]) +']')
        lsoal_23 = request.values.get('l['+ str(data[22]) +']')
        if msoal_23 == lsoal_23:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_23 == '#D' and lsoal_23 == 'D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_23 == '#C' and lsoal_23 == 'C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_23 == 'I' and lsoal_23 == '#I':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_23 or not msoal_23.strip():
            flash('Terdapat jawaban yang kosong pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_23 or not lsoal_23.strip():
            flash('Terdapat jawaban yang kosong pada soal No.23, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        # 24
        msoal_24 = request.values.get('m['+ str(data[23]) +']')
        lsoal_24 = request.values.get('l['+ str(data[23]) +']')
        if msoal_24 == lsoal_24:
            flash('Terdapat jawaban yang kosong atau TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_24 == '#S' and lsoal_24 == 'S':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_24 == 'D' and lsoal_24 == '#D':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if msoal_24 == 'C' and lsoal_24 == '#C':
            flash('TIDAK diperbolehkan memilih PALING dan KURANG dengan penyataan yang sama pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not msoal_24 or not msoal_24.strip():
            flash('Terdapat jawaban yang kosong pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))
        if not lsoal_24 or not lsoal_24.strip():
            flash('Terdapat jawaban yang kosong pada soal No.24, Silahkan kembali ke laman sebelumnya.', 'danger')
            return redirect(url_for('jawab_error'))


    image_file = url_for('static', filename='img/' + current_user.image_file)

    m_hasil = soalController.hitung_mhasiltes() 
    l_hasil = soalController.hitung_lhasiltes()
    c_hasil = soalController.hitung_chasiltes()
    hasil_tipekepribadian = soalController.hasil_tipekepribadian()
    

    skor_dominance_most = soalController.hasilskor_dominance_most()
    skor_influance_most = soalController.hasilskor_influance_most()
    skor_steadiness_most = soalController.hasilskor_steadiness_most()
    skor_compliance_most = soalController.hasilskor_compliance_most()
    skor_dominance_least = soalController.hasilskor_dominance_least()
    skor_influance_least = soalController.hasilskor_influance_least()
    skor_steadiness_least = soalController.hasilskor_steadiness_least()
    skor_compliance_least = soalController.hasilskor_compliance_least()
    skor_dominance = soalController.hasilskor_dominance()
    skor_influance = soalController.hasilskor_influance()
    skor_steadiness = soalController.hasilskor_steadiness()
    skor_compliance = soalController.hasilskor_compliance()

    hasil_klasifikasi = ml.klasifikasipekerjaan()

    new_hasil = Hasiltes(most_D=m_hasil[0], most_I=m_hasil[1], most_S=m_hasil[2], most_C=m_hasil[3], least_D=l_hasil[0], least_I=l_hasil[1], least_S=l_hasil[2], least_C=l_hasil[3], change_D=c_hasil[0], change_I=c_hasil[1], change_S=c_hasil[2], change_C=c_hasil[3], hasil_tipekepribadian=hasil_tipekepribadian, rekomendasi_pekerjaan=hasil_klasifikasi, nama=current_user)

    db.session.add(new_hasil)
    db.session.commit()

    deskripsi = soalController.deskripsikepribadian()

    change_chart = {}
    change_chart['name'] = 'Graph_CHANGE'
    change_chart['labels'] = ['Dominance', 'Influance', 'Steadiness', 'Compliance']
    change_chart['datasets'] = [
        {
            'label': 'Skor',
            'lineTension': False,
            'backgroundColor': 'rgba(78, 115, 223, 0.05)',
            'borderColor': 'rgba(78, 115, 223, 1)',
            'pointRadius': 3,
            'pointBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHoverRadius': 3,
            'pointHoverBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointHoverBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHitRadius': 10,
            'pointBorderWidth': 2,
            'data' : [skor_dominance, skor_influance, skor_steadiness, skor_compliance]
        },
    ]
    
    most_chart = {}
    most_chart['name'] = 'Graph_MOST'
    most_chart['labels'] = ['Dominance', 'Influance', 'Steadiness', 'Compliance']
    most_chart['datasets'] = [
        {
            'label': 'Skor',
            'lineTension': False,
            'backgroundColor': 'rgba(78, 115, 223, 0.05)',
            'borderColor': 'rgba(78, 115, 223, 1)',
            'pointRadius': 3,
            'pointBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHoverRadius': 3,
            'pointHoverBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointHoverBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHitRadius': 10,
            'pointBorderWidth': 2,
            'data' : [skor_dominance_most, skor_influance_most, skor_steadiness_most, skor_compliance_most]
        },
    ]

    least_chart = {}
    least_chart['name'] = 'Graph_LEAST'
    least_chart['labels'] = ['Dominance', 'Influance', 'Steadiness', 'Compliance']
    least_chart['datasets'] = [
        {
            'label': 'Skor',
            'lineTension': False,
            'backgroundColor': 'rgba(78, 115, 223, 0.05)',
            'borderColor': 'rgba(78, 115, 223, 1)',
            'pointRadius': 3,
            'pointBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHoverRadius': 3,
            'pointHoverBackgroundColor': 'rgba(78, 115, 223, 1)',
            'pointHoverBorderColor': 'rgba(78, 115, 223, 1)',
            'pointHitRadius': 10,
            'pointBorderWidth': 2,
            'data' : [skor_dominance_least, skor_influance_least, skor_steadiness_least, skor_compliance_least]
        },
    ]
    
    return render_template("user/hasiltes.html", m_hasil=m_hasil, l_hasil=l_hasil, c_hasil=c_hasil, skor_dominance=skor_dominance, skor_influance=skor_influance, skor_steadiness=skor_steadiness, skor_compliance=skor_compliance,image_file=image_file, hasil_tipekepribadian=hasil_tipekepribadian, change_chart=change_chart, least_chart=least_chart, most_chart=most_chart, deskripsi=deskripsi, hasil_klasifikasi=hasil_klasifikasi)

@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        jumlah_user = len(User.query.all())
        jumlah_hasil = len(Hasiltes.query.all())
        return render_template("admin/dashboard.html", image_file=image_file, jumlah_user=jumlah_user, jumlah_hasil=jumlah_hasil)
    else:
        return redirect(url_for('home'))

@app.route('/admin/soal')
@login_required
def admin_soal():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        data = soalController.index()
        return render_template("admin/data_soal.html", data=data, image_file=image_file)
    else:
        return redirect(url_for('home'))

@app.route('/admin/akurasi_user')
@login_required
def admin_akurasiuser():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        return render_template("admin/akurasi.html", image_file=image_file)
    else:
        return redirect(url_for('home'))

@app.route("/admin/akurasi_dataset", methods=['GET'])
@login_required
def admin_akurasidataset():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        data = decisiontree.get_xtest()
        return render_template("admin/akurasi_dataset.html", data=data, image_file=image_file)
    else:
        return redirect(url_for('home'))

@app.route("/admin/akurasi_dataset/hasilakurasi", methods=['GET'])
@login_required
def admin_hasilakurasi():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        data = decisiontree.get_akurasi()
        return render_template("admin/hasilakurasi.html", data=data, image_file=image_file)
    else:
        return redirect(url_for('home'))


@app.route("/admin/visualisasi")
@login_required
def admin_visualisasi():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        data = ml.extract_rules()
        return render_template("admin/visualisasi.html", image_file=image_file, data=data)
    else:
        return redirect(url_for('home'))

@app.route('/admin/hasiltes')
@login_required
def admin_hasiltes():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        hasil = admin.hasiltes()
        return render_template("admin/hasiltes.html", image_file=image_file, hasil=hasil)
    else:
        return redirect(url_for('home'))

@app.route('/admin/hasiltes/<int:hasil_id>')
@login_required
def admin_hasiltesinfo(hasil_id):
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        hasil = Hasiltes.query.get_or_404(hasil_id)
        deskripsi = data_tipekepribadian.query.all()
        for deskripsi in deskripsi:
            if deskripsi.tipe_kepribadian == hasil.hasil_tipekepribadian:
                hasil_deskripsi = [deskripsi.deskripsi, deskripsi.ciri_umum, deskripsi.nilai_dalam_team, deskripsi.kemungkinan_kelemahan, deskripsi.ketakutan_terbesar]
        return render_template("admin/info_userhasil.html", image_file=image_file, hasil=hasil, hasil_deskripsi=hasil_deskripsi)
    else:
        return redirect(url_for('home'))

@app.route('/admin/user')
@login_required
def admin_user():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        user = admin.user()
        form = RegistrationForm()
        return render_template("admin/user_manage.html", image_file=image_file, user=user, form=form)
    else:
        return redirect(url_for('home'))

@app.route('/admin/user/tambah', methods=['GET','POST'])
@login_required
def admin_tambahuser():
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_password, jenis_kelamin=form.jeniskelamin.data, umur=form.umur.data)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Akun Berhasil ditambahkan!', 'success')
            return redirect(url_for('admin_user'))
        return render_template("admin/tambah_user.html", image_file=image_file, form=form)
    else:
        return redirect(url_for('home'))

@app.route('/admin/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def admin_edituser(user_id):
    if current_user.roles == 'Admin':
        image_file = url_for('static', filename='img/' + current_user.image_file)
        user = User.query.get_or_404(user_id)
        form = AdminAccountForm()
        if request.method == 'POST':
            user.roles = form.roles.data
            user.fullname = form.fullname.data
            user.username = form.username.data
            user.email = form.email.data
            user.jenis_kelamin = form.jeniskelamin.data
            user.umur = form.umur.data
            try:
                db.session.commit()
                flash(f'Akun berhasil diperbarui.', 'success')
                return redirect(url_for('admin_user'))
            except:
                flash(f'Akun gagal diperbarui', 'danger')
                return redirect(url_for('admin_edituser'))
        if request.method == 'GET':
            form.roles.data = user.roles
            form.fullname.data = user.fullname
            form.username.data = user.username
            form.email.data = user.email
            form.jeniskelamin.data = user.jenis_kelamin
            form.umur.data = user.umur

        return render_template("admin/update_user.html", image_file=image_file, user=user, form=form)
    else:
        return redirect(url_for('home'))

@app.route('/admin/user/<int:user_id>/delete', methods=['POST'])
@login_required
def admin_hapususer(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()
    flash(f'Akun berhasil dihapus', 'success')
    return redirect(url_for('admin_user'))