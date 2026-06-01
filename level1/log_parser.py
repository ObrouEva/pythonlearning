import re

log = """
Failed login from 192.168.1.100 at 09:15
Failed login from 10.0.0.5 at 09:22
Success login from 192.168.1.1 at 09:45
Failed login from 172.16.0.1 at 10:01
"""

ip_pattern = r'\d+\.\d+\.\d+\.\d+'
ip = re.findall(ip_pattern, log)

print(ip)

timestamps_pattern = r'\d+:\d+'  
timestamps = re.findall(timestamps_pattern, log)

failed = re.findall('Failed', log)
failed_logins = len(re.findall(f'Failed', log))

success = re.findall('Success', log)
success_logins = len(re.findall(f'Success', log))

print('Timestamps :', timestamps)
print('Failed logins :', failed_logins)
print('Success logins :', success_logins)



