from flask import Flask, render_template, make_response, jsonify
from functools import wraps
# from flask_cache import Cache
# import cx_Oracle

app = Flask(__name__)

# app configuration
app.config['SECRET_KEY'] = '!@$RFGAVASDGAQQQ'



def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


@app.route('/')
@allow_cross_domain
@cache.cached(timeout=2, key_prefix='random')
def index():
    sql_string = "SELECT distinct USERID FROM BLITZSTAT.STG_IS_SESSION_STATS"
    cursor.execute(sql_string)
    row = cursor.fetchall()
    userCount = len(row)

    data = {'data': userCount, 'users': row}
    return jsonify(data)


@app.route('/test/')
def test():
    return render_template('test.htm')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
