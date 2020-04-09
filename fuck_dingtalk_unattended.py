# VER 3.1
import requests
import json
import time
import threading


# 用户更改区域开始
# 疯狗模式,快速刷时间
# 指定ulcookie,同时线程个数等于ulcookie个数,必须至少有一个
ulcookiesMadDog = [
    '55edc0eb6c478246863ffb1365e7e109',
    '56a7657fe05081e1c87b9ffd857d988f',
    '5a7e2e03f359bc503d585ba33e17f592',
    '7f7d4c97b49eb54019824778e70d8e05'
]
# 懒狗模式,自动从GitHub上读取视频ID,True是开,False是关,若开启则会强制关闭懒人模式,建议开启,除非我忘记更新了
LazyDogMode = True
# 表示是否刷今天的视频,True为 是,False为 否,若为 否,则必须在下面指定时间
UseTodayVideo = True
# 若上面为 否,则必须在此处指定时间
if not UseTodayVideo:
    VideoDate = {
        "year": 2020,
        "month": 1,
        "day": 1,
    }
else:
    # 这里别动
    VideoDate = {
        "year": time.localtime().tm_year,
        "month": time.localtime().tm_mon,
        "day": time.localtime().tm_mday,
    }
# Time是次数,我这个代码每次刷增加1分钟,默认值:1000
# 可刷时间,每次+1分钟,20次+20分钟
Times = 1000
# 这个是你在两次刷时间操作之间,停顿的秒数,建议不动,不然可能会被临时停止访问钉钉,默认值:5
SleepSecond = 5
# 这两个暂时别动,是每次刷的时间相关的,还没搞清楚
courseTime = 700
learnTime = 600
# 这两个代表你是谁,在每天第一次必须要改,后面都不用改,不要把引号删了,出现未登录问题优先排查这两个
dd_sid = 'k0_6f280b17b18e8e5e1ff6_0b176f285e8e8eb1699698707e064b24b2ed63d72f0f'
isg = 'BBUVXHKQ59qNrMPAsFLj9WyYJBHPEskkXXnNDZe6RgzJ7jfgX2NJ9iJovPDYbuHc'
# 这两个可能每两三天要更新一次,出现未登录问题其次排查这两个,ulcookie请在上面指定
sign = 'e3b922eaf021cab2cd3f5f5df4a4109e'
# 这三个也代表你是谁,只有第一次使用要修改,不要把引号删了
dt_s = 'u-1c4b69-7140459ff7-b5f54ae-6f59b5-792eaa9e-eb00daa9-b8b3-4885-a814-61d92387a4fb'
cna = 'LRLRFtSKfSICAXAxrxj3zKsn'
XSRF_TOKEN = '4433e438-3a80-44ca-a6cd-df3b52c41c5d'
# 用户更改区域结束


# 主要逻辑开始
# 别动这里
# 别动这里
def foo(order=0):
    global EXIT
    for i in range(Times):
        if EXIT:
            exit(0)
        flag_fail = False
        tmp_headers = Headers.copy()
        tmp_headers['ulcookie'] = ulcookies[order]
        response = requests.post(url=Url, data=json.dumps(Data), headers=tmp_headers)
        print()
        print("进程", order, "调试信息开始.")
        print("进程", order, response.text)
        print("进程", order, "调试信息结束.")
        print()
        print("进程", order, "次数:", i + 1, "共", Times)
        print("进程", order, "个数:", j + 1, "共", len(VideoInfos))
        print("次数:", i + 1, "共", Times)
        print("个数:", j + 1, "共", len(VideoInfos))
        response_formatted = eval(
            response.text.replace('\n', '').replace('\t', '').replace('true', 'True').replace('false', 'False'))
        global SleepSecond
        if response_formatted.get('rgv587_flag') == "sm":
            SleepSecond += 1
            print("进程", order, "警告: DoS 保护.")
        elif SleepSecond == 12:
            SleepSecond = 5
        if response_formatted.get('success') == 0:
            print("进程", order, "失败: 一般失败:", response_formatted['desc'])
            flag_fail = True
        if response_formatted.get('data') == 0:
            print("进程", order, "失败: 视频未找到.")
            flag_fail = True
        if response.status_code == 200:
            if not flag_fail:
                print("进程", order, "成功.")
            else:
                EXIT = True
                exit(-1)
        else:
            print("进程", order, "失败:", response.status_code)
            exit(-1)
        time.sleep(SleepSecond)


def fooWrapper():
    print("进程数:", len(ulcookiesMadDog))
    for i in range(len(ulcookiesMadDog) - 1):
        threading.Thread(target=foo, args=(i,)).start()
    tmp_thread = threading.Thread(target=foo, args=(len(ulcookiesMadDog) - 1,))
    tmp_thread.start()
    tmp_thread.join()
# 别动这里
# 别动这里
# 主要逻辑结束


# 逻辑开始
# 这里也别动
# 标头,Cookie处理
EXIT = False
VideoInfosUrl = 'https://gitee.com/chitaotao/dkskvd/raw/master/VideoInfosGithub.txt'
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
    # ulcookie
    'sign': sign,
    'Referer': 'https://saas.daxue.dingtalk.com/dingtalk/pc/detail.jhtml?appId=5488&'
               'corpid=ding3ec58e510b79646dacaaa37764f94726',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': CookiesFormatted
}

# 懒人模式/懒狗模式/疯狗模式的特别处理,及调用主逻辑
ulcookies = ulcookiesMadDog
VideoInfosResponse = requests.get(VideoInfosUrl).text.replace('\r', '').replace('\n', '').replace('\t', '')
VideoInfosGit = ''
# 会创建变量VideoInfosGit
exec(VideoInfosResponse)
if not VideoInfosGit:
    VideoInfosGit = {}
    print("懒狗模式: 错误: 网络错误: 获取视频信息失败.")
    exit(-1)
Date = str(VideoDate["year"]) + '-' + str(VideoDate["month"]) + '-' + str(VideoDate["day"])
VideoInfos = VideoInfosGit[Date]
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
    print("正在处理:", VideoInfo, j + 1, "共", len(VideoInfos))
    fooWrapper()
    print("已处理:", VideoInfo, j + 1, "共", len(VideoInfos))
    print()
    j = j + 1
print('全部完成.')
# 这里也别动
# 逻辑结束
