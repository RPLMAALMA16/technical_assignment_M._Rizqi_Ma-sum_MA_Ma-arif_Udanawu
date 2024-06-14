from flask import Flask, request, g, jsonify

app = Flask(__name__)

sensor_data = {}

def response_builder(success = True, message = "Respon diterima dengan baik!", data = None):
    return jsonify({
        'success': success,
        'message': message,
        'data': data
    }), 200
    
@app.before_request
def safe_json():
    g.data = None
    if 'application/json' in request.headers.get('Content-Type', ''):
        g.data = request.get_json()
    else:
        data = request.get_data().decode("utf-8")
        try:
            g.data = int(data)
        except ValueError:
            g.data = data

@app.route('/sensor/<string:sensor_name>', methods=['POST'])
def post_sensor(sensor_name):
    sensor_data[sensor_name] = g.data
    return response_builder(message="Data sensor sudah berhasil dikirim!", data=g.data)

@app.route('/sensor/<string:sensor_name>', methods=['GET'])
def get_sensor(sensor_name):
    data = sensor_data.get(sensor_name, None)
    message = "data sensor milik M.Rizqi Ma'sum berhasil terkirim!" if data is not None else "sensor tidak memiliki data!"
    success = data is not None
    return response_builder(success, message, data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)