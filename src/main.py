from flask import Flask
from breadpi import BreadPi
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    bread_pi = BreadPi()
    bread_pi.led_on('L1')
    bread_pi.led_on('L2')
    bread_pi.led_on('L3')
    bread_pi.led_on('L4')
    app.run(host='0.0.0.0', port=80)
