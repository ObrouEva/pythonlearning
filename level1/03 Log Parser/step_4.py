import re

with open('level1/03 Log Parser/access.log', 'r') as f:
  text = f.read()

lines = text.split('\n')
counts = {}                          # outside the loop

for line in lines:
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    if ip_match:
        ip = ip_match.group()        # extract the string
        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1

sorted_ip = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print('=== Requests per IP ===')
for ip, count in sorted_ip[:5]:
     print(f'{ip}: {count} requests')