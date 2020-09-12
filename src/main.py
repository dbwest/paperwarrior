from breadpi import BreadPi
import time
# from flask import Flask

bread_pi = BreadPi()

while True:
    bread_pi.led_on('L1')
    bread_pi.led_on('L2')
    bread_pi.led_on('L3')
    bread_pi.led_on('L4')
    time.sleep(1)
    bread_pi.led_off('L1')
    bread_pi.led_off('L2')
    bread_pi.led_off('L3')
    bread_pi.led_off('L4')
    time.sleep(1)


# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':

    # app.run(host='0.0.0.0', port=80)
