from breadpi import BreadPi
import time
from flask import Flask
from flask_bootstrap import Bootstrap

# bread_pi = BreadPi()
#
# while True:
#     bread_pi.led_on('L1')
#     bread_pi.led_on('L2')
#     bread_pi.led_on('L3')
#     bread_pi.led_on('L4')
#     time.sleep(1)
#     bread_pi.led_off('L1')
#     bread_pi.led_off('L2')
#     bread_pi.led_off('L3')
#     bread_pi.led_off('L4')
#     time.sleep(1)


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
