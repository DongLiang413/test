# -*- encoding=UTF-8 -*-

#
# content = requests.get('http://www.qiushibaike.com').content
# print 1
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'LYM'


@app.route('/profile/<uid>')
def profile(uidS):
    return 'uid: ' + uid

# def demo_list():
#     lsa = [1.1, 'a', '3']
#     print 1, lsa
#     lsb = [1.1, 2.2]
#     print 2, lsb


# list set dictionary
if __name__ == '__main__':
    print 'LYM'
    app.run(debug = True)