# VER 1.2
import requests
import json
from time import sleep


# 用户更改区域开始
# Time是次数,因为我这个代码每次刷增加5%,所以加了自动多刷几次的次数
Times = 20
# 这个是你在两次刷时间操作之间,停顿的秒数,建议不动,不然可能会被临时停止访问钉钉
SleepSecond = 4
# 下面三个在你换视频的时候要改,str()不要删,不要多加引号
resourceId = str(103476085)
packageId = str(102960314)
courseId = str(101921004)
# 这两个暂时别动,是每次刷的时间相关的,还没搞清楚,不要多加引号
courseTime = 50000
learnTime = 6000
# 这两个代表你是谁,在第一次要改,后面都不用改
dd_sid = 'k0_25340b1b24e9855ec7fc_0b1b25345e85e9243c15420dba2f3d75e48511d9aa83'
isg = 'BKCgK0e66mY9L1aPfZm-4tkDca5yqYRzIgXkgxq1HLtyFUc_wrpSAxvrqb-VpTxL'
# 用户更改区域结束

Url = "https://saas.daxue.dingtalk.com/dingtalk/course/record.jhtml"
Data = {
    "source": 3,
    "studyType": 2,
    "resourceId": resourceId,
    "packageId": packageId,
    "courseId": courseId,
    "courseTime": courseTime,
    "learnTime": learnTime,
    "type": 2
}
Cookies = {
    'dt_s': 'u-1c4b69-713b146399-b5f548f-8c59a6-3a8356d9-10a8d683-9287-4681-b3d3-188e429b277b',
    'up_ab': 'y',
    'preview_ab': 'y',
    'cna': 'LRLRFtSKfSICAXAxrxj3zKsn',
    'XSRF-TOKEN': '4a918264-173f-4049-baf7-1f5c2a58504b',
    'dd_sid': dd_sid,
    'isg': isg
}
CookiesFormatted = ''

for key, value in Cookies.items():
    CookiesFormatted += (key + '=' + value + '; ')

Headers = {
    'Host': 'saas.daxue.dingtalk.com',
    'Connection': 'keep-alive',
    'Content-Length': '139',
    'Origin': 'https://saas.daxue.dingtalk.com',
    'X-XSRF-TOKEN': '4a918264-173f-4049-baf7-1f5c2a58504b',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 dingtalk-win/1.0.0 nw(0.14.7) DingTalk(5.0.6-Release.1) Mojo/1.0.0 Native AppType(release)',
    'isAjax': 'true',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'ulcookie': 'fa04cdb0c4c182f55466f6a70fe96ad3',
    'sign': 'fb52241a82dd242ef97ecc621e3fb195',
    'Referer': 'https://saas.daxue.dingtalk.com/dingtalk/pc/detail.jhtml?appId=5488&corpid=ding3ec58e510b79646dacaaa37764f94726',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': CookiesFormatted
}
for i in range(Times):
    Response = requests.post(url=Url, data=json.dumps(Data), headers=Headers)
    # Debug info start.到Debug info stop.输出的是调试数据,可忽略
    print()
    print("Debug info start.")
    print(Response.text)
    print("Debug info stop.")
    print()
    print("Time:", i + 1)
    if eval(Response.text.replace('\n', '').replace('\t', '').replace('true', 'True'))["data"] == 0:
        print("Failed: Video Not Found.")
    if Response.status_code == 200:
        print("Success")
    else:
        print("Failed:", Response.status_code)
    sleep(SleepSecond)
