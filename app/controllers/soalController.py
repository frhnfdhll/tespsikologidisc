from app.models.soal import Soal
from app.models.data_tk import data_tipekepribadian
from app.models.tipekepribadian import graphic_Change, graphic_Least, graphic_Most
from flask import request, flash, redirect, url_for

def index():
    soal = Soal.query.all()
    return soal

def hitung_mhasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data :
        msoal_1 = request.form['m['+ str(data[0]) +']']
        msoal_2 = request.form['m['+ str(data[1]) +']']
        msoal_3 = request.form['m['+ str(data[2]) +']']
        msoal_4 = request.form['m['+ str(data[3]) +']']
        msoal_5 = request.form['m['+ str(data[4]) +']']
        msoal_6 = request.form['m['+ str(data[5]) +']']
        msoal_7 = request.form['m['+ str(data[6]) +']']
        msoal_8 = request.form['m['+ str(data[7]) +']']
        msoal_9 = request.form['m['+ str(data[8]) +']']
        msoal_10 = request.form['m['+ str(data[9]) +']']
        msoal_11 = request.form['m['+ str(data[10]) +']']
        msoal_12 = request.form['m['+ str(data[11]) +']']
        msoal_13 = request.form['m['+ str(data[12]) +']']
        msoal_14 = request.form['m['+ str(data[13]) +']']
        msoal_15 = request.form['m['+ str(data[14]) +']']
        msoal_16 = request.form['m['+ str(data[15]) +']']
        msoal_17 = request.form['m['+ str(data[16]) +']']
        msoal_18 = request.form['m['+ str(data[17]) +']']
        msoal_19 = request.form['m['+ str(data[18]) +']']
        msoal_20 = request.form['m['+ str(data[19]) +']']
        msoal_21 = request.form['m['+ str(data[20]) +']']
        msoal_22 = request.form['m['+ str(data[21]) +']']
        msoal_23 = request.form['m['+ str(data[22]) +']']
        msoal_24 = request.form['m['+ str(data[23]) +']']

        m_hasiltes = [msoal_1, msoal_2, msoal_3, msoal_4, msoal_5, msoal_6, msoal_7, msoal_8, msoal_9, msoal_10, msoal_11, msoal_12, msoal_13, msoal_14, msoal_15, msoal_16, msoal_17, msoal_18, msoal_19, msoal_20, msoal_21, msoal_22, msoal_23, msoal_24]

        most_D = m_hasiltes.count('D')
        most_I = m_hasiltes.count('I')
        most_S = m_hasiltes.count('S')
        most_C = m_hasiltes.count('C')
        most_D_kosong = m_hasiltes.count('#D')
        most_I_kosong = m_hasiltes.count('#I')
        most_S_kosong = m_hasiltes.count('#S')
        most_C_kosong = m_hasiltes.count('#C')
        most_kosong = most_D_kosong + most_I_kosong + most_S_kosong + most_C_kosong

        most_total = most_D + most_I + most_S + most_C + most_kosong

        m_hasil = [most_D, most_I, most_S, most_C, most_kosong, most_total]

        return m_hasil

def hitung_lhasiltes():
    # data = Soal.query.order_by(Soal.id_soal).all()
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data :
        lsoal_1 = request.form['l['+ str(data[0]) +']']
        lsoal_2 = request.form['l['+ str(data[1]) +']']
        lsoal_3 = request.form['l['+ str(data[2]) +']']
        lsoal_4 = request.form['l['+ str(data[3]) +']']
        lsoal_5 = request.form['l['+ str(data[4]) +']']
        lsoal_6 = request.form['l['+ str(data[5]) +']']
        lsoal_7 = request.form['l['+ str(data[6]) +']']
        lsoal_8 = request.form['l['+ str(data[7]) +']']
        lsoal_9 = request.form['l['+ str(data[8]) +']']
        lsoal_10 = request.form['l['+ str(data[9]) +']']
        lsoal_11 = request.form['l['+ str(data[10]) +']']
        lsoal_12 = request.form['l['+ str(data[11]) +']']
        lsoal_13 = request.form['l['+ str(data[12]) +']']
        lsoal_14 = request.form['l['+ str(data[13]) +']']
        lsoal_15 = request.form['l['+ str(data[14]) +']']
        lsoal_16 = request.form['l['+ str(data[15]) +']']
        lsoal_17 = request.form['l['+ str(data[16]) +']']
        lsoal_18 = request.form['l['+ str(data[17]) +']']
        lsoal_19 = request.form['l['+ str(data[18]) +']']
        lsoal_20 = request.form['l['+ str(data[19]) +']']
        lsoal_21 = request.form['l['+ str(data[20]) +']']
        lsoal_22 = request.form['l['+ str(data[21]) +']']
        lsoal_23 = request.form['l['+ str(data[22]) +']']
        lsoal_24 = request.form['l['+ str(data[23]) +']']

        l_hasiltes = [lsoal_1, lsoal_2, lsoal_3, lsoal_4, lsoal_5, lsoal_6, lsoal_7, lsoal_8, lsoal_9, lsoal_10, lsoal_11, lsoal_12, lsoal_13, lsoal_14, lsoal_15, lsoal_16, lsoal_17, lsoal_18, lsoal_19, lsoal_20, lsoal_21, lsoal_22, lsoal_23, lsoal_24]

        least_D = l_hasiltes.count('D')
        least_I = l_hasiltes.count('I')
        least_S = l_hasiltes.count('S')
        least_C = l_hasiltes.count('C')
        least_D_kosong = l_hasiltes.count('#D')
        least_I_kosong = l_hasiltes.count('#I')
        least_S_kosong = l_hasiltes.count('#S')
        least_C_kosong = l_hasiltes.count('#C')
        least_kosong = least_D_kosong + least_I_kosong + least_S_kosong + least_C_kosong

        least_total = least_D + least_I + least_S + least_C + least_kosong

        l_hasil = [least_D, least_I, least_S, least_C, least_kosong, least_total]

        return l_hasil

def hitung_chasiltes():
    m_hasil = hitung_mhasiltes()
    l_hasil = hitung_lhasiltes()
    change_D = m_hasil[0] - l_hasil[0]
    change_I = m_hasil[1] - l_hasil[1]
    change_S = m_hasil[2] - l_hasil[2]
    change_C = m_hasil[3] - l_hasil[3]

    c_hasil = [change_D, change_I, change_S, change_C]

    return c_hasil

def hasilskor_dominance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Dominance
    for data_graph in data_graph:
        if c_hasil[0] == data_graph.change_d:
            skor_dominance = data_graph.skor
            return skor_dominance

def hasilskor_influance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Influance
    for data_graph in data_graph:
        if c_hasil[1] == data_graph.change_i:
            skor_influance = data_graph.skor
            return skor_influance

def hasilskor_steadiness():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Steadiness
    for data_graph in data_graph:
        if c_hasil[2] == data_graph.change_s:
            skor_steadiness = data_graph.skor
            return skor_steadiness

def hasilskor_compliance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Compliance
    for data_graph in data_graph:
        if c_hasil[3] == data_graph.change_c:
            skor_compliance = data_graph.skor
            return skor_compliance

def hasilskor_dominance_most():
    m_hasil = hitung_mhasiltes()
    data_graph = graphic_Most.query.all()
    # Dominance
    for data_graph in data_graph:
        if m_hasil[0] == data_graph.most_d:
            skor_dominance_most = data_graph.skor
            return skor_dominance_most

def hasilskor_influance_most():
    m_hasil = hitung_mhasiltes()
    data_graph = graphic_Most.query.all()
    # influance
    for data_graph in data_graph:
        if m_hasil[1] == data_graph.most_i:
            skor_influance_most = data_graph.skor
            return skor_influance_most

def hasilskor_steadiness_most():
    m_hasil = hitung_mhasiltes()
    data_graph = graphic_Most.query.all()
    # steadiness
    for data_graph in data_graph:
        if m_hasil[2] == data_graph.most_s:
            skor_steadiness_most = data_graph.skor
            return skor_steadiness_most

def hasilskor_compliance_most():
    m_hasil = hitung_mhasiltes()
    data_graph = graphic_Most.query.all()
    # compliance
    for data_graph in data_graph:
        if m_hasil[3] == data_graph.most_c:
            skor_compliance_most = data_graph.skor
            return skor_compliance_most

def hasilskor_dominance_least():
    l_hasil = hitung_lhasiltes()
    data_graph = graphic_Least.query.all()
    # dominance
    for data_graph in data_graph:
        if l_hasil[0] == data_graph.least_d:
            skor_dominance_least = data_graph.skor
            return skor_dominance_least

def hasilskor_influance_least():
    l_hasil = hitung_lhasiltes()
    data_graph = graphic_Least.query.all()
    # influance
    for data_graph in data_graph:
        if l_hasil[1] == data_graph.least_i:
            skor_influance_least = data_graph.skor
            return skor_influance_least

def hasilskor_steadiness_least():
    l_hasil = hitung_lhasiltes()
    data_graph = graphic_Least.query.all()
    # steadiness
    for data_graph in data_graph:
        if l_hasil[2] == data_graph.least_s:
            skor_steadiness_least = data_graph.skor
            return skor_steadiness_least

def hasilskor_compliance_least():
    l_hasil = hitung_lhasiltes()
    data_graph = graphic_Least.query.all()
    # compliance
    for data_graph in data_graph:
        if l_hasil[3] == data_graph.least_c:
            skor_compliance_least = data_graph.skor
            return skor_compliance_least

def bagian_dominance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Dominance
    for data_graph in data_graph:
        if c_hasil[0] == data_graph.change_d:
            bagian_dominance = data_graph.bagian
            return bagian_dominance

def bagian_influance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Influance
    for data_graph in data_graph:
        if c_hasil[1] == data_graph.change_i:
            bagian_influance = data_graph.bagian
            return bagian_influance

def bagian_steadiness():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Steadiness
    for data_graph in data_graph:
        if c_hasil[2] == data_graph.change_s:
            bagian_steadiness = data_graph.bagian
            return bagian_steadiness

def bagian_compliance():
    c_hasil = hitung_chasiltes()
    data_graph = graphic_Change.query.all()
    # Compliance
    for data_graph in data_graph:
        if c_hasil[3] == data_graph.change_c:
            bagian_compliance = data_graph.bagian
            return bagian_compliance

def hasil_tipekepribadian():
    c_hasil = hitung_chasiltes()

    dominance = bagian_dominance()
    dominance_skor = hasilskor_dominance()
    c_hasil_dominance = c_hasil[0]

    influance = bagian_influance()
    influance_skor = hasilskor_influance()
    c_hasil_influance = c_hasil[1]

    steadiness = bagian_steadiness()
    steadiness_skor = hasilskor_steadiness()
    c_hasil_steadiness = c_hasil[2]

    compliance = bagian_compliance()
    compliance_skor = hasilskor_compliance()
    c_hasil_compliance = c_hasil[3]

    # Dominance
    if (dominance - influance > 3) and (dominance - steadiness > 3) and (dominance - compliance > 3):
        hasil_tipekepribadian = 'dominance'
    # Dominance Influance
    if (dominance - influance<=3) and (dominance - steadiness>3) and (dominance - compliance>3):
        if (dominance > influance):
            hasil_tipekepribadian = 'dominance influance'
        if (dominance == influance):
            if dominance_skor > influance_skor:
                hasil_tipekepribadian = 'dominance influance'
            if dominance_skor == influance_skor:
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance'
    # Dominance Steadiness
    if (dominance - influance>3) and (dominance - steadiness<=3) and (dominance - compliance>3):
        if (dominance > steadiness):
            hasil_tipekepribadian = 'dominance steadiness'
        if (dominance == steadiness):
            if dominance_skor > steadiness_skor:
                hasil_tipekepribadian = 'dominance steadiness'
            if dominance_skor == steadiness_skor:
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness'
    # Dominance Compliance
    if (dominance - influance>3) and (dominance - steadiness>3) and (dominance - compliance<=3):
        if (dominance > compliance):
            hasil_tipekepribadian = 'dominance compliance'
        if (dominance == compliance):
            if dominance_skor > compliance_skor:
                hasil_tipekepribadian = 'dominance compliance'
            if dominance_skor == compliance_skor:
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance'
    # Dominance Influance Steadiness
    if (dominance-influance<=3) and (dominance-steadiness<=3):
        if (dominance > influance > steadiness > compliance):
            hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance == influance > steadiness > compliance):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance > influance == steadiness > compliance):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance > influance > steadiness == compliance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance == influance == steadiness > compliance):
            if (dominance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance > influance == steadiness == compliance):
            if (influance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (influance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance == influance > steadiness == compliance):
            if (dominance_skor > influance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor > steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
        if (dominance == influance == steadiness == compliance):
            if (dominance_skor > influance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor > steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor > influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
            if (dominance_skor == influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance steadiness'
    # Dominance Influance Compliance
    if (dominance-influance<=3) and (dominance-compliance<=3):
        if (dominance > influance > compliance > steadiness):
            hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance == influance > compliance > steadiness):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance > influance == compliance > steadiness):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance > influance > compliance == steadiness):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance == influance == compliance > steadiness):
            if (dominance_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance > influance == compliance == steadiness):
            if (influance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (influance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance == influance > compliance == steadiness):
            if (dominance_skor > influance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor > compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
        if (dominance == influance == compliance == steadiness):
            if (dominance_skor > influance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor > compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor > influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
            if (dominance_skor == influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance influance compliance'
    # Dominance Steadiness Influance
    if (dominance-steadiness<=3) and (dominance-influance<=3):
        if (dominance > steadiness > influance > compliance):
            hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance == steadiness > influance > compliance):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance > steadiness == influance > compliance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance > steadiness > influance == compliance):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance == steadiness == influance > compliance):
            if (dominance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance > steadiness == influance == compliance):
            if (steadiness_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (steadiness_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance == steadiness > influance == compliance):
            if (dominance_skor > steadiness_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor > influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
        if (dominance == steadiness == influance == compliance):
            if (dominance_skor > steadiness_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor > influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor > steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
            if (dominance_skor == steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness influance'
    # Dominance Steadiness Compliance
    if (dominance-steadiness<=3) and (dominance-compliance<=3):
        if (dominance > steadiness > compliance > influance):
            hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance == steadiness > compliance > influance):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance > steadiness == compliance > influance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance > steadiness > compliance == influance):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance == steadiness == compliance > influance):
            if (dominance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance > steadiness == compliance == influance):
            if (steadiness_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (steadiness_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance == steadiness > compliance == influance):
            if (dominance_skor > steadiness_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor > compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
        if (dominance == steadiness == compliance == influance):
            if (dominance_skor > steadiness_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor > compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor > steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
            if (dominance_skor == steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance steadiness compliance'
    # Dominance Compliance Influance
    if (dominance-compliance<=3) and (dominance-influance<=3):
        if (dominance > compliance > influance > steadiness):
            hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance == compliance > influance > steadiness):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance > compliance == influance > steadiness):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance > compliance > influance == steadiness):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance == compliance == influance > steadiness):
            if (dominance_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance > compliance == influance == steadiness):
            if (compliance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (compliance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance == compliance > influance == steadiness):
            if (dominance_skor > compliance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor > influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
        if (dominance == compliance == influance == steadiness):
            if (dominance_skor > compliance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor > influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor > compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
            if (dominance_skor == compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance influance'
    # Dominance Compliance Steadiness
    if (dominance-compliance<=3) and (dominance-steadiness<=3):
        if (dominance > compliance > steadiness > influance):
            hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance == compliance > steadiness > influance):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance > compliance == steadiness > influance):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance > compliance > steadiness == influance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance == compliance == steadiness > influance):
            if (dominance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance > compliance == steadiness == influance):
            if (compliance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (compliance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance == compliance > steadiness == influance):
            if (dominance_skor > compliance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor > steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
        if (dominance == compliance == steadiness == influance):
            if (dominance_skor > compliance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor > steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor > compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'
            if (dominance_skor == compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'dominance compliance steadiness'

    # Influance
    if (influance-dominance>3) and (influance-steadiness>3) and (influance-compliance>3):
        hasil_tipekepribadian = 'influance'
    # Influance Dominance
    if (influance - dominance<=3) and (influance - steadiness>3) and (influance - compliance>3):
        if (influance > dominance):
            hasil_tipekepribadian = 'influance dominance'
        if (influance == dominance):
            if influance_skor > dominance_skor:
                hasil_tipekepribadian = 'influance dominance'
            if influance_skor == dominance_skor:
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance'
    # Influance Steadiness
    if (influance - steadiness<=3) and (influance - compliance>3) and (influance - dominance>3):
        if (influance > steadiness):
            hasil_tipekepribadian = 'influance steadiness'
        if (influance == steadiness):
            if influance_skor > steadiness_skor:
                hasil_tipekepribadian = 'influance steadiness'
            if influance_skor == steadiness_skor:
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness'
    # Influance Compliance
    if (influance - compliance<=3) and (influance - dominance>3) and (influance - steadiness>3):
        if (influance > compliance):
            hasil_tipekepribadian = 'influance compliance'
        if (influance == compliance):
            if influance_skor > compliance_skor:
                hasil_tipekepribadian = 'influance compliance'
            if influance_skor == compliance_skor:
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance'
    # Influance Dominance Steadiness
    if (influance-dominance<=3) and (influance-steadiness<=3):
        if (influance > dominance > steadiness > compliance):
            hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance == dominance > steadiness > compliance):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance > dominance == steadiness > compliance):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance > dominance > steadiness == compliance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance == dominance == steadiness > compliance):
            if (influance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance > dominance == steadiness == compliance):
            if (dominance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (dominance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance == dominance > steadiness == compliance):
            if (influance_skor > dominance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor > steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
        if (influance == dominance == steadiness == compliance):
            if (influance_skor > dominance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor > steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor > dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
            if (influance_skor == dominance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance steadiness'
    # Influance Dominance Compliance
    if (influance-dominance<=3) and (influance-compliance<=3):
        if (influance > dominance > compliance > steadiness):
            hasil_tipekepribadian = 'influance dominance compliance'
        if (influance == dominance > compliance > steadiness):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance > dominance == compliance > steadiness):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance > dominance > compliance == steadiness):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance == dominance == compliance > steadiness):
            if (influance_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance > dominance == compliance == steadiness):
            if (dominance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (dominance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance == dominance > compliance == steadiness):
            if (influance_skor > dominance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor > compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
        if (influance == dominance == compliance == steadiness):
            if (influance_skor > dominance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor > compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor > dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
            if (influance_skor == dominance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance dominance compliance'
    # Influance Steadiness Dominance
    if (influance-steadiness<=3) and (influance-dominance<=3):
        if (influance > steadiness > dominance > compliance):
            hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance == steadiness > dominance > compliance):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance > steadiness == dominance > compliance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance > steadiness > dominance == compliance):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance == steadiness == dominance > compliance):
            if (influance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance > steadiness == dominance == compliance):
            if (steadiness_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (steadiness_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance == steadiness > dominance == compliance):
            if (influance_skor > steadiness_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor > dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
        if (influance == steadiness == dominance == compliance):
            if (influance_skor > steadiness_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor > dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor > steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
            if (influance_skor == steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness dominance'
    # Influance Steadiness Compliance
    if (influance-steadiness<=3) and (influance-compliance<=3):
        if (influance > steadiness > compliance > dominance):
            hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance == steadiness > compliance > dominance):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance > steadiness == compliance > dominance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance > steadiness > compliance == dominance):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance == steadiness == compliance > dominance):
            if (influance_skor > steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance > steadiness == compliance == dominance):
            if (steadiness_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (steadiness_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance == steadiness > compliance == dominance):
            if (influance_skor > steadiness_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor > compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
        if (influance == steadiness == compliance == dominance):
            if (influance_skor > steadiness_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor > compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor > steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
            if (influance_skor == steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance steadiness compliance'
    # Influance Compliance Dominance
    if (influance-compliance<=3) and (influance-dominance<=3):
        if (influance > compliance > dominance > steadiness):
            hasil_tipekepribadian = 'influance compliance dominance'
        if (influance == compliance > dominance > steadiness):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance > compliance == dominance > steadiness):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance > compliance > dominance == steadiness):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance == compliance == dominance > steadiness):
            if (influance_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance > compliance == dominance == steadiness):
            if (compliance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (compliance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance == compliance > dominance == steadiness):
            if (influance_skor > compliance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor > dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
        if (influance == compliance == dominance == steadiness):
            if (influance_skor > compliance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor > dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor > compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
            if (influance_skor == compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance dominance'
    # Influance Compliance Steadiness
    if (influance-compliance<=3) and (influance-steadiness<=3):
        if (influance > compliance > steadiness > dominance):
            hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance == compliance > steadiness > dominance):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance > compliance == steadiness > dominance):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance > compliance > steadiness == dominance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance == compliance == steadiness > dominance):
            if (influance_skor > compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance > compliance == steadiness == dominance):
            if (compliance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (compliance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance == compliance > steadiness == dominance):
            if (influance_skor > compliance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor > steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
        if (influance == compliance == steadiness == dominance):
            if (influance_skor > compliance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor > steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor > compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
            if (influance_skor == compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'influance compliance steadiness'
    
    # Steadiness
    if (steadiness-dominance>3) and (steadiness-influance>3) and (steadiness-compliance>3):
        hasil_tipekepribadian = 'steadiness'
    # Steadiness Dominance
    if (steadiness - dominance<=3) and (steadiness - influance>3) and (steadiness - compliance>3):
        if (steadiness > dominance):
            hasil_tipekepribadian = 'steadiness dominance'
        if (steadiness == dominance):
            if steadiness_skor > dominance_skor:
                hasil_tipekepribadian = 'steadiness dominance'
            if steadiness_skor == dominance_skor:
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance'
    # Steadiness Influance
    if (steadiness - influance<=3) and (steadiness - dominance>3) and (steadiness - compliance>3):
        if (steadiness > influance):
            hasil_tipekepribadian = 'steadiness influance'
        if (steadiness == influance):
            if steadiness_skor > influance_skor:
                hasil_tipekepribadian = 'steadiness influance'
            if steadiness_skor == influance_skor:
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance'
    # Steadiness Compliance
    if (steadiness - compliance<=3) and (steadiness - dominance>3) and (steadiness - influance>3):
        if (steadiness > compliance):
            hasil_tipekepribadian = 'steadiness compliance'
        if (steadiness == compliance):
            if steadiness_skor > compliance_skor:
                hasil_tipekepribadian = 'steadiness compliance'
            if steadiness_skor == compliance_skor:
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance'
    # Steadiness Dominance Influance
    if (steadiness-dominance<=3) and (steadiness-influance<=3):
        if (steadiness > dominance > influance > compliance):
            hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness == dominance > influance > compliance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness > dominance == influance > compliance):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness > dominance > influance == compliance):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness == dominance == influance > compliance):
            if (steadiness_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness > dominance == influance == compliance):
            if (dominance_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (dominance_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness == dominance > influance == compliance):
            if (steadiness_skor > dominance_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor > influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
        if (steadiness == dominance == influance == compliance):
            if (steadiness_skor > dominance_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor > influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor == influance_skor > compliance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor > dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
            if (steadiness_skor == dominance_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance influance'
    # Steadiness Dominance Compliance
    if (steadiness-dominance<=3) and (steadiness-compliance<=3):
        if (steadiness > dominance > compliance > influance):
            hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness == dominance > compliance > influance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness > dominance == compliance > influance):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness > dominance > compliance == influance):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness == dominance == compliance > influance):
            if (steadiness_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness > dominance == compliance == influance):
            if (dominance_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (dominance_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness == dominance > compliance == influance):
            if (steadiness_skor > dominance_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor > compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
        if (steadiness == dominance == compliance == influance):
            if (steadiness_skor > dominance_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor > compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor == compliance_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor > dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
            if (steadiness_skor == dominance_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness dominance compliance'
    # Steadiness Influance Dominance
    if (steadiness-influance<=3) and (steadiness-dominance<=3):
        if (steadiness > influance > dominance > compliance):
            hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness == influance > dominance > compliance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness > influance == dominance > compliance):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness > influance > dominance == compliance):
            if (dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness == influance == dominance > compliance):
            if (steadiness_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness > influance == dominance == compliance):
            if (influance_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (influance_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness == influance > dominance == compliance):
            if (steadiness_skor > influance_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor > dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
        if (steadiness == influance == dominance == compliance):
            if (steadiness_skor > influance_skor > dominance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor > dominance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor > dominance_skor == compliance_skor):
                if (c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor == dominance_skor > compliance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor > influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
            if (steadiness_skor == influance_skor == dominance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance dominance'
    # Steadiness Influance Compliance
    if (steadiness-influance<=3) and (steadiness-compliance<=3):
        if (steadiness > influance > compliance > dominance):
            hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness == influance > compliance > dominance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness > influance == compliance > dominance):
            if (influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness > influance > compliance == dominance):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness == influance == compliance > dominance):
            if (steadiness_skor > influance_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor > compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor == compliance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness > influance == compliance == dominance):
            if (influance_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (influance_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness == influance > compliance == dominance):
            if (steadiness_skor > influance_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor > compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
        if (steadiness == influance == compliance == dominance):
            if (steadiness_skor > influance_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor > compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor == compliance_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor > influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
            if (steadiness_skor == influance_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness influance compliance'
    # Steadiness Compliance Dominance
    if (steadiness-compliance<=3) and (steadiness-dominance<=3):
        if (steadiness > compliance > dominance > influance):
            hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness == compliance > dominance > influance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness > compliance == dominance > influance):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness > compliance > dominance == influance):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness == compliance == dominance > influance):
            if (steadiness_skor > compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness > compliance == dominance == influance):
            if (compliance_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (compliance_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness == compliance > dominance == influance):
            if (steadiness_skor > compliance_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor > dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
        if (steadiness == compliance == dominance == influance):
            if (steadiness_skor > compliance_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor > dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor > compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
            if (steadiness_skor == compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance dominance'
    # Steadiness Compliance Influance
    if (steadiness-compliance<=3) and (steadiness-influance<=3):
        if (steadiness > compliance > influance > dominance):
            hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness == compliance > influance > dominance):
            if (steadiness_skor > compliance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness > compliance == influance > dominance):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness > compliance > influance == dominance):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness == compliance == influance > dominance):
            if (steadiness_skor > compliance_skor > influance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness > compliance == influance == dominance):
            if (compliance_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (compliance_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness == compliance > influance == dominance):
            if (steadiness_skor > compliance_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor > influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
        if (steadiness == compliance == influance == dominance):
            if (steadiness_skor > compliance_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor > influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor > compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
            if (steadiness_skor == compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'steadiness compliance influance'
    
    # Compliance
    if (compliance-dominance>3) and (compliance-steadiness>3) and (compliance-influance>3):
        hasil_tipekepribadian = 'compliance'
    # Compliance Dominance
    if (compliance-dominance<=3) and (compliance-steadiness>3) and (compliance-influance>3):
        if (compliance > dominance):
            hasil_tipekepribadian = 'compliance dominance'
        if (compliance == dominance):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance dominance'
            if compliance_skor == dominance_skor:
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance'
    # Compliance Influance
    if (compliance-dominance>3) and (compliance-steadiness>3) and (compliance-influance<=3):
        if (compliance > influance):
            hasil_tipekepribadian = 'compliance influance'
        if (compliance == influance):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance influance'
            if compliance_skor == influance_skor:
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance'
    # Compliance Steadiness
    if (compliance-dominance>3) and (compliance-steadiness<=3) and (compliance-influance>3):
        if (compliance > steadiness):
            hasil_tipekepribadian = 'compliance steadiness'
        if (compliance == steadiness):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance steadiness'
            if compliance_skor == steadiness_skor:
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness'
    # Compliance Dominance Influance
    if (compliance-dominance<=3) and (compliance-influance<=3):
        if (compliance > dominance > influance > steadiness):
            hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance == dominance > influance > steadiness):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance > dominance == influance > steadiness):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance > dominance > influance == steadiness):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance == dominance == influance > steadiness):
            if (compliance_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance > dominance == influance == steadiness):
            if (dominance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (dominance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance == dominance > influance == steadiness):
            if (compliance_skor > dominance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor > influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
        if (compliance == dominance == influance == steadiness):
            if (compliance_skor > dominance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor > influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor == influance_skor > steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor > dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
            if (compliance_skor == dominance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance influance'
    # Compliance Dominance Steadiness
    if (compliance-dominance<=3) and (compliance-steadiness<=3):
        if (compliance > dominance > steadiness > influance):
            hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance == dominance > steadiness > influance):
            if (compliance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance > dominance == steadiness > influance):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance > dominance > steadiness == influance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance == dominance == steadiness > influance):
            if (compliance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance > dominance == steadiness == influance):
            if (dominance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (dominance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance == dominance > steadiness == influance):
            if (compliance_skor > dominance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor > steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
        if (compliance == dominance == steadiness == influance):
            if (compliance_skor > dominance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor > steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor == steadiness_skor > influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor > dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
            if (compliance_skor == dominance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_dominance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance dominance steadiness'
    # Compliance Influance Dominance
    if (compliance-influance<=3) and (compliance-dominance<=3):
        if (compliance > influance > dominance > steadiness):
            hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance == influance > dominance > steadiness):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance > influance == dominance > steadiness):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance > influance > dominance == steadiness):
            if (dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance == influance == dominance > steadiness):
            if (compliance_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance > influance == dominance == steadiness):
            if (influance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (influance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance == influance > dominance == steadiness):
            if (compliance_skor > influance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor > dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
        if (compliance == influance == dominance == steadiness):
            if (compliance_skor > influance_skor > dominance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor > dominance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor > dominance_skor == steadiness_skor):
                if (c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor == dominance_skor > steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor > influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
            if (compliance_skor == influance_skor == dominance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_dominance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance dominance'
    # Compliance Influance Steadiness
    if (compliance-influance<=3) and (compliance-steadiness<=3):
        if (compliance > influance > steadiness > dominance):
            hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance == influance > steadiness > dominance):
            if (compliance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance > influance == steadiness > dominance):
            if (influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance > influance > steadiness == dominance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance == influance == steadiness > dominance):
            if (compliance_skor > influance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor > steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor == steadiness_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance > influance == steadiness == dominance):
            if (influance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (influance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance == influance > steadiness == dominance):
            if (compliance_skor > influance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor > steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
        if (compliance == influance == steadiness == dominance):
            if (compliance_skor > influance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor > steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor > influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
            if (compliance_skor == influance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_influance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance influance steadiness'
    # Compliance Steadiness Dominance
    if (compliance-steadiness<=3) and (compliance-dominance<=3):
        if (compliance > steadiness > dominance > influance):
            hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance == steadiness > dominance > influance):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance > steadiness == dominance > influance):
            if (steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance > steadiness > dominance == influance):
            if (dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance == steadiness == dominance > influance):
            if (compliance_skor > steadiness_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance > steadiness == dominance == influance):
            if (steadiness_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (steadiness_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance == steadiness > dominance == influance):
            if (compliance_skor > steadiness_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor > dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
        if (compliance == steadiness == dominance == influance):
            if (compliance_skor > steadiness_skor > dominance_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor > dominance_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor > dominance_skor == influance_skor):
                if (c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor == dominance_skor > influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor > steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
            if (compliance_skor == steadiness_skor == dominance_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_dominance > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness dominance'
    # Compliance Steadiness Influance
    if (compliance-steadiness<=3) and (compliance-influance<=3):
        if (compliance > steadiness > influance > dominance):
            hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance == steadiness > influance > dominance):
            if (compliance_skor > steadiness_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance > steadiness == influance > dominance):
            if (steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance > steadiness > influance == dominance):
            if (influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance == steadiness == influance > dominance):
            if (compliance_skor > steadiness_skor > influance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor > influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor == influance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor == influance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance > steadiness == influance == dominance):
            if (steadiness_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (steadiness_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance == steadiness > influance == dominance):
            if (compliance_skor > steadiness_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor > influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
        if (compliance == steadiness == influance == dominance):
            if (compliance_skor > steadiness_skor > influance_skor > dominance_skor):
                hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor > influance_skor > dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor > influance_skor == dominance_skor):
                if (c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor == influance_skor > dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor > steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
            if (compliance_skor == steadiness_skor == influance_skor == dominance_skor):
                if (c_hasil_compliance > c_hasil_steadiness > c_hasil_influance > c_hasil_dominance):
                    hasil_tipekepribadian = 'compliance steadiness influance'
    
    
    return hasil_tipekepribadian

def deskripsikepribadian():
    hasil = hasil_tipekepribadian()
    deskripsi_hasil = data_tipekepribadian.query.all()
    for deskripsi_hasil in deskripsi_hasil:
        if deskripsi_hasil.tipe_kepribadian == hasil:
            hasil_deskripsi = [deskripsi_hasil.deskripsi, deskripsi_hasil.ciri_umum, deskripsi_hasil.nilai_dalam_team, deskripsi_hasil.kemungkinan_kelemahan, deskripsi_hasil.ketakutan_terbesar]
            
            return hasil_deskripsi
