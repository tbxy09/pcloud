#!/usr/bin/env python
#coding=utf-8

import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
# import util
from util.log import apidebug,apiinfo

# client = AcsClient('<LTAIHW05LP8OLw8x>', '<5PCpkTO2g82HeFKI4H9PyuprhXtQLP>', 'cn-beijing')
# client = AcsClient(
#                 'LTAIHW05LP8OLw8x',
#                 '5PCpkTO2g82HeFKI4H9PyuprhXtQLP',
#                 'cn-beijing')

def describeIns(*key):

    apidebug(key)

    client = AcsClient(
                    key[0],
                    key[1],
                    'cn-beijing')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('ecs.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2014-05-26')
    request.set_action_name('DescribeInstances')

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    if os.environ.get("API_JSON_INFO")=="1":
        apiinfo("Json Response")
        print(str(response, encoding = 'utf-8'))
    return response

def describeSec(*key):

    apidebug(key)

    client = AcsClient(
                    key[0],
                    key[1],
                    'cn-beijing')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('ecs.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2014-05-26')
    request.set_action_name('DescribeSecurityGroupAttribute')

    request.add_query_param('RegionId', 'cn-beijing')
    request.add_query_param('SecurityGroupId', 'sg-2zeiafyiu5nh8zsuy1u6')

    response = client.do_action_with_exception(request)

    if os.environ.get("API_JSON_INFO")=="1":
        apiinfo("Json Response")
        print(str(response, encoding = 'utf-8'))

def modifySec(*key):
    apidebug(key)

    client = AcsClient(
                    key[0],
                    key[1],
                    'cn-beijing')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('ecs.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2014-05-26')
    request.set_action_name('AuthorizeSecurityGroup')

    request.add_query_param('RegionId', 'cn-beijing')
    request.add_query_param('SecurityGroupId', 'sg-2zeiafyiu5nh8zsuy1u6')
    request.add_query_param('IpProtocol', 'tcp')
    request.add_query_param('PortRange', '22/22')
    # request.add_query_param('SourceCidrIp', '223.87.240.203')
    host_ip = key[2]
    request.add_query_param('SourceCidrIp', host_ip)
    request.add_query_param('Policy', 'accept')
    request.add_query_param('Priority', '1')

    # response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding = 'utf-8'))
