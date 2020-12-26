"""
        数据API功能实现模块
        by admin@musp.cn
        2020/12/7 22点03分
"""
import requests
import json
import random
import re
import time


'''
    基于Python的requests模块编写的页面抓取编写
    2020/12/1 22：09
'''
class NewSeverUrl:
    def __init__(self, url=''):
        self.ip = str(random.randint(1, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(1, 255))
        self.data = {}
        self.header = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'CLIENT-IP': self.ip,        # 设置虚拟请求Ip防高请求下服务器ip被拉黑
            'X-FORWARDED-FOR': self.ip,  # 2020/12/7 12点31分
        }
        print(time.time())
        tyeUrl = re.findall(r'((https?|ftp?|file?)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])', url)
        if tyeUrl:
            self.url = tyeUrl[0][0]
            self.restoreurl()
        else:
            self.returnUrlNull()

     # 检测页面是否存在跳转行为
    def restoreurl(self):
        print('restorurl:', time.time())
        request = requests.get(self.url, headers=self.header)
        if request.status_code == 301 or request.status_code == 302:
            self.url = request.headers['redirect_url']
        else:
            self.url = self.url


    # 统一返回格式
    # @title标题名 @cover视频封面图 @video视频源地址 @music视频音乐
    @staticmethod
    def returns(title='', cover='', video='', music=''):
        if video == "":
            data = {
                'code': 302,
                'message': "很抱歉展示无法获取相关信息！",
                'coinfo': '如有疑问请联系admin@musp.cn',
            }
        else:
            data = {
                'code': 200,
                'title': title,
                'cover': cover,
                'video': video,
                'music': music
            }
        return data

    # URL为空时返回
    @staticmethod
    def returnUrlNull():
        data = {
            'code': 304,
            'message': "您输入的URL为空或不合法！请重新输入。",
            'coinfo': '如有疑问请联系admin@musp.cn'
        }
        return data


    # 静态方法检测请求状态
    @staticmethod
    def requestCode(req = ''):
        if hasattr(req, 'status_code'):
            if req.status_code == 200:
                return True
        else:
            return False


    # 快手无水印视频地址抓取
    def kuaishou(self):
        print('ks')
        request = requests.get(self.url, headers=self.header)
        # 请求异常处理
        if self.requestCode(request):
            try:
                data = self.returns(re.findall(r'<div class="caption-container">(.+?)</div>', request.text)[0], re.findall(r'\"shareCover\":\"(.+?)\"', request.text)[0], re.findall(r'\"srcNoMark\":\"(http.+?)\"', request.text)[0])
            except IndexError:
                data = self.returns()
            return data
        else:
            data = self.returns()
            return data


    def douyin(self):
        requrl = requests.get(self.url, headers=self.header)
        if self.requestCode(requrl):
            try:
                request = requests.get('https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + re.findall(r'/share/video/([a-zA-Z0-9]+?)/', requrl.url)[0])
                dydata = request.json()
                # 获取视频播放地址时需要耗费大量的浏览
                # 解决思路：无 ！
                video = requests.get(dydata["item_list"][0]["video"]["play_addr"]["url_list"][0].replace('playwm', 'play'), headers=self.header)
                data = self.returns(dydata['item_list'][0]["desc"], dydata["item_list"][0]["video"]["cover"]["url_list"][0], video.url, dydata["item_list"][0]["music"]["play_url"]["url_list"][0])
            except IndexError:
                data = self.returns()
        else:
            data = self.returns()
        return data

class NewSeverData:
    pass

