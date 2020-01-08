#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
报错 ：json 'str' object has no attribute 'read'
只需要将json.load()换成json.loads()就可以了 
'''

from cloudxns.api import *
try:
    import json
except ImportError:
    import simplejson as json

if __name__ == '__main__':

    print('CloudXNS API Version: ', Api.vsersion())
    api_key = 'xxxxxxxxxxxxxxxxx'
    secret_key = 'xxxxxxxx'
    api = Api(api_key=api_key, secret_key=secret_key)
    # api.set_debug(True)

    """
    功能 域名列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    #获取域名信息列表
    result = api.domain_list()
    result_json = json.loads(result)

    #转换数据为列表
    result_list = result_json['data']

    #将域名文件转换成列表
    with open('xns_domain.txt','r') as f:
        content = f.read().splitlines()
    domain_list_xns = content

    def get_domain_id(result_listf, domainf):
        t = None
        for i in result_listf:
            if domainf in i.values():
                t = True
                domain_id = i['id']
                result = api.domain_delete(domain_id)
                print result + "     " + domainf + "已删除!"
                break
            else:
                t = False
        if t is not True:
            print domainf + "解析不在XNS"

    for domain in domain_list_xns:
        domain_xns = domain + '.'
        get_domain_id(result_list, domain_xns)