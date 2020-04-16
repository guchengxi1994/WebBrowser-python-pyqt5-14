'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-16 16:54:07
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-16 17:04:26
'''

import re

def judge(path:str):
    """
    判断网址是不是满足正则表达式
    """
    pattern = r"^(http://)|(https://){0,1}[A-Za-z0-9][A-Za-z0-9\-\.]+[A-Za-z0-9]\.[A-Za-z]{2,}[\43-\176]*$"
    
    # return(re.match(pattern,path))
    if re.match(pattern,path) is not None:
        return True
    else :
        return False

    # print(s)


if __name__ == "__main__":
    path = "www.baidu.com"
    print(judge(path))