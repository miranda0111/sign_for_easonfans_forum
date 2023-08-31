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
ssl._create_default_https_context = ssl._create_unverified_context
# --------------------------------------------------------------------------------------------
Script_Name = "神经研究所签到"
Name_Pinyin = "SJ"
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
        easonfans_sign(ck,content)
        time.sleep(random.randint(11, 22))
        
        easonfans_gplay(ck)
        time.sleep(random.randint(11, 22))
        
        easonfans_gplay(ck)
        time.sleep(random.randint(11, 22))
        
        easonfans_gplay(ck)
        
        uids = [str(random.randint(46011, 52786)) for _ in range(10)]
        message = "%E5%8E%9F%E8%B0%85%E6%88%91%E4%B8%8D%E5%86%8D%E9%80%81%E8%8A%B1%EF%BC%8C%E4%BC%A4%E5%8F%A3%E5%BA%94%E8%A6%81%E7%BB%93%E7%96%A4%EF%BC%8C%E8%8A%B1%E7%93%A3%E9%93%BA%E6%BB%A1%E5%BF%83%E9%87%8C%E5%9D%9F%E5%9C%BA%E6%89%8D%E5%AE%B3%E6%80%95%E3%80%82%E2%80%94%E2%80%94%E9%99%88%E5%A5%95%E8%BF%85%5Bem%3A5%3A%5D%5Bem%3A9%3A%5D%5Bem%3A11%3A%5D"
        for e in range(0, len(uids)):
            uid = uids[e]
            easonfan_comment(ck,uid,message)
            time.sleep(random.randint(11, 22))
        
def ql_env(name):
    global ckArr
    if name in os.environ:
        ckArr = []
        # print(111111111111)
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



async def easonfans_sign(easonfanck, easonfancomment):
    # easonfanck = "sNgB_2132_saltkey=ST1yI81S; sNgB_2132_lastvisit=1692674624; sNgB_2132_webtctzcountforumindex=0; sNgB_2132_con_request_uri=http%3A%2F%2Feasonfans.com%2Fforum%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php; sNgB_2132_client_created=1692678235; sNgB_2132_client_token=2506D8E06A9FE0F0F0E185755078904E; sNgB_2132_auth=6253Ff6csAbRJcpjdVWG%2BlDSYJNsO%2FRbyjCohhM%2F9Zb637XTDyvbHAEuicXI0GZhLXrmu1hVfX0JwdZvH%2BmyD2hoqw; sNgB_2132_creditnotice=0D0D2D0D0D0D0D0D0D60818; sNgB_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; sNgB_2132_connect_login=1; sNgB_2132_connect_is_bind=1; sNgB_2132_connect_uin=2506D8E06A9FE0F0F0E185755078904E; security_session_verify=72c17bb8b9a1443d0945f1ff7033e9d9; sNgB_2132_lip=183.46.169.55%2C1693039880; sNgB_2132_creditbase=0D0D1552D0D0D0D0D0D0; sNgB_2132_nofavfid=1; sNgB_2132_onlineusernum=242; sNgB_2132_sid=hyWxm7; sNgB_2132_ulastactivity=5158Z%2FdUPa%2BM%2BnnhQPpSBdZnFwzfuM4ne35DLhDJU%2F4TXU%2FXhwRp; sNgB_2132_home_diymode=1; sNgB_2132_webtctzcounthomespace=0; sNgB_2132_lastact=1693039932%09plugin.php%09"
    # easonfancomment = ""
    # easonfancomment =1 "%E6%88%91%E8%A6%81%E8%B5%9A%E7%A7%AF%E5%88%86%EF%BC%81"


    url = "http://easonfans.com//forum/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0&mobile=2"
    headers = {
        "Host": "easonfans.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http//easonfans.com",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": easonfanck,
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; 2304FPN6DC Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "Referer": "http://easonfans.com/forum/plugin.php?id=dsu_paulsign:sign&mobile=2",
        "Content-Length": "110",
        "Cache-Control": "max-age=0",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Upgrade-Insecure-Requests": "1"
    }
    data = f"formhash=7aea1da7&qdxq=kx&qdmode=1&todaysay={easonfancomment}&fastreply=0"
    response = requests.request("POST", url, headers=headers, data=data)
    html = response.text
    # soup = BeautifulSoup(html, 'xml')
    # info = soup.body.get_text()

    nam = re.findall('<div style="line-height:30px; text-indent:2em;">(.*?).</div>', html)[0]

    msg(nam)

def easonfans_gplay(easonfanck):
    url = "http://easonfans.com/forum/plugin.php?id=gplayconstellation:front&mod=index&formhash=7aea1da7&act=game_result&inajax=1&ajaxtarget=myaward"
    headers = {
        "Host":"easonfans.com",
        "X-Requested-With":"XMLHttpRequest",
        "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding":"gzip, deflate",
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Linux; Android 13; 2304FPN6DC Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "Connection":"keep-alive",
        "Referer":"http://easonfans.com/forum/plugin.php?id=gplayconstellation:front&act=phone&mobile=2",
        "Cookie":easonfanck
    }
    response = requests.get(url, headers=headers)
    html = response.text
    nam = re.findall('<input type="hidden" id="out_activity_credit" value="(.*?)">', html)[0]
    msg(f"获得{nam}金钱")

def easonfan_comment(easonfanck,uid,message):

    url = "http://easonfans.com/forum/home.php?mod=spacecp&ac=comment"
    
    headers = {
        "Host": "easonfans.com",
        "Connection": "keep-alive",
        "Content-Length": "515",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://easonfans.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; 2304FPN6DC Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": f"http://easonfans.com/forum/home.php?mod=space&uid={uid}&do=wall&mobile=2",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": easonfanck
    }
    data = f"message={message}&referer=home.php%3Fmod%3Dspace%26uid%3D%26do%3Dwall&id={uid}&idtype=uid&handlekey=qcwall_{uid}&commentsubmit=true&quickcomment=true&commentsubmit_btn=true&formhash=7aea1da7"
    response = requests.request("POST", url, headers=headers, data=data)
    html = response.text

    # soup = BeautifulSoup(html, 'xml')
    # info = soup.body.get_text()
    
    nam = re.findall('<p class="ashow cl">(.*?).</p>', html)[0]
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
