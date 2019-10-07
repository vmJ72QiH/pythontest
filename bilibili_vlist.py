from urllib.request import urlopen
import json
import os

download_list = []
url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=312294516&page=1&pagesize=25'
# urlopen 打开网页的链接，read 读取，decode 解码
html = urlopen(url).read().decode('utf-8')
# 将 str 用 json 解析成 dict
a = json.loads(html)
# 获取视频的列表
b = a["data"]["vlist"]
# 获取每个视频的 aid 并添加到 download_list
for i in b:
    download_list.append("https://www.bilibili.com/av" + str(i["aid"]))
# 下载URL为：https://www.bilibili.com/av + $i["aid"]
for i in download_list:
    print(i)
