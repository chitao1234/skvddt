# VER 3.1
import requests
import json
import time
import threading


# 用户更改区域开始
# 疯狗模式,快速刷时间
# 指定ulcookie,同时线程个数等于ulcookie个数,必须至少有一个
ulcookiesMadDog = [
    '326ecd7013c0f1f91738c2138e43cda1',
    'b1b633c27e9b8d2f28c8c8748fddd7f1',
    'e38e5e8ddcd75baf2a85253c0aee2222',
    '520d8efabc92e06504fc4fff2092e993',
    'df07d772592d028fa9f4357bd413194e',
    '96dbecd7bf755e66973debc041ce1859',
    'dd51a207af1f038358cd02096fa1cac5',
    '3872e7afecd0f14847c4172ad31d4ed2',
    '8cf54f86a5aa74685e38027c4a6782cd',
    'c1bb4d8481a729af2ce38a0563b78b6d',
    '419a8be03d2a1ef2733a158004215732',
    '8a4bfdbe0492b39a0bc08802fcfdda5a',
    '96b8f61e404b6a372604548971c4b446',
    '943e6fd5e096c99f757382c30ee81df0',
    '26da952cdac3b46f8316f81eb5934ece',
    '71f89f8c48ac8c1f73a4b9b34484181c',
    '218e5606af992347714e6d87fb9fb3a6',
    'bdbee482ec60f76c69d0d4dcadbb082d',
    '02bfa1769d3ddee6e8c60e4cb0a839e7',
    'ae5e5988cb4a777d8d48dd0f5ff9aadd',
    '779486070fef17b7724a4d60579fbde6',
    'ec59c27f9226939803625ef488847388',
    'baae950a45dc0341505a9d7ef7b57238',
    '7ecfb33e4e6f7cbd1cdd0ce65e87c4b3',
    'ac82d21a1fb3aa08387df6b54cdb76f5',
    '2281ca69c42f878a54dd2e2cb51b88b8',
    '05f3bd7a680ec9dc46f0d77f2cfdf774',
    'a9114b68638c60bb5212ebc0f56f52cb',
    '8957855d7225d2d693371ba1a4b9a015',
    '728d13b53b8bc005943df44cea329d9e',
    '93cbe634ee8f91daa877ef78f43d3b07',
    'd3315569c7f3584063656b53f2263ad3',
    '47904785c57a332c70e1fb4fe507a177',
    '20c175547025380c98e8686e65c14e6d',
    'f5c490edf815af042bbf4ca3a1800d74',
    '22ac1408435390cb6bee39acdfb73647',
    'fe1da203b0a6c5e491fcc3d87aff12dd',
    '2ab1a34775a64b1ee2eed1eb3fd005ff',
    '1ca5dde8ed744d42e0854b3ea1c03401',
    'a73ea9957c0c13ee16290ce479b87730',
    '036197cedb3f7857acd079e5ea1aed42',
    '9a47f1c10111986012f80d4a69c47d33',
    'a7d15d2d807f62fac72de46f03e8ca40',
    'f3c604d6227004002f92e2dcff231a43',
    '49ab65aa78b1443d2a116a40c2c383c5',
    '8655bd3f1f59b2006b7dd0942d451e4e',
    '3dbb282ad2b8feb43618f9e2fc0c8c1a',
    '3a75d9e531f24783f2d8598911b85229',
    'cddefa5956e08aac855a12670a5b1d7c',
    'a35425892fe25a8035b85f3b3b44eb2c',
    '1983b7550e88b875f3af784af9e05e01',
    'b89c16bf48af12913587c41816df1e8d',
    'f9e01e744cd140ce6640d4a1d1dca869',
    'a573f690f6212bb27e342fdeb8127913',
    '85e0658f78d2c81f6e958c1edfed2c0a',
    'a4fe1303f335cc625ca4beed4b6c9c2c',
    '99bf11ec84f28e50584c94ab4d35fdbd',
    '9fd40ab390e6f49442e3baa3583ae433',
    '751d8e84b85d9f42ed66868159c005b3',
    '600aba6d689f925c857946e65d14fc4d',
    '7190c077c5dee419fb981d005911fc3c',
    '8f2244c589776c20352536bd6279a822',
    'c8a185bb7a9f276068afb8c41731ee58',
    '3b650f1c58e820539f97759a4678cb87',
    '30bdba99218b5f2d8a1586af7584ca3f',
    'fe56dc0defd0f841bfa54b8ceff80dad',
    '79f107adfafd4d3e788a94ff380536b2',
    'c958e46e533d3ac57590c6d5359dfc9a',
    '604314a83fd0a9cd19467268684cbf06',
    '3eb62c6c5605eeafc5db0d3d9ab27a13',
    'c421645499883581167380546c4f1a85',
    'a3b03536921d0bfc703d0b44c696c56e',
    'c9b013b5eb67219ec0abeca97e94d60c',
    '5d45a4ef35eaf6dbf8ce5c6ee5ed4382',
    'bbd33fe8139c6a28e9af5a32f9ffaabe',
    'bb85bd65e56d5f8c7f1e3467c08eb688',
    'd2a50565c3a194e4031638b92772d85a',
    'fe1ae83b2820dd40e0f7a5f3b7b186a5',
    'd3795d4fb3bb8ecb777bc47505f8c17c',
    'a5b4fe9d5609282a48d9805acda86f2e',
    '5d1ac259fb43221e7afaa096aeb35075',
    'db7b52bea416f2797e0f39e2bdfaa918',
    'd8f1a917eac8f3f6563e9e2752d0285e',
    '5f27190500c200446e8947a422472f8c',
    'fc9e41d49878849722494629fe381f2c',
    'e480147c2bc4652d7620447b6d93ba6e',
    '925dd63515ed99cfa2c4ece7b58d26e9',
    'b67915990c026b51c44c7afe8c55b3c0',
    '754d80e01a5caa7a362a37862334d211',
    '777fe7569d6b88a36c0a661b8034ded9',
    'bb4b9d8dbe246a10e55cf372b34d79ba',
    '1ad66582c110b2fce4729e1b4a86452f',
    '086424cabc73d0d858da51c6517da90f',
    '690e8b58c5d6bdebae0a0c854192a659',
    '3fb9f448aa4e8d7d0c138be59fc1ed2c',
    '21cd2dbd91a3a2c600111685406764bc',
    '9d0cec54342f88d4502a16fcdfcdfe3b',
    'aa27c6f35d2dd684b9ab7e19e69f3879',
    'f9681a8e76f7c3cf8851ffd63ceaf386',
    '72d0b6cbdcb0e44f219b6de5f8049d81'
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
        try:
            time.sleep(SleepSecond)
        except KeyboardInterrupt:
            EXIT = True


def fooWrapper():
    print("进程数:", len(ulcookiesMadDog))
    for i in range(len(ulcookiesMadDog) - 1):
        threading.Thread(target=foo, args=(i,)).start()
        # 把进程平均分配到5秒内,4.9为了减去开始进程消耗的时间
        time.sleep(4.9 / len(ulcookiesMadDog))
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
