# coding: utf-8
'''
Created on 2017年10月22日

@author: raytine
'''
import requests
import json


def translate(message):
    res = requests.get('http://www.xfyun.cn/services/mtranslate/tryTranslat?from_lang=en&to_lang=cn&origin_text={}'.format(message))
    json_message = json.loads(res.content)
    result = json_message['data']['result']+'\n'
    return result