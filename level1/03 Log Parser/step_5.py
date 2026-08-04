import re

with open('level1/03 Log Parser/access.log', 'r') as f:
  text = f.read()

lines = text.split('\n')
requests = 0
errors = 0
counts = {}

with open('level1/03 Log Parser/report.txt', 'w') as f:
  for line in lines:
      
      #extract Ip, daten status with re.search()
      ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
      date = re.search(r'\[(\d+/\w+/\d+:\d+:\d+:\d+)\]', line)
      status = re.search(r'" (\d{3}) ', line)

      #counts requests and errors
     
      if ip and date and status: 
        requests += 1
        if status.group(1) in ('404', '500'):
            errors +=1

        ip_str = ip.group()        # ← extract string
        if ip_str in counts:
            counts[ip_str] += 1
        else:
            counts[ip_str] = 1
      
  sorted_ip = sorted(counts.items(), key=lambda x: x[1], reverse=True)

  f.write('===== Log Report ======\n')
  f.write(f'Total errors : {errors}\n') 
  f.write(f'Total requests : {requests}\n')
  f.write(f'\n=== Requests per IP ===\n')
  for ip, count in sorted_ip[:5]:
     f.write(f'{ip}: {count} requests\n')
  f.write('\n===== Error Lines =====\n')
  for line in lines:
      
      #extract Ip, daten status with re.search()
      ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
      date = re.search(r'\[(\d+/\w+/\d+:\d+:\d+:\d+)\]', line)
      status = re.search(r'" (\d{3}) ', line)

      if ip and date and status: 
          if status.group(1) in ('404', '500'):
            f.write(f'IP: {ip.group()} | Date: {date.group(1)} | Status: {status.group(1)}\n')
  f.write('=======================')