from flask import Flask, jsonify,request
from model import prediksibanjir
from model import lahan
from model import erupsi

app = Flask(__name__)



@app.route('/banjir-prediction', methods=['POST'])
def prediction1():
    input = request.json
    if input is None:
        return jsonify({
            'status': 400,
            'eror':'Prediksi tidak ditemukan!'
            }),400
    prediksi = prediksibanjir.prediksi(input)
    result = prediksi.tolist()
    data = {
        'status': 200,
        'msg':'berhasil melakukan prediksi!',
        'prediksi': result,
    }
    return jsonify(data),200

@app.route('/erupsi-prediction', methods=['POST'])
def prediction2():
    input = request.json
    if input is None:
        return jsonify({
            'status': 400,
            'eror':'Prediksi tidak ditemukan!'
            }),400
    prediksi = erupsi.prediksi(input)
    result = prediksi.tolist()
    data = {
        'status': 200,
        'msg':'berhasil melakukan prediksi!',
        'prediksi': result,
    }
    return jsonify(data),200

@app.route('/kebakaran-prediction', methods=['POST'])
def prediction3():
    input = request.json
    if input is None:
        return jsonify({
            'status': 400,
            'eror':'Prediksi tidak ditemukan!'
            }),400
    prediksi = lahan.prediksi(input)
    result = prediksi.tolist()
    data = {
        'status': 200,
        'msg':'berhasil melakukan prediksi!',
        'prediksi': result,
    }
    return jsonify(data),200

if __name__ == '__main__':
    app.run(debug=True)
