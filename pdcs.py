import pandas as pd
from wechat_work import WechatWork

# # 测试通过企业微信发送信息

corpid = 'wx86ade657d9d15fc5'
appid = '1000015'
corpsecret = 'vP_tz5m43cgFsQ-phNeWgZBhIelYxv3OEaXB4JLrHHY'
users = ['006104']
w = WechatWork(corpid=corpid,
               appid=appid,
               corpsecret=corpsecret)
# 发送文本
w.send_text(f'要发送的信息   ', users)

# df = pd.read_csv('site.csv', encoding='utf-8')
# # print(df.items)
# for x in df.values:
#     stri = ''
#     stri = str(x[0]) + str(x[1]) + str(x[2])
#
# print(type(stri))
