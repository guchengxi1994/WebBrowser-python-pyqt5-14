'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-21 10:03:55
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-21 10:10:40
'''

import socket
def check_aliveness(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(2)
    try:
        sk.connect((ip,port))
        # print ('server %s %d service is OK!' %(ip,port))
        return True
    except Exception:
        # print 'server %s %d service is NOT OK!'  %(ip,port)
        return False
    finally:
        sk.close()
    return False