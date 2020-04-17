'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:29:09
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 08:31:11
'''
from flask import Flask, request
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

@app.route('/')
def hello_world():
    return 'hello Junrui'

# 主程序入口
if __name__ == '__main__':
    app.run(debug=True)
