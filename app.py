from flask import Flask, jsonify,request
from model import prediksibanjir

app = Flask(__name__)



@app.route('/prediction', methods=['POST'])
def prediction():
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

if __name__ == '__main__':
    app.run(debug=True)
