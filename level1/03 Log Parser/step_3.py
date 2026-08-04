import re

with open('level1/03 Log Parser/access.log', 'r') as f:
  text = f.read()

lines = text.split('\n')
print('=== Error Lines ===')

total = 0

for line in lines:
  ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
  date = re.search(r'\[(\d+/\w+/\d+:\d+:\d+:\d+)\]', line)
  status = re.search(r'" (\d{3}) ', line)
  if ip and date and status: 
      if status.group(1) in ('404', '500'):
        total +=1
        print(f'IP: {ip.group()} | Date: {date.group(1)} | Status: {status.group(1)}')

print(f'Total errors: {total}')