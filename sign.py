# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:03:10 2023

@author: m1361
"""

# !/bin/env python3
# -*- coding: utf-8 -*
"""
"""

try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    import random
    import asyncio
    import ssl
    from bs4 import BeautifulSoup
except Exception as e:
    print(e)
requests.packages.urllib3.disable_warnings()
# ssl._create_default_https_context = ssl._create_unverified_context
# --------------------------------------------------------------------------------------------
Script_Name = "神经研究所签到"
Name_Pinyin = "SS"
Script_Change = ""
Script_Version = "1.0.0"
# --------------------------------------------------------------------------------------------
async def start():
    global ckArr
    # easonfancomment = "%E5%8A%AA%E5%8A%9B%E5%8A%AA%E5%8A%9B%E5%86%8D%E5%8A%AA%E5%8A%9B%E5%8A%A0%E6%B2%B9%EF%BC%81"
    
    content = "%E5%8A%AA%E5%8A%9B%E5%8A%AA%E5%8A%9B%E5%86%8D%E5%8A%AA%E5%8A%9B%E5%8A%A0%E6%B2%B9%EF%BC%81"
    for inx, data in enumerate(ckArr):
        msg("开始第" + str(inx + 1) + "个账号")
        ck = data
        # await get_user(ck)
        await asyncio.sleep(1)
        await easonfans_sign(ck,content)
        
def ql_env(name):
    global ckArr
    if name in os.environ:
        ckArr = []
        print(111111111111)
        _data = os.environ[name]
        if "#" in _data:
            _ck = _data.split("#")
            ckArr = _ck
        elif "@" in _data:
            _ck = _data.splitlines()
            ckArr = _ck
        else:
            ckArr = _data.split("+")
    # print(ckArr)

# def easonfans_sign(easonfanck, easonfancomment):
#     url = "https://www.easonfans.com/forum/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0&mobile=2"
#     headers = {
#         "Host": "www.easonfans.com",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Origin": "https//www.easonfans.com",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Cookie": "sNgB_2132_connect_is_bind=0; sNgB_2132_lastact=1682303687%09plugin.php%09; sNgB_2132_lip=183.63.119.39%2C1682303349; sNgB_2132_sid=oo4Qq8; sNgB_2132_ulastactivity=2c6ek6SV%2FSk6IWh43w%2B4TQ5Lsq%2F54EsWnoP280WSUY45vSvzT0eF; security_session_verify=62e02f61336ade32fd941cb8b4f59735; sNgB_2132_forum_lastvisit=D_31_1682254086D_17_1682254089; sNgB_2132_visitedfid=17D31; sNgB_2132_nofavfid=1; sNgB_2132_auth=0db0bNrGhE69Bz1d8xekxxdD%2FcKamp6hvagtHk30WbfOBw91MVUml1epRd%2Bjktq6JFfuSOGi5K7zHTCrf37Kb%2Bgrvw; sNgB_2132_lastcheckfeed=60818%7C1682250507; sNgB_2132_lastvisit=1682246886; sNgB_2132_saltkey=kb96ZElc",
#         "Connection": "keep-alive",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/WIFI Language/zh_CN",
#         "Referer": "https//www.easonfans.com/forum/plugin.php?id=dsu_paulsign",
#         "Content-Length": "146",
#         "Accept-Language": "zh-CN,zh-Hans;q=0.9"
#     }
#     data = f"formhash=4c2783cc&qdxq=fd&qdmode=1&todaysay={easonfancomment}&fastreply=0"
#     response = requests.request("POST", url, headers=headers, data=data)
#     html = response.text
#     soup = BeautifulSoup(html, 'xml')
#     # info = soup.body.get_text()

#     nam = re.findall('<div style="line-height:30px; text-indent:2em;">(.*?).</div>', html)[0]

#     print(nam)

async def easonfans_sign(easonfanck, easonfancomment):
    url = "https://www.easonfans.com/forum/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0&mobile=2"
    headers = {
        "Host": "www.easonfans.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https//www.easonfans.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "sNgB_2132_connect_is_bind=0; sNgB_2132_lastact=1682303687%09plugin.php%09; sNgB_2132_lip=183.63.119.39%2C1682303349; sNgB_2132_sid=oo4Qq8; sNgB_2132_ulastactivity=2c6ek6SV%2FSk6IWh43w%2B4TQ5Lsq%2F54EsWnoP280WSUY45vSvzT0eF; security_session_verify=62e02f61336ade32fd941cb8b4f59735; sNgB_2132_forum_lastvisit=D_31_1682254086D_17_1682254089; sNgB_2132_visitedfid=17D31; sNgB_2132_nofavfid=1; sNgB_2132_auth=0db0bNrGhE69Bz1d8xekxxdD%2FcKamp6hvagtHk30WbfOBw91MVUml1epRd%2Bjktq6JFfuSOGi5K7zHTCrf37Kb%2Bgrvw; sNgB_2132_lastcheckfeed=60818%7C1682250507; sNgB_2132_lastvisit=1682246886; sNgB_2132_saltkey=kb96ZElc",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/WIFI Language/zh_CN",
        "Referer": "https//www.easonfans.com/forum/plugin.php?id=dsu_paulsign",
        "Content-Length": "146",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    data = f"formhash=4c2783cc&qdxq=fd&qdmode=1&todaysay={easonfancomment}&fastreply=0"
    response = requests.request("POST", url, headers=headers, data=data)
    html = response.text
    soup = BeautifulSoup(html, 'xml')
    # info = soup.body.get_text()

    nam = re.findall('<div style="line-height:30px; text-indent:2em;">(.*?).</div>', html)[0]

    msg(nam)

# ====================================================================
def last_version(name, mold):
    url = ''
    if mold == 1:
        url = f"https://gitee.com/miranda0111/xmydsbs/raw/master/{name}.py"
    try:
        _url = url
        _headers = {}
        resp = requests.get(url=_url, headers=_headers, verify=False)
        result = resp.text
        resp.close()
        r = re.compile(r'Script_Version = "(.*?)"')
        _data = r.findall(result)
        if not _data:
            return "出现未知错误 ,请稍后重试!"
        else:
            return _data[0]
    except Exception as err:
        print(err)
        
# 通知服务
class Msg(object):
    def __init__(self, m=''):
        self.str_msg = m
        self.message()

    # noinspection PyMethodMayBeStatic
    def get_sendnotify(self):
        if not os.path.exists("sendNotify.py"):
            cur_path = os.getcwd()
            print(f"未找到通知依赖文件,将于脚本执行目录({cur_path})新建:sendNotify.py (url为https://gitee.com/miranda0111/xmydsbs/raw/master/sendNotify.py)")
            try:
                url = 'https://gitee.com/miranda0111/xmydsbs/raw/master/sendNotify.py'
                response = requests.get(url)
                with open('sendNotify.py', "w+", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as err:
                print(err)
        else:
            print("文件已存在,跳过")
            pass
        pass

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            # msg_info = ''
            msg_info = f"{msg_info}\n{self.str_msg}"
        except Exception as err:
            print(err)
            msg_info = "{}".format(self.str_msg)
        sys.stdout.flush()
        # 这代码的作用就是刷新缓冲区。
        # 当我们打印一些字符时 ,并不是调用print函数后就立即打印的。一般会先将字符送到缓冲区 ,然后再打印。
        # 这就存在一个问题 ,如果你想等时间间隔的打印一些字符 ,但由于缓冲区没满 ,不会打印。就需要采取一些手段。如每次打印后强行刷新缓冲区。

    def main(self):
        global send
        cur_path = os.getcwd()
        # print(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            # noinspection PyBroadException
            try:
                from sendNotify import send
            except Exception as err:
                self.get_sendnotify()
                print(err)
                try:
                    from sendNotify import send
                except Exception as err:
                    print(err)
                    print("加载通知服务失败~")
        else:
            self.get_sendnotify()
            try:
                from sendNotify import send
            except Exception as err:
                print(err)
                print("加载通知服务失败~")

Msg().main()

def msg(data):
    Msg(data)



def tip():
    # global ckArr
    print("================ 脚本只支持青龙新版 =================")
    print("============ 具体教程以请自行查看顶部教程 =============")
    
    # msg(f"🔔 {Script_Name}，开始! ")
    # origin_version = last_version(Name_Pinyin, 1)
    # msg(f"📌 本地脚本: {Script_Version}\n    远程仓库版本: {origin_version}")
    # if str(Script_Version) == str(origin_version):
    #     msg(f"📌 🆙 脚本版本一致，完成内容: {Script_Change}")
    # else:
    #     msg('📌 📌 📌 发现版本更新！请尽快更新！📌 📌 📌 \n')
    #     msg(f"📌 🆙 更新内容: {Script_Change}")

    print(f"📌 共发现 {str(len(ckArr))} 个账号")

if __name__ == '__main__':
    global ckArr, msg_info, send
    # sendindex = 1
    print(f"{Name_Pinyin}_DATA")
    ql_env(f"{Name_Pinyin}_DATA")
    # ckArr = os.environ.get(f"{Name_Pinyin}_DATA")
    # print(ckArr)
    tip()
    asyncio.run(start())
    # if sendindex == 1:
    send(f"{Script_Name}", msg_info)