# VER 2.1
import requests
import json
from time import sleep


# 用户更改区域开始
# 懒人模式,把json粘贴过来,自动解析视频ID,True是开,False是关,支持多个视频
LazyMode = True
VideoInfos = [
    {"source": 3, "studyType": 2, "resourceId": "103592832", "packageId": "102318342", "courseId": "102579256",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103325538", "packageId": "102318342", "courseId": "102893143",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103079865", "packageId": "102318342", "courseId": "102019165",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103476086", "packageId": "102973230", "courseId": "101921005",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103922022", "packageId": "102973230", "courseId": "102051033",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103392161", "packageId": "102973230", "courseId": "102345080",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103476087", "packageId": "102973230", "courseId": "101921006",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "102406149", "packageId": "102973230", "courseId": "102486938",
     "courseTime": 0, "learnTime": 0, "type": 1}
]
# Time是次数,因为我这个代码每次刷增加1分钟,请根据视频长度做调整,因为视频大部分25分钟,所以默认值:25
# 可刷时间,每次+1分钟,20次+20分钟
Times = 25
# 这个是你在两次刷时间操作之间,停顿的秒数,建议不动,不然可能会被临时停止访问钉钉,默认值:5
SleepSecond = 5
# 下面三个在你换视频的时候要改,str()不要删,不要多加引号
if not LazyMode:
    # 没开懒人模式
    courseId = str(102197105)
    packageId = str(102649199)
    resourceId = str(103582425)
else:
    resourceId = ''
    packageId = ''
    courseId = ''
# 这两个暂时别动,是每次刷的时间相关的,还没搞清楚
courseTime = 700
learnTime = 600
# 这两个代表你是谁,在每天第一次必须要改,后面都不用改,不要把引号删了
dd_sid = 'k0_1cc70ab1d787865ec84c_0ab11cc75e8687d753643b8b59ec567d4ec4d24784fd'
isg = 'BMvLAQ1QERTORU0umsA183aKWm-1YN_iW0AihD3JPYpqXOi-xTH5MGs6Ml6y_Dfa'
# 这五个也代表你是谁,只有第一次使用要修改,不要把引号删了
dt_s = 'u-1c4b69-713b146399-b5f548f-8c59a6-3a8356d9-10a8d683-9287-4681-b3d3-188e429b277b'
cna = 'LRLRFtSKfSICAXAxrxj3zKsn'
XSRF_TOKEN = '4a918264-173f-4049-baf7-1f5c2a58504b'
ulcookie = 'fa04cdb0c4c182f55466f6a70fe96ad3'
sign = 'fb52241a82dd242ef97ecc621e3fb195'
# 用户更改区域结束


# 主要逻辑开始
# 别动这里
# 别动这里
def foo():
    for i in range(Times):
        flag_fail = False
        response = requests.post(url=Url, data=json.dumps(Data), headers=Headers)
        # Debug info start.到Debug info stop.输出的是调试数据,可忽略
        print()
        print("Debug info start.")
        print(response.text)
        print("Debug info stop.")
        print()
        print("Time:", i + 1)
        response_formatted = eval(
            response.text.replace('\n', '').replace('\t', '').replace('true', 'True').replace('false', 'False'))
        if response_formatted.get('rgv587_flag') == "sm":
            # 若显示这个,请把SleepSecond调大,建议调回默认值
            # 同时在多设备运行也有可能出现此问题
            print("Failed: DoS Protection.")
            flag_fail = True
        if response_formatted.get('success') == 0:
            print("Failed: General Fail:", response_formatted['desc'])
            flag_fail = True
        if response_formatted.get('data') == 0:
            print("Failed: Video Not Found.")
            flag_fail = True
        if response.status_code == 200 and not flag_fail:
            print("Success.")
        else:
            print("Failed:", response.status_code)
            exit(-1)
        sleep(SleepSecond)
# 别动这里
# 别动这里
# 主要逻辑结束


# 逻辑开始
# 这里也别动
# 标头,Cookie处理及懒人模式的特别处理
Url = "https://saas.daxue.dingtalk.com/dingtalk/course/record.jhtml"

Cookies = {
    'dt_s': dt_s,
    'up_ab': 'y',
    'preview_ab': 'y',
    'cna': cna,
    'XSRF-TOKEN': XSRF_TOKEN,
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
    'X-XSRF-TOKEN': XSRF_TOKEN,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36 dingtalk-win/1.0.0 nw(0.14.7) '
                  'DingTalk(5.0.6-Release.1) Mojo/1.0.0 Native AppType(release)',
    'isAjax': 'true',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'ulcookie': ulcookie,
    'sign': sign,
    'Referer': 'https://saas.daxue.dingtalk.com/dingtalk/pc/detail.jhtml?appId=5488&'
               'corpid=ding3ec58e510b79646dacaaa37764f94726',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': CookiesFormatted
}

if LazyMode:
    # 开了懒人模式
    j = 0
    for VideoInfo in VideoInfos:
        resourceId = VideoInfo['resourceId']
        packageId = VideoInfo['packageId']
        courseId = VideoInfo['courseId']
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
        print("Now Processing:", VideoInfo, j + 1, "in", len(VideoInfos))
        foo()
        print("Processed", VideoInfo, j + 2, "in", len(VideoInfos))
        print()
        j = j + 1
else:
    # 没开懒人模式
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
    foo()
print('Done.')
# 这里也别动
# 逻辑结束
