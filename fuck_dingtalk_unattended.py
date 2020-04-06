# VER 2.1
import requests
import json
from time import sleep


# 用户更改区域开始
# 懒人模式,把json粘贴过来,自动解析视频ID,True是开,False是关,支持多个视频
LazyMode = True
VideoInfos = [
    {"source": 3, "studyType": 2, "resourceId": "103692055", "packageId": "102453309", "courseId": "102482170",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103207978", "packageId": "102270333", "courseId": "102788191",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103728082", "packageId": "102453307", "courseId": "102925258",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103271009", "packageId": "102453307", "courseId": "102286242",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "102842008", "packageId": "102609325", "courseId": "102957231",
     "courseTime": 0, "learnTime": 0, "type": 1},
    {"source": 3, "studyType": 2, "resourceId": "103271006", "packageId": "102609325", "courseId": "102286239",
     "courseTime": 0, "learnTime": 0, "type": 1}
]
# Time是次数,因为我这个代码每次刷增加1分钟,请根据视频长度做调整,因为视频大部分25分钟,所以默认值:25
# 可刷时间,每次+1分钟,20次+20分钟
Times = 250
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
# 这两个代表你是谁,在每天第一次必须要改,后面都不用改,不要把引号删了,出现未登录问题优先排查这两个
dd_sid = '0b012f6f5e8b4ba52b1b0551fecbc4c96b111ded6675'
isg = 'BJWVHCJWZ1_IX0NAMNJjdewYpJFPkkmkEXKs6hc8_4zrbqlg3-P1ddroPHBY7mFc'
# 这两个可能每两三天要更新一次,出现未登录问题其次排查这两个
ulcookie = '246e84f67592134e799bbbe8b6fb1318'
sign = '3aba6b743605ef0dacd8d9a76f4450c6'
# 这三个也代表你是谁,只有第一次使用要修改,不要把引号删了
dt_s = 'u-1c4b69-7140459ff7-b5f54ae-6f59b5-792eaa9e-eb00daa9-b8b3-4885-a814-61d92387a4fb'
cna = 'LRLRFtSKfSICAXAxrxj3zKsn'
XSRF_TOKEN = '4433e438-3a80-44ca-a6cd-df3b52c41c5d'
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
            global SleepSecond
            SleepSecond += 1
        elif SleepSecond == 8:
            SleepSecond = 5
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
