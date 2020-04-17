# VER 3.1
import requests
import json
import time
import threading


# 用户更改区域开始
# 疯狗模式,快速刷时间
# 这个代表你是谁,可能每天要更新一次,出现未登录问题优先排查这个
# 指定ulcookie,同时线程个数等于ulcookie个数,必须至少有一个
ulcookiesMadDog = [
    '11f33e6ed8f2f230b5cabca5ecd09704',
    '96ef338a783171c9cf7b9f39c012b8a4',
    '1a5a3e53cc3ab0186ec01859530d17ce',
    'b962aa64eb3721188b66d0d367270f09',
    'f1011746ab207a4d743a8354877b351a',
    '28e64f7a0de99bc23e4882791cc238d1',
    'ca804914ca07c06577670a888f813704',
    'da8934b49ac894c41b4a3462ae97ba3c',
    'b089d2c23063c80881345ef68a491133',
    'a68d4f182271c6b98f75ee8b5dcada3a',
    '2ab7cb11a93b6358b6a3603c55f91065',
    '3a97c6ac9411492eb7c8ee0e2a998f77',
    '1525f2cc7145d3baee62ab26240ee90e',
    'b8e08e5e71d04a592cad038a634d22dc',
    '5e6080d009477ea6a771872ddbf24845',
    '4db0d35c5c497901b3d7ed0aa5b9361a',
    '1a7aa06f102e96dba16ba87a13aeae65',
    'd1bffc55ea15cfd979553d3679808803',
    'b983cc05e48dce410db9925951f8056d',
    'e056eebcfb8c04323b60796b5078a48f',
    '6789e3c3515cfaa69d44a800b041ada6',
    '4e4b3cbdaed1aec9bc7bb07683555bdd',
    'b4298350f455f1282c73c3abf53e495c',
    '853528d1de9720efba9e110e9a7dd3f2',
    'efdb0b48f027fffccbb646a49c6c3e0a',
    '192fa97c269634f4de09eded97d87169',
    'c04a1f21ca51916f975fcdc6499eedec',
    'a971cb202c09811a2f476fb60011f681',
    '8a3e84098a22b2b8fe60376a838b49f5',
    'a240023effe200bb2d582f310ce7acb7',
    '4a7507b5323f915a414bdc0f65792df5',
    '4e534e6996894cb7f1208c453f9a383b',
    '810a3a63a61d1903f81a9ed71ebecef8',
    '20989fe5c02b51632136200e7beeb00f',
    'b61afeecf1d979df5d684d2debf196d1',
    'ef30ca01697dabd7cfcc7c4268e58b47',
    '870469fd6aa8eafeb6ff84a9d00ae0a7',
    '6cb039b5eae47c350406f634eea30aa3',
    '34cfbf4a1dc6022173b635e950a225ac',
    'c9c334a70842860fad2926a3c76649e4',
    'a347fb4212f216ec37b82da1ba68786e',
    '4827ae93d70c7768f7ffca61b7ddd066',
    'eed67c36683565e410776d53c44a5c79',
    '05696fdb0a77a02ada4ccc6ee95f06a2',
    'f6d467155e5e2acc7fa6f392b6f937f3',
    '67454a8db1e13f04a0a0ff422be78470',
    'abf5e3004d87e0788afc10ec2c3c6df1',
    'f2e4f090e4098939a725c0fde7d7b581',
    '475fd550d73c20364c2b18d5e5e03f79',
    '77847387a8a5c4777db162e13f2527d9',
    'f9a85785a9ffce48ab4cb984043cbdd8',
    'a4c723fc9d469c31c89fe175ddda977f',
    'ecf40bb4093885ec54e7d04bee39cbba',
    'd4b528a8a454b7349f32917f75123f23',
    '93e761ab032a477705edf9d736ab5ad4',
    'f3f5f60a74a36c1bf85a64d21e4263c0',
    'ed4bbc8b56e490342799705fd7c343dc',
    'eb5dffce7c6ebdc8e885c8254550e966',
    'd0bc80855abe5916215aeb2f93098688',
    '1afe4ace16bfae6e4b5265bd18a45b85',
    '0f2187b1ed1e61eb532b68c35bf46d14',
    'b002ccc095a05868c9dde7d7ea4d16d2',
    '0890851d8f7fb18e2e372f964429fab9',
    '61cf2580ad60343d078a310fce4ac606',
    '98119052c26d104ee01617acab40be65',
    'd3186017e3c1fa5a84e9da76f52aaa7b',
    '7e9eedcb4fe7ba665bb6b0c044014c9b',
    'fbd1a8ec45dc56df55b17afaf3217fba',
    '0a5599772edb5157fbbacd08d59a6737',
    'f77e21c0de5128e01393425b19cc00c0',
    '006344aaad97d5966ac129fc4653f377',
    '1f56c622fec1b67d7169b151c2728b71',
    '25963ebc4211f94efc76f6bdb770bc14',
    'c00509584eff8bc83f4034ecc7e08072',
    'f8c97e7d3aba4953d15f54542f3ad178',
    '68412c376f7b88d9a17e9d464262d7f6',
    '79e04947b4516284d4debc12e48ae9f5',
    '5707210e055f8d320297dd9e95450f06',
    '0504f42002b4f6fc1f932380a439b4c3',
    '90538b38ea7e32d553db7c977757ade7',
    '433e9cb4716d05420266621e4856959d',
    '4f12fad001ad5bb0a58a392381850472',
    '60a5ee8187c01c0e952ae9e560f68a0c',
    '6c551316719bd7e4711dcfca19874436',
    '42c1ffafb62e2a6050b7ab7f4792d00a',
    '31b1ad3893b38007c876d610595d420c',
    '662dfc2cc65258e8a091cf3f2697b53b',
    'd896a1f584008af9e201a82fc95f4015',
    'f7b4e1b9d6a2a50ff5569bfdc4f6c31f',
    'f667624072c23db2df52339d0c99e16a',
    '268940ead1af283d78b3f4db78106622',
    '4ff919d0e1d9c82dc55066f9a0ed997f',
    '09de77e96e96df043ff8665e7ebd8cb5',
    'd641ebbebb32f7fe63ed0c6fc614c1e4',
    '6b2d61a3dcc4047ce93f795ebce55680',
    '3fdbbf11cd1335a042d4cc5aff69257c',
    '619103a9cecac90f9294730ae0b644ce',
    'f93e029a12f1d0f6f68d9fbe40d5bd9d',
    '7a2b619ee44a98dc7c6e274371665015',
    '6b2e51ee6a5a867c87789810c4ed9811',
    '3641cbdbdb05c4510b114c6abc7a05ef',
    '84f6296d09368fbc566419d2d51dc29c',
    'e4fbec594a2328a15f522ae58b7f2cbb',
    '8bac96a15a872ba21f24b73fc52d32e8',
    '1a45e5311cfc3dfab4035b96827ec6ad',
    '6198e5a44fb474a6d4cf9898f8aafbf3',
    'ec62c504599d56112dbf9451fbc5d04d',
    '20c41aa601295af3f3ac4c62a227a81b',
    '59236f678cc0c4b76517d3afb20b890f',
    '55d10f20532787cc10d494c2cb90f6f2',
    'f38f22cb82a6411abc9103560c778c98',
    '3d2c4be56a4d1df2472063a2e1158653',
    '6f69d4993b75e329e72c4263020127b4',
    '30a90003be0fe4740968f7f24d932ec0',
    'f2503903db9969114f8dd05c5703004b',
    '226f6a572164b06e55bdc159e46586f6',
    'ea1676aa8b382285a9d9365125154af2',
    '67aaf4f5c235e790accce0ca299cfa81',
    '2c4d8f8cc62f5d9616a3a2afe6b7b3a2',
    '2cbd78bc2910d45c9a77c2c3d68b069a',
    'fc5d3692a74e4cb932d969b90d224ccd',
    'c5118daed35159d4713e337593576bd1',
    'b84eed82959ea12a04a06026367fd2e2',
    '427307d57b490c035e3507f1a20b6688',
    'f5830c2fd836c059f33940228771a0ec',
    '20c2c0958a63ab690af609f16086aa97',
    'a8c81a2201015a9aa0b13beb8b3e0847',
    '5caca4781f4db5404810b8690c3681d3',
    'a571fcc00d2bcc14a5ce9b0978c651e7',
    'd361cfd6474d3a6fd0fae99e87d13e57',
    '8b87af68121f26ce79cfbc13dbde4739',
    '5648e066d8b7bf1875a6ad5ffd7c09d7',
    '75b18416562af4ca39a3ec859f4634aa',
    '14e0d8ffced7e3d4331be8e7d0dc6463',
    '48344cabf9ec728adffbe800069e514d',
    'be750ded75be1c5a43c00861fd43b99a',
    '3008e12aec7d04b7163d75a957f0f511',
    'e6d240f974aed76a624b17b355238048',
    '9503808c80c4d5ead859dcab17e5f684',
    '445ddb89bb836287dff63c99f2fb5591',
    '5bd8f204a995159bc01138f6cf343567',
    '0d70699e01181bfac5254f7f282a5cb5',
    '7b9ea3c34f844ce7227f3de969123b2f',
    '11f04a6bf42f42aa1372300a684004fa',
    'ceefe85b740fab11f4670108316af2d8',
    '44d4ab30ded4deec6d2788e05764c706',
    'e2c63d7d5d7b4d422a5462aa3d298679',
    '36e9767ad5e58399020ee1d973ec3829',
    'c70c84dcb82ed8ffe2f83f38ac6e983d',
    'ccef309dfe78f0b58b620b6428e56409',
    '109c56f1149e12c1225e661295abb042',
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
# 禁用代理
Proxies = {
  "http": None,
  "https": None,
}
# Time是次数,我这个代码每次刷增加1分钟,默认值:1000
# 可刷时间,每次+1分钟,20次+20分钟
Times = 1000
# 这个是你在两次刷时间操作之间,停顿的秒数,建议不动,不然可能会被临时停止访问钉钉,默认值:5
SleepSecond = 5
# 这两个暂时别动,是每次刷的时间相关的,还没搞清楚
courseTime = 700
learnTime = 600
# 这三个也代表你是谁,第一次使用要修改,然后等出错再修改吧,不要把引号删了,出现未登录问题其次排查这两个
dd_sid = 'k0_6f280b17b18e8e5e1ff6_0b176f285e8e8eb1699698707e064b24b2ed63d72f0f'
isg = 'BBUVXHKQ59qNrMPAsFLj9WyYJBHPEskkXXnNDZe6RgzJ7jfgX2NJ9iJovPDYbuHc'
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
        response = requests.post(url=Url, data=json.dumps(Data), headers=tmp_headers, proxies=Proxies)
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
VideoInfosResponse = requests.get(VideoInfosUrl, proxies=Proxies).text.replace('\r', '').replace('\n', '').replace('\t', '')
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
