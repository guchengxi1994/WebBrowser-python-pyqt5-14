'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:29:09
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-20 16:15:09
'''
from flask import Flask, request,render_template
from flask_cors import CORS,cross_origin
import json

# app = Flask(__name__)

app = Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True, resources=r'/*')

@app.route('/')
def hello_world():
    return 'hello World'

@app.route("/showImg")
def showImage():
    import base64
    # imgName = json.loads(request.get_data())['imgname']
    
    try:
        # imgName = json.loads(request.get_data())['imgname']
        imgName = request.args.get("imgName")
        print(imgName)

    except Exception:
        imgName = "D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\test1.png"
    
    print(imgName)
    
    with open(imgName,'rb') as f:
            # new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        base64_data = base64.b64encode(f.read()).decode("utf-8")
        # imgName = "./static/test.png"
        return render_template("index.html", user_image = base64_data)
    

# 主程序入口
if __name__ == '__main__':
    app.run(debug=True)
