# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from ding_msg import *
import re
requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5
reload(sys)
sys.setdefaultencoding('utf-8')
CDATES = time.strftime('%Y-%m-%d', time.localtime(time.time()))
from ding_msg import *
all_msg = ''


def get_news():
    global all_msg
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        'Referer': 'https://shuo.taoguba.com.cn/newsFlash/',
        'Cookie': 'JSESSIONID=b169846c-0fe0-43bc-aaa1-b9dad16f0eac; Hm_lvt_cc6a63a887a7d811c92b7cc41c441837=1623320243; Hm_lpvt_cc6a63a887a7d811c92b7cc41c441837=1623320785; UM_distinctid=179f56d2df2882-047a5ba0ebc66e-445566-7e900-179f56d2df3972; CNZZDATA1574657=cnzz_eid%3D1627495985-1623319571-https%253A%252F%252Fwww.taoguba.com.cn%252F%26ntime%3D1623319571',
        'Origin': 'https://shuo.taoguba.com.cn/newsFlash/',
        'TE':'Trailers'
    }
    for i in range(1,20):
        datas= requests.get('https://shuo.taoguba.com.cn/newsFlash/getAllNewsFlash?type=A&pageNo='+str(i),headers = headers)
        data_json = json.loads(datas.text)
        dto = data_json.get('dto')
        lists = dto.get('list')
        for list in lists:
            shuoid = list.get('shuoID')
            subject = list.get('subject')
            body = list.get('body')
            if '早间新闻精选' in subject:
                dingmsg(body)
                print body
def dingmsg(msg):
    webhook = 'https://yach-oapi.zhiyinlou.com/robot/send?access_token=Y3EwTlNXS04xUnlXVllrOEk0SjV6bE9sUy9NQW95TEplSVBFZWUxYkdNbFlOMXlaM1ZabjNkZW5hUG8yL1RqTw'
    secert = 'SEC2ee4e38693af5ae78ac3444190c77a9e'
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook,secert)
    xiaoding.send_text(msg)
    print "发送消息成功"

if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # scheduler.add_job(get_news, 'cron', day_of_week='0-6', hour=9, minute=01)
    # scheduler.start()
    get_news()