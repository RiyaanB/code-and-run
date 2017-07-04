from xenotables import XT, CC
c = CC(CC.localSock(), {})
print(c.ip, c.port)
x = XT(c.ip, c.port)
x.put("name", 90)
print(x.getAll())