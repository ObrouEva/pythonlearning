with open('/Users/ATOM/python learning/level1/access.log', 'r') as f:
  log = f.read()

lines = log.split('\n')

total_request = 0
ip_dict = {}
four_four = 0
four_three = 0
two = 0

for line in lines:
    if line == '':      # ← skip empty lines
        continue
    total_request += 1
    ip = line.split()[0]
    status = line.split()[-1] 
        # step 1 : get the IP
    if ip in ip_dict:       # step 2 : count it
        ip_dict[ip] += 1
    else:
        ip_dict[ip] = 1
    
    if status == '404':
      four_four +=1
    if status == '403':
      four_three += 1
    if status == '200':
      two += 1

unique = len(ip_dict)   # number of unique keys = unique IPs
  
sorted_ip = sorted(ip_dict.items(), 
                      key=lambda x: x[1],
                      reverse=True)

print(f'--- Log Analysis Report ---\nTotal requests  : {total_request}\nUnique IPs      : {unique}\n404 errors      : {four_four}\n403 errors      : {four_three}\n200 responses   : {two}\n\nTop 3 most actives IPs :')

for  i, (active, request) in enumerate(sorted_ip[:3], 1):
   print(f'{i}. {active} : {request} requests')
