from urllib.request import urlopen
# python -m pip install --upgrade requests
import requests

# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip())         # Remove trailing newline
#             break


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('../../resource/RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()




