'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:29:09
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-22 10:44:33
'''
from flask import Flask, request,render_template
from flask_cors import CORS,cross_origin
import json
import os
from utils.analyse import plotFigureWithLabels as pf
import base64


# app = Flask(__name__)

app = Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True, resources=r'/*')

# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp


# app.after_request(after_request)

@app.route('/')
def hello_world():
    return 'hello World'

def img2base64(imgPath):
     with open(imgPath,'rb') as f:
                # new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        base64_data = base64.b64encode(f.read()).decode("utf-8")
            # imgName = "./static/test.png"
        return base64_data
    

@app.route("/changeImg",methods=['POST',"GET"])
def change():
    print("---change---")
    # print(request.get_data())
    resData = {}
    if 'POST' == request.method:
        try:
            xstick = json.loads(request.get_data())['xstick']
            # print(xstick)
            ystick = json.loads(request.get_data())['ystick']
            # print(ystick)
            figLoc = json.loads(request.get_data())['figLoc']
            # print(figLoc)
            imgName = json.loads(request.get_data())['imgName']
            # print(imgName)
            dataPath = json.loads(request.get_data())['dataPath']
            # print(dataPath)
            sheetName = json.loads(request.get_data())['sheetName']
            # print(sheetName)

            figurePath = pf(dataPath,sheetName,xstick=xstick,ystick=ystick)



            resData['resultCode'] = 200
            resData['figurePath'] = figurePath
            resData['figureData'] = img2base64(figurePath)
            return json.dumps(resData)
        except Exception as e:
            print(e)
            resData['resultCode'] = 500
            return json.dumps(resData)
        
    else:
        return "ERROR"


    
    


@app.route("/showImg",methods=['POST',"GET"])
def showImage():
    
    # print(request.args)
    # imgName = json.loads(request.get_data())['imgname']
    
    if "GET" == request.method:
        try:
            # imgName = json.loads(request.get_data())['imgname']
            imgName = request.args.get("imgName")
            dataPath = request.args.get("dataPath")
            sheetName = request.args.get("sheetName")
            # print(imgName)
            if os.path.exists(imgName):
                pass
            else:
                raise FileNotFoundError('文件不存在')

        except Exception:
            imgName = "D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\test1.png"
            dataPath = "D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\data.xls"
            sheetName = "Sheet1"
        
        # print(imgName)
        
        with open(imgName,'rb') as f:
                # new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            base64_data = base64.b64encode(f.read()).decode("utf-8")
            # imgName = "./static/test.png"
            return render_template("index.html", user_image = base64_data,imgName = imgName,dataPath = dataPath,sheetName=sheetName)
    
    elif 'POST' == request.method:
        # print(request.get_data())
        resData = {}
        try:
            xstick = json.loads(request.get_data())['xstick']
            ystick = json.loads(request.get_data())['ystick']
            figLoc = json.loads(request.get_data())['figLoc']
            imgName = json.loads(request.get_data())['imgName']
            # print(xstick)
            # print(ystick)
            # print(figLoc)
            resData['resultCode'] = 200
            return json.dumps(resData)
        except Exception as e:
            print(e)
            resData['resultCode'] = 500
            return json.dumps(resData)
    
    else:
        return "ERROR"

    

# 主程序入口
if __name__ == '__main__':
    app.run(debug=True)
