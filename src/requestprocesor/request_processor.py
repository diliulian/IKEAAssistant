#coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan
'''
from wechat.message_utils import MessageUtil
import common_params
from wechat import message_utils
import HTMLParser
class RequestProcessor(object):
    '''
    classdocs
    '''
    def get(self, requst):
        requst.write("this is MyWeChatService!")
        

    def post(self, request):
        print request.request.body
        
        req_dict=self.message_util.parse_xml(request)
        
        rsp_dict={}
        rsp_dict[common_params.to_user_name]=req_dict[common_params.from_user_name]
        rsp_dict[common_params.from_user_name]=req_dict[common_params.to_user_name]
        msg_time=long(req_dict[common_params.create_time])
        print 'before, msg_time= '+str(msg_time)
        msg_time=msg_time+3
        print 'after, msg_time= '+str(msg_time)
        rsp_dict[common_params.create_time]=str(msg_time)
        rsp_dict[common_params.message_type]=req_dict[common_params.message_type]
        rsp_dict[common_params.content]=req_dict[common_params.content]
#         rsp_dict[common_params.message_id]=req_dict[common_params.message_id]
        
        rsp_xml=self.message_util.gen_xml(rsp_dict)
        
        rsp_xml=self.html_parser.unescape(rsp_xml)
        
        print rsp_xml
        
        request.write(rsp_xml)
        
    
    def __init__(self):
        self.message_util=MessageUtil()
        self.html_parser = HTMLParser.HTMLParser()
        