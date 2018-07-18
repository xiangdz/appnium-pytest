# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""
'''封装钉钉群发消息f'''
import  requests,json
from  config.config_dingding import Dingtalk_access_token
def send_ding(content):
    url = Dingtalk_access_token
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "isAtAll": True
    }
    headers = {
        'Content-Type': 'application/json'
	}
    f = requests.post(url, data=json.dumps(pagrem), headers=headers)
    if f.status_code==200:
        return True
    else:
        return False