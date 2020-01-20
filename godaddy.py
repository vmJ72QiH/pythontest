#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import json
import requests
import re

# url="https://api.ote-godaddy.com/v1/domains?statuses=ACTIVE&limit=20"
# headers={"Authorization": "sso-key UzQxLikm_46KxDFnbjN7cQjmw6wocia:46L26ydpkwMaKZV6uVdDWe"}
#
# P_get=requests.get(url, headers=headers)
# domain_list = P_get.json()
# print(domain_list)

domain_list = [{'createdAt': '2017-11-15T15:02:56.000Z', 'domain': '123qwe1123.com', 'domainId': 1260039,
                'expirationProtected': False, 'expires': '2021-11-15T15:02:56.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2021-12-30T15:02:56.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2018-01-14T15:02:56.000Z', 'transferProtected': False},
               {'createdAt': '2017-11-16T15:28:54.000Z', 'domain': '123qweq123.com', 'domainId': 1260142,
                'expirationProtected': False, 'expires': '2021-11-16T15:28:54.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2021-12-31T15:28:54.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2018-01-15T15:28:54.000Z', 'transferProtected': False},
               {'createdAt': '2019-03-11T07:30:44.000Z', 'domain': '123test.com', 'domainId': 1572355,
                'expirationProtected': False, 'expires': '2020-03-11T07:30:44.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': True, 'renewAuto': True,
                'renewDeadline': '2020-04-25T00:30:43.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-05-10T07:30:44.000Z', 'transferProtected': False},
               {'createdAt': '2019-02-15T20:22:45.000Z', 'domain': '123websiteautosignup.com', 'domainId': 1501192,
                'expirationProtected': False, 'expires': '2020-02-15T20:22:45.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-03-31T13:22:41.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-04-16T20:22:45.000Z', 'transferProtected': False},
               {'createdAt': '2019-02-15T19:47:08.000Z', 'domain': '123websitesissi.com', 'domainId': 1501191,
                'expirationProtected': False, 'expires': '2020-02-15T19:47:08.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-03-31T12:47:06.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-04-16T19:47:08.000Z', 'transferProtected': False},
               {'createdAt': '2017-01-03T17:54:02.000Z', 'domain': '12d12d12d.com', 'domainId': 1150472,
                'expirationProtected': False, 'expires': '2020-01-03T17:54:02.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-02-17T17:54:02.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2017-03-04T17:54:02.000Z', 'transferProtected': False},
               {'createdAt': '2019-01-24T15:19:34.000Z', 'domain': '1andonehundredthousand.com', 'domainId': 1500394,
                'expirationProtected': False, 'expires': '2020-01-24T15:19:34.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-03-09T08:19:29.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-03-25T15:19:34.000Z', 'transferProtected': False},
               {'createdAt': '2019-04-26T08:11:35.000Z', 'domain': '2222asdasdasd12321312321.xyz', 'domainId': 1815400,
                'expirationProtected': False, 'expires': '2020-04-26T23:59:59.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-06-10T01:11:30.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-06-25T08:11:35.000Z', 'transferProtected': False},
               {'createdAt': '2019-06-03T08:06:42.000Z', 'domain': '2321.life', 'domainId': 1897049,
                'expirationProtected': False, 'expires': '2020-06-03T08:06:42.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-07-18T01:06:37.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-08-02T08:06:42.000Z', 'transferProtected': False},
               {'createdAt': '2019-04-26T08:16:08.000Z', 'domain': '2asdasdasd12321312321.xyz', 'domainId': 1815418,
                'expirationProtected': False, 'expires': '2020-04-26T23:59:59.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-06-10T01:16:03.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-06-25T08:16:08.000Z', 'transferProtected': False},
               {'createdAt': '2019-04-26T08:17:19.000Z', 'domain': '2asdasdasd123213123221.xyz', 'domainId': 1815424,
                'expirationProtected': False, 'expires': '2020-04-26T23:59:59.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-06-10T01:17:16.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-06-25T08:17:19.000Z', 'transferProtected': False},
               {'createdAt': '2019-06-03T18:49:05.000Z', 'domain': '39102814.com', 'domainId': 1897052,
                'expirationProtected': False, 'expires': '2020-06-03T18:49:05.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-07-18T11:49:00.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-08-02T18:49:05.000Z', 'transferProtected': False},
               {'createdAt': '2019-12-20T04:05:38.000Z', 'domain': '3ddgd.com', 'domainId': 1901420,
                'expirationProtected': False, 'expires': '2020-12-20T04:05:38.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2021-02-02T21:05:33.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2020-02-18T04:05:38.000Z', 'transferProtected': False},
               {'createdAt': '2019-05-10T22:50:31.000Z', 'domain': '4242abramrsrd.com', 'domainId': 1891336,
                'expirationProtected': False, 'expires': '2020-05-10T22:50:31.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-06-24T15:50:28.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-07-09T22:50:31.000Z', 'transferProtected': False},
               {'createdAt': '2018-09-06T10:55:38.000Z', 'domain': '49c20c79-6391-41fe-91a1-30b033126987b.com',
                'domainId': 1280220, 'expirationProtected': False, 'expires': '2020-09-06T10:55:38.000Z',
                'holdRegistrar': False, 'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-10-21T10:55:38.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2018-11-05T10:55:38.000Z', 'transferProtected': False},
               {'createdAt': '2019-12-07T12:47:55.000Z', 'domain': '5.exchange', 'domainId': 1900930,
                'expirationProtected': False, 'expires': '2020-12-07T12:47:55.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2021-01-21T05:47:52.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2020-02-05T12:47:55.000Z', 'transferProtected': False},
               {'createdAt': '2019-10-11T06:02:13.000Z', 'domain': '5djjd1938.com', 'domainId': 1898968,
                'expirationProtected': False, 'expires': '2020-10-11T06:02:13.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-11-24T23:02:10.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-12-10T06:02:13.000Z', 'transferProtected': False},
               {'createdAt': '2018-08-01T10:59:36.000Z', 'domain': 'a2zfashion.com', 'domainId': 1278731,
                'expirationProtected': False, 'expires': '2020-08-01T10:59:36.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-09-15T10:59:36.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2018-09-30T10:59:36.000Z', 'transferProtected': False},
               {'createdAt': '2019-03-31T11:37:40.000Z', 'domain': 'a42inc.com', 'domainId': 1677396,
                'expirationProtected': False, 'expires': '2020-03-31T11:37:40.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': True,
                'renewDeadline': '2020-05-15T04:37:37.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-05-30T11:37:40.000Z', 'transferProtected': False},
               {'createdAt': '2019-07-17T09:13:50.000Z', 'domain': 'aabbd.com', 'domainId': 1897665,
                'expirationProtected': False, 'expires': '2020-07-17T09:13:50.000Z', 'holdRegistrar': False,
                'locked': True, 'nameServers': None, 'privacy': False, 'renewAuto': False,
                'renewDeadline': '2020-08-31T02:13:45.000Z', 'renewable': True, 'status': 'ACTIVE',
                'transferAwayEligibleAt': '2019-09-15T09:13:50.000Z', 'transferProtected': False}]

expiresdate = []
ooo = []
for i in domain_list:
    one = {}
    one['domain'] = i['domain']
    one['expires'] = i['expires'][:7]
    expiresdate.append(one)

expiresdate_sorted = sorted(expiresdate, key=lambda x: x['expires'])

def month_list():
    year_mon = time.strftime("%Y-%m", time.localtime())
    year_mon_s = year_mon.split("-")
    year = year_mon_s[1]
    mon = year_mon_s[0]
    year_mon_list = []
    for i in range(0, 12):
        e = i + int(year)
        k = mon
        e = "0" + str(e)
        j = k + "-" + e
        year_mon_list.append(j)
        if int(e) >= 12:
            e = "0" + str(int(e) - 11)
            k = str(int(mon) + 1)
            j = k + "-" + e
            year_mon_list.append(j)
    return year_mon_list

year_mon = month_list()

for i in expiresdate_sorted:
    for k in year_mon:
        if k in i['expires']:
            print(i)

