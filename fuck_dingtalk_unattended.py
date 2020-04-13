# VER 3.1
import requests
import json
import time
import threading


# 用户更改区域开始
# 疯狗模式,快速刷时间
# 指定ulcookie,同时线程个数等于ulcookie个数,必须至少有一个
ulcookiesMadDog = [
    'a63bb43f5b79f3829fb05ee46e1f8d36',
    '2cacc32c31dec0534a6e8f26473343c1',
    '98c7b6dd1921f8cf139c7254dc697ee8',
    'e8d6a3be99d9c0fbc055ad8207d7811d',
    '59aa183769a3647e392e736271575505',
    '23d241ecc3b4e12004f73e3f11176690',
    'd5c30ed5e4eaa4d6dbc3280ec6f2d2a3',
    '4e22be58cb4cd9da0f2a79c89950818a',
    '5f460b5c3804b2526fd60e92bd9e3baf',
    '3a0f4b7a2929b837699b5c1c45678b4a',
    'bdcf53cd563fd2686b00fa3cede937d4',
    'd38f0a0f3d7bbc789da0111d83838ed3',
    'eb556436edcc633dfe584f8d100f0dc7',
    '5067c0300cefa64d2a9938f79c9b0f18',
    '38485a289420ade5bd17490567da8813',
    '64abec3d6a9745e917fb6bc527a622e5',
    'c7aebe8380e0b1c11c44f4c5e6132fbe',
    '3d0274af1c9420a3776dce998de7ef72',
    '667f7c9b1fa514c025b08c9115664562',
    '28350bc2aad38feb5ac370a3e133b582',
    '589271c714ed0b6b5480b5e4f527b833',
    'ecae032924c7b14b90006ab2f442ca32',
    'f6c54a59403be7e6c788914af13643df',
    '6914c79b27138ebbf9260a8b04ad9482',
    '099ae68d33dc711254ab1718e77deec0',
    'dffd72f704825acdee5d550d0af2ada9',
    '109a7d29a36c6ec2a03649d836978f97',
    '998499f92e4a28b35b8dd36cd8f4d346',
    '0b8ceb70768bcfcb59355e7f4e831cbb',
    '09998626c7c31574989c79de3fa62d67',
    '1e525fd338cbc6bdb1a682b2f7041cae',
    '7a900015a968508fe91b11bb27f8022d',
    'bd6047a70c9f02b75ca08c1c90847041',
    'e58736ad94d67564e05efc6c059fb71d',
    '26891fe33b21143717ac6ee489fea9a4',
    '7a343577b74ad2c1207422ef06817e93',
    '30f1839efcf28cb58c298b2d62d5ffd1',
    'c7d7a60bd308cb2e1a4ee7124f251ed5',
    'ced59ca828c5fac34aec45b66f86cb69',
    '1c46dd47708138617c942727be5ff105',
    '234de0a3e8c019939add02401e5787ff',
    'b99d23e788b5c8c2abbe8676bc1f55e5',
    'ce611e94de754015c1dd91c8daf144ca',
    '1df4fbcb369d4ff7f636db6626bc5f04',
    'd969e963c2065f513732ad64333de394',
    'b33dfe796af4a8d34445c9dc8c716ad6',
    '67ee33c15c88e80675d21af78c611c0f',
    'd5e229797325304dca3ab0854c9d212c',
    'c3a1ac92ae50204b72a08a4cd2520436',
    '6fc61a0d78e0ee9fb91a74431361ca3e',
    '63c127bab18d849235a52995e118d5e1',
    '3948bdd8328af753dc00244c25450d76',
    '03e3e1306e5c1582e741fcda45f2d923',
    '889554c282f87c2bb0cee329edd1006c',
    'fdb0de8a3f1359b8c4d35bb250d88d14',
    '97a74d3f70a932d23cadde5139e2a698',
    'ff1bbd3b005904591e6fe914e55fe46f',
    '777fa2179b7ad132b36a03aae839072e',
    '744864ac5da86a8068cd208ba7c9eece',
    'c6d128b945fcb9a8aa86e1b286097f61',
    'db40ec39824465c7042c1e1868f81f76',
    'a9d5b65bd1480a3b96e6590a2473bc2f',
    'b5764bc8ccecf0a74aabb21d4e09563b',
    '3ddc8235b5194433365bf14911d67dac',
    'c8346f51de16610dd36cbd3c79163f49',
    '840aa65e135e6738b4406deb00a69cb6',
    '8e2a9375e0ec8c2711b7093dd7c4c790',
    '5e08a396cd875f807888f0c7c1155f5b',
    'ed44721f03cf39c98f1757ea5dc31f06',
    '04a321e2bf42284c2c7f06b4b7314056',
    'cb652732ad943a3d3de9d6cfc2b097c7',
    '1191cf1772a5929d32f383af857681f0',
    '0fa9aebcd175e7843352eff19abd3102',
    'b7c61934e92eb32a458df3b76a72fb00',
    '31431ba4992ebf19bd5c343bdc4bb3bd',
    'e107ec9b23df5e741012f9008f85baf4',
    'f043bac7f9f0c79084ba3543a9622fe4',
    '803aca66a2887e6c77deb57e086a76e3',
    '0a63aaf476dd92ce7e1792f9a3029e1a',
    '386f6168e3f22bfdd132bb031c99c177',
    'd18688cea51f376b47a54bf4c76e7716',
    '74aba0bc202f545708b1481bafb01fc8',
    '801f09dba9f6568ae14447e1e85713e0',
    '596ad67f5f53826b0e95294d4c5af996',
    'c55db62a754d602adc5a35e7ff4b9104',
    '8cbd4100073fdbbe364b7ac30eb77217',
    'cee2eec5dc95af082c8c3d3089b543b9',
    '12b5cb0369baf22fc73814da454405fc',
    'de225a8eb314c12c21a763f583ccc110',
    'ad625839cb44e171c105eb37aec5aefe',
    '250ad938cf0461d09b7868aa1de33b55',
    'c9c212d990b8fc32cafb947bd19ba317',
    '894da9cb29c0a2dcf32683d17f52814b',
    '5cf68df666c6e55c04d89a0986157773',
    '88c910d68fe85fc10f7798cb00d1189f',
    '5311c820c4b1bf2be88811e89bd63ab1',
    'a32a67332db0bba553428604064b448b',
    'fef92c12e1afa5dd24b002f859d8f675',
    'ecab76d2932a43ee0b3d2f43a82437d4',
    '0b7af7fe4b1a796ffb4f255e651a59c3',
    '7e67cffa0f3967e0c650d025f09badd7',
    '53b8b5d50fe33abb9d22c9c179f16332',
    '732c230fb37ffada099e2d92f82e3cdc',
    '007880fd7367afe14afbeefad5b57e81',
    '5dd2dc3fd61aa9a746d20a3fcda537e6',
    'edc6290a5433ed6bef3d7dc5bff23fc1',
    'e8fa8a20854a1da449451838bb700c5f',
    '5bf955098a17322f53c4cac38cfef000',
    'd4e571b4d36f10c106819e904af78750',
    '1c0a8b4a29f2381a5ca3c4a9e6c7274d',
    '34da081f0f3bcbc4c598ce9864f7032c',
    'ebe01581b4d627eadd36b8e6cc301fc7',
    'f8c86e32870622ad1997e604775fe07f',
    'c615bb4fbca9ef77d8433be1a3c65b31',
    '79958a05b532f3696ccbc6b6279fdfb9',
    'a41cce1438321166683d6839e5b5c4d6',
    '15fabd78f80dc4bf48524ba867384bac',
    'feecdc5c37ea61510d9ebccc055ab44b',
    '888a9269a0a92446da456d27aa386435',
    '3e5912ee277e48e8a1321b8921ceb7b2',
    '67f29d4aef2f90a69ce5e00984394f29',
    '47bfe582f5a9531a61b79c0ba4b69fe5',
    'a9b8ee401a4f85901943756622623aae',
    '491ec9f6cfaa57ee37228981ab150a34',
    '86075761c752e02d6069738555b5aa17',
    '0c39691fb99fd5d5111c8783f7d5406e',
    '17224cee8bab6812721a591f2b83ff32',
    'afa7b4699283bce92873b024cef320ec',
    'b2b809a49bf0000352978a4f5f6374c8',
    '1e01bbbbcdd49a39ae59eb73f23a588b',
    'b6983adfc306869b34c3157badaf9549',
    'e8a74da0d5ee50b7c7c6a6be405292e6',
    '6e6b4e11507e002e4edfa1c268e50cd1',
    '7366ae84ae32f42f02b7790875de8e8e',
    '81ea89f9050580e67d27d0cf24e2b217',
    '31cedcd5e0448ecb386c6df0f569fab2',
    'f07ef1cf62aa4e634734851056a0572d',
    '593d32655426e81442c830085e44eccc',
    '0de89b3c1044bb463df8a4eb596528d8',
    'f8ab3af54755706cdc3f70b012e313a2',
    '4f148804a3297470e4047cb7aa9c1cba',
    '77a120cc0ccd2ea5309b8eac298df732',
    'f5fd32d37a39a2afb07dbe3f15ce3663',
    '10674e264bf4a8dc600a4d1895fa152e',
    '01bfcc26057a33af9853b0df54a6426b',
    'c96d5dd780cd3cb452ec4d2f239aa8c4',
    '674265efe11d7636dbd23631eb67dff4',
    'f5498218619071a46457a121ca3041b6',
    '4a744a88d93f34f31040e40d33f87090',
    'db4a65ee9e90b8fa5e4d8aff3ef6d36c',
    'eb540524c148e76cad2127f4dc38384f',
    '41b726f6fb2ef0bd5a3380e782bd1fb3',
    'db9420aa72fdac26a1f98f565251a29e',
    '709e854a98c116f0eacbe25367f61402',
    'a0425c1213e47fc5ff9496b765e42178',
    '106572bd0f0c55d513e3b541c7c83ebc',
    '2672f661feb31eb6691ddff9e2164cff',
    'b95b2bf7b3f5573953bf413ea59680bb',
    'a07591303a94893d11b17be84c22005f',
    'f919ea1555b00594b3ce5ddeb461bc9c',
    '1907839dd8bc0b515bc98a6a096b5294',
    'deadd991de7339393e67a0f953760105',
    '2d4cf8f5b844555f843574f6c4b0a875',
    '982e87a16253b68484506257f0fe9489',
    'c0bdaa6ed0a36c75cf4c51d72c8cc0ba',
    'c908056cc57ea020d3cd746a89f2da72',
    '79c603229b25f71ea63410b0a7d42f21',
    'd90f87e708c8b4c75234efeeaeeb55e6',
    'cfd555cccd18044418ad13a10bf369e6',
    'e6f240b788f15612e133d32c935f9899',
    '266c0f7f6089aa84c70c9192b7676360',
    '587d2f2016718ebd6684de7b2fa2eb71',
    'bf7bdd87bc0486d98c512a4c6dcbd940',
    '35e6342b28b61f2ef33c9a9ceaedbe21',
    '392334f4cd3723b29093b1cf2343bff0',
    'd76a9ac3bb26d1e095707a6eeb6ceaf2',
    '13d7535c53db7b2c8d4f65669f87b12a',
    '5f3f867ed0f57e37886c335f24127608',
    'ad758477cb07669d3cac22ad8c513a3a',
    'f0fcfaea563eef0435ac5fac0ded35e3',
    '0292006e2548535a226891440d185134',
    '70f79be10f04afd7febbb5bed91885f2',
    '48974a3b79266f2c329f3f8ad752b1ef',
    '3d1935b3201b4c0017e12fc7d0a85012',
    '85322edd508f370af96f98ac60b049d2',
    'f9dbdcc9f6ea59d7e6f452f2288853b2',
    '591abd13617f7bd3f337e8ff7b16ceda',
    'de738c63918b94a7f6efda6d1a82eef8',
    '265df9bc27f3e01be731cb330551dd23',
    '1d9d70e44657535b1612d03050db07ca',
    'efa3518d69b2f488740e952b4af6a04c',
    'b8d2b3ad84f97cb7c77a10879f2d5d9e',
    '94a167d5748563d649bf8af43f075c6a',
    '42fa6d4e0f81d95ab3750cbc4b4d75f1',
    '4680789651cbe89263790eee104188c1',
    'da3bb4e5159d389bf4c3fa659fce30c7',
    'c688aded90ba9e992a0c244493d6bd0c',
    '8cd1cfa29b9f0ca2093de0bbcf4a3914',
    'ec7f721149429a4e46df85a228566824',
    '8261d9ee09955800913cd39f5157511f',
    '1c0382b53cd6302faa4a94f71b407d1c',
    '6a459e177f3ffdb09d857d41b8c313b5',
    '578aa0399543a89b5d51615b0b159c4d',
    '67ae8b78918ba49ac9e6283a620863ca',
    'c8795cbab1f23ce2e8bb4945e0cae53a',
    '0d22f98ebfbc1bda870de00d6d98ab27',
    '3d58e4be09758d39df54bbbe9185108e',
    '532fa071358aa7ec4081255cfefb5f8c',
    '2fa901e917551207c59a6164d5289667',
    '9e39b230f93092921762be04fc0235a9',
    '7a8d8a325fc5f71024c49fd954d8b8e2',
    'c31babf4df7ea5377f4a6f4138403b31',
    '2eb18d32f830e3079b1fb23f76392e2b',
    '9a3ff567a0e9f36e82036bdb52f366c7',
    '60e1b5e94450814f3189ed97d69a96b4',
    'b249afe68915be0d197a21ac89ba03aa',
    'a8b73dea55795b6707bab5cd56ca5810',
    'dca81854b6060306fa0a0df48225be9c',
    'fde256f21aaf905e9351222f0fe6ecc7',
    'eb71b03a0a26df5bc30497381d386610',
    'f6f9371f73f2220b7182690511ec8e27',
    'd7187e56ca2688441a9a8d0d899bbc8a',
    '0b8c4862f92d6e0afaba2af4c47dee70',
    'bfca01f4ed6d2591165bd04cdd6975f0',
    'a473b0ea7cc2bc7517d450eb6579f646',
    '2894f8bfabdfa120ab0d4644c465b827'
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
dd_sid = 'k0_01b90b5a37d1925e15d3_0b5a01b95e92d1371b62aabd08e07759b4a382b0105d'
isg = 'BAMDZwSaWfgQBhX2kijt2-4ikseteJe6H7O7mzXgB2LZ9CIWvUmCCxiiaoa61O-y'
# 这两个可能每两三天要更新一次,出现未登录问题其次排查这两个,ulcookie请在上面指定
sign = '7c2c0770a826740882803e8e7250c430'
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
