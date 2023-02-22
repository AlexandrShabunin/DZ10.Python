import subprocess
import chardet

for sites in ['yandex.ru', 'youtube.com']:
    args = ['ping', sites]
    wow_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in wow_ping.stdout:
    result = chardet.detect(line)
print(line.decode(result['encoding']))

