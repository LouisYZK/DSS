# coding: utf-8  
# agri.gov.cn_amf_client.py  
# http://jgsb.agri.gov.cn/flexapps/hqApp.swf数据抓取  
  
import urllib2  
import uuid  
import pyamf  
from pyamf import remoting  
from pyamf.flex import messaging  
  
class HqPara:    
    def __init__(self):  
        self.marketInfo = None  
        self.breedInfoDl = None  
        self.breedInfo = None  
        self.provice = None  
# https://en.wikipedia.org/wiki/Action_Message_Format  
# registerClassAlias("personTypeAlias", Person);  
# 注册自定义的Body参数类型，这样数据类型com.itown.kas.pfsc.report.po.HqPara就会在后面被一并发给服务端（否则服务端就可能返回参数不是预期的异常Client.Message.Deserialize.InvalidType）  
pyamf.register_class(HqPara, alias='com.itown.kas.pfsc.report.po.HqPara')  
  
# 构造flex.messaging.messages.RemotingMessage消息  
msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),  
                                clientId=str(uuid.uuid1()).upper(),  
                                operation='getHqSearchData',  
                                destination='reportStatService',  
                                timeToLive=0,  
                                timestamp=0)  
# 第一个是查询参数，第二个是页数，第三个是控制每页显示的数量（默认每页只显示15条）  
msg.body = [HqPara(), '1', '50']  
msg.headers['DSEndpoint'] = None  
msg.headers['DSId'] = str(uuid.uuid1()).upper()  
# 按AMF协议编码数据  
req = remoting.Request('null', body=(msg,))  
env = remoting.Envelope(amfVersion=pyamf.AMF3)  
env.bodies = [('/1', req)]  
data = bytes(remoting.encode(env).read())  
  
# 提交请求  
url = 'http://jgsb.agri.gov.cn/messagebroker/amf'  
req = urllib2.Request(url, data, headers={'Content-Type': 'application/x-amf'})  
# 解析返回数据  
opener = urllib2.build_opener()  
  
# 解码AMF协议返回的数据  
resp = remoting.decode(opener.open(req).read())  
for i, record in enumerate(resp.bodies[0][1].body.body[0]):  
    print i, record['farmProduceName'],record['marketName'],record['maxPrice'],record['minPrice'],record['averagePrice'],record['producAdd'] and record['producAdd'],record['reportMan']  