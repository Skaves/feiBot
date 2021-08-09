# 400: 'BadRequest',
# 401: 'Unauthorized',
# 403: 'Forbidden',
# 404: 'NotFound',
# 405: 'MethodNotAllowed',
# 406: 'NotAcceptable',
# 408: 'RequestTimeout',
# 409: 'Conflict',
# 410: 'Gone',
# 411: 'LengthRequired',
# 412: 'PreconditionFailed',
# 413: 'RequestEntityTooLarge',
# 414: 'RequestURITooLarge',
# 415: 'UnsupportedMediaType',
# 416: 'RequestedRangeNotSatisfiable',
# 417: 'ExpectationFailed',
# 418: 'ImATeapot',
# 422: 'UnprocessableEntity',
# 423: 'Locked',
# 424: 'FailedDependency',
# 428: 'PreconditionRequired',
# 429: 'TooManyRequests',
# 431: 'RequestHeaderFieldsTooLarge',
# 451: 'UnavailableForLegalReasons',
# 500: 'InternalServerError',
# 501: 'NotImplemented',
# 502: 'BadGateway',
# 503: 'ServiceUnavailable',
# 504: 'GatewayTimeout',
# 505: 'HTTPVersionNotSupported'


msgCode = {
    200 : {"Info" : "Done",                     "Explanation" : "服务器成功返回用户请求的数据" },
    201 : {"Info" : "CREATED",                  "Explanation" : "用户新建或修改数据成功" },
    202 : {"Info" : "Accepted",                 "Explanation" : "表示一个请求已经进入后台排队" },
    204 : {"Info" : "NO CONTENT",               "Explanation" : "用户删除数据成功" },
    300 : {"Info" : "Wrong",                    "Explanation" : "参数类型错误" },
    301 : {"Info" : "Wrong",                    "Explanation" : "参数格式错误" },
    302 : {"Info" : "Wrong",                    "Explanation" : "参数超出正常取值范围" },
    303 : {"Info" : "Token Expired",            "Explanation" : "token过期" },
    304 : {"Info" : "Invalid Token",            "Explanation" : "token无效" },
    400 : {"Info" : "INVALID REQUEST",          "Explanation" : "用户发出的请求有错误，服务器没有进行新建或修改数据的操作" },
    401 : {"Info" : "Unauthorized",             "Explanation" : "表示用户没有权限（令牌、用户名、密码错误）" },
    403 : {"Info" : "Forbidden",                "Explanation" : "表示用户得到授权（与401错误相对），但是访问是被禁止的" },
    404 : {"Info" : "NOT FOUND",                "Explanation" : "用户发出的请求针对的是不存在的记录，服务器没有进行操作" },
    406 : {"Info" : "Not Acceptable",           "Explanation" : "用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）" },
    410 : {"Info" : "Gone",                     "Explanation" : "用户请求的资源被永久删除" },
    422 : {"Info" : "Unprocesable entity",      "Explanation" : "当创建一个对象时，发生一个验证错误" },
    500 : {"Info" : "INTERNAL SERVER ERROR",    "Explanation" : "服务器发生错误，用户将无法判断发出的请求是否成功" }
}
from flask import jsonify
# from apps.urls import api as order_api

# def register_errors(app):
# @app.errorhandler(CustomErr)
def handle_flask_error(error):

    # response 的 json 内容为自定义错误代码和错误信息
    response = jsonify(error.to_dict())
    
    # response 返回 error 发生时定义的标准错误代码
    response.status_code = error.status_code
    
    return response

class CustomErr(Exception):

    status_code = 400

    def __init__(self, return_code=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict(self.payload or ())
        
        # 增加 dict key: return code
        rv['return_code'] = self.return_code
        
        # 增加 dict key: message, 具体内容由常量定义文件中通过 return_code 转化而来
        rv['message'] = msgCode[self.return_code]["Info"]
        
        # 日志打印
        # logger.warning(msgCode[self.return_code]["Explanation"])
        
        return rv
