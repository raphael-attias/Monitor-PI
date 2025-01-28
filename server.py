from flask import Flask, jsonify, render_template
import psutil
import subprocess
from collections import deque

app = Flask(__name__)

CAPTURE_FILE = '/var/captures/capture.pcap'
MAX_HISTORY = 75

history = {
    'cpuTemp': deque(maxlen=MAX_HISTORY),
    'gpuTemp': deque(maxlen=MAX_HISTORY),
    'upload': deque(maxlen=MAX_HISTORY),
    'download': deque(maxlen=MAX_HISTORY),
    'cpuUsage': deque(maxlen=MAX_HISTORY),
    'gpuUsage': deque(maxlen=MAX_HISTORY),
    'ramUsage': deque(maxlen=MAX_HISTORY)
}

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/data')
def get_stats():
    try:
        cpu_temp = float(subprocess.getoutput("vcgencmd measure_temp").split('=')[1][:-2])
    except Exception:
        cpu_temp = 0.0
    try:
        gpu_temp = round(int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000, 1)
    except Exception:
        gpu_temp = 0.0

    upload = 0.0
    download = 0.0

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    gpu_usage = 0

    history['cpuTemp'].append(cpu_temp)
    history['gpuTemp'].append(gpu_temp)
    history['upload'].append(upload)
    history['download'].append(download)
    history['cpuUsage'].append(cpu_usage)
    history['gpuUsage'].append(gpu_usage)
    history['ramUsage'].append(ram_usage)

    packets = []

    return jsonify(
        cpuTemp=list(history['cpuTemp']),
        gpuTemp=list(history['gpuTemp']),
        upload=list(history['upload']),
        download=list(history['download']),
        cpuUsage=list(history['cpuUsage']),
        gpuUsage=list(history['gpuUsage']),
        ramUsage=list(history['ramUsage']),
        packets=packets
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
