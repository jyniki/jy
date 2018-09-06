# -*- coding: utf-8 -*-

import requests
import os 
road=os.getcwd()
print(road)
url = 'http://jupter-oss.oss-cn-hangzhou.aliyuncs.com/file/opensearch/documents/1427/%E4%B8%8A%E6%B5%B7%E5%B8%82.csv?Expires=1535799159&OSSAccessKeyId=unrUSZdy4TBoR9Kz&Signature=lsg8XN%2Fzej32UqEuuZT01p5RnHU%3D&response-content-disposition=attachment%3B%20'
Headers = {u'accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           u'accept-encoding': u'gzip,deflate,br',
           u'accept-language': u'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           u'cookie': u'cna=oqsLFEF1JyoCAXPI4jx4snhW; isg=BMPDN7mYnK5YN1DaM8AxpCm6UYHBKlfx_Pn8NPWgXiKZtOPWfQjkyyUmKoRfD69y; __yunlog_session__=1535425954882; cnz=q6sLFKZzHmkCATziyHMEuVmf; l=AtDQjJrf9Rq80lViHQuXH3jboBQiorTj; login_aliyunid_pk=1789708939315587; login_aliyunid_token="B3CrIWfUUwTFPtPL6SODz3+7BRULA/wQlLY1EIspjRY="; aliyun_lang=zh; login_tianchi_ticket=6D70D1724E59AFE3D103E9270A322510F77728BB12A0B34CFEDE0FDADD94312D88B9C07CF7893408F68106D3D6AB36A79951999D727885A8869A0F4E801EDC9FED88C7F1483951E7D29E0A4AC055225849C146FA3376650FE00FE93433AFB0696B8AE1FCB8058E71; _tb_token_=2921aba8-ad7e-4359-962c-ac2ca928a865; login_aliyunid_csrf=_csrf_tk_1175535432239591; ping_test=false; t=009afed6f361d0f1b9d0e7be3f7303c5; _tb_token_=e3d64e577676e; cookie2=15ff280e8d45c2aa3a11e8bfb8233364; _hvn_login=6; csg=5b48a775; login_aliyunid="jy****"; login_aliyunid_ticket=M1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_8$$sLZf31qotJP22f9N2YMLwY6GllgVWw4n4QXBsluMHPof_BNpwU_TOTNChoB0; hssid=1ojiPOcMzqNmJAAgcRjOcsA1; hsite=6; aliyun_country=CN; aliyun_site=CN',
           u'connection':u'keep-alive',
           u'referer':u'https://tianchi.aliyun.com/datalab/index.htm?spm=5176.100073.5610778.11.1ff16fc1wUhqPb',
           u'upgrade-insecure-requests': u'1',
           u'user-agent': u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0'
           }
r = requests.get(url=url, headers=Headers, stream=True)
path=os.path.join(road,'downloads/test.csv')
f = open(path, "wb")
for chunk in r.iter_content(chunk_size=1024):
     if chunk:
         f.write(chunk)