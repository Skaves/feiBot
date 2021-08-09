#encoding:utf-8
from setup import create_app
from flask import request,abort

app = create_app()

@app.route('/')
def index():
    print(app.config)
    return "hello"


@app.before_request
def print_request_info():
    if app.config['SHOW_HEADERS']:
        print("请求地址：" + str(request.path))
        print("请求方法：" + str(request.method))
        print("---请求headers--start--")
        print(str(request.headers).rstrip())
        print("---请求headers--end----")
        print("GET参数：" + str(request.args))
        print("POST参数：" + str(request.form))


# @app.before_request
# def auth():
#     token = request.headers.get('Authorization')
#     print(token)
#     if not token:
#         abort(401)
    


if __name__ == '__main__':
    app.run(threaded=True, use_reloader=False, host='0.0.0.0', port=6888)
    
