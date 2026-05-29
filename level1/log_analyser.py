with open('/Users/ATOM/python learning/level1/access.log', 'r') as f:
  log = f.read()

line = log.split('\n')
total_request = len(line)
# print(total_request)
ip = line.split()[0]
print(ip)

# for i in range(0,total_request):
#   ip = line[i].split()[0]   # ← first word = IP, always correct

# ip_dict = {}
# for line_text in log:
#     ip = line_text.split()[0]    # extract IP
#     if ip in ip_dict:
#         ip_dict[ip] += 1
#     else:
#         ip_dict[ip] = 1

# for pair in ip_dict.items():
#     print(pair)


