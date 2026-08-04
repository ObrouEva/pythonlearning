import re

with open('level1/03 Log Parser/access.log', 'r') as f:
  text = f.read()

lines = text.split('\n')

for line in lines:
    ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    date = re.search(r'\[(\d+/\w+/\d+:\d+:\d+:\d+)\]', line)
    status = re.search(r'" (\d{3}) ', line)
    if ip and date and status: 
       print(f'IP: {ip.group()} | Date: {date.group(1)} | Status: {status.group(1)}')