import re

with open('/Users/ATOM/python learning/level1/access.log', 'r') as f:
  log = f.read()

ip_count = {}
with open('/Users/ATOM/python learning/level1/suspicious_report.txt', 'w') as f:
    f.write('--- Suspicious Requests ---\n')
    lines = log.split('\n')
    ip_count = {}
    for line in lines:
       if line == '':      # ← skip empty lines
         continue
    
       status = re.search('404|403', line)
       if status:
          ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
          f.write(f'{ip.group()} → {status.group()} → {line.split()[5].strip(chr(34))}\n')

          if ip.group() in ip_count:    # ← ip.group() not ip
            ip_count[ip.group()] += 1
          else:
            ip_count[ip.group()] = 1
       
    f.write('\n--- Request per IP ---\n')
    for ip, count in ip_count.items():
         f.write(f'{ip} : {count} bad requests\n') 

    f.write('\n--- Suspicious IPs ---\n')
    for ip, count in ip_count.items():
      if count >= 3:
         f.write(f'⚠️ {ip} : {count} bad requests — SUSPICIOUS\n')
      else: 
         f.write(f'{ip} : {count} bad requests — ok\n')  # ← no print() wrapper