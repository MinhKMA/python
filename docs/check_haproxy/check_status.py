import json
from haproxystats import HAProxyServer
from prettytable import PrettyTable

url_monitor = ''
user_name = ''
pass = ''
haproxy = HAProxyServer(url_monitor, user = user_name  , password = pass)
data = json.loads(haproxy.to_json())
tables = PrettyTable(['Name backend', 'status', ''])
for i in range(len(data[haproxy.name]["backends"][0]["listeners"])):
    name_sv = data[haproxy.name]["backends"][0]["listeners"][i]["svname"]
    status_sv = data[haproxy.name]["backends"][0]["listeners"][i]["status"]
    type_sv = data[haproxy.name]["backends"][0]["listeners"][i]["act"]
    if type_sv = 1:
        a = 'ACTIVE'
    else:
        a = 'BACKUP'
    tables.add_row([str(name_sv), str(status_sv), a])
 print(tables)
