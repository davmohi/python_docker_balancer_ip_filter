import mmap,json,re
def getIps(file,max):
    ips =[]
    with open(file, 'rb') as f:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        for match in re.finditer(b'([0-9]{1,3}\\.){3}[0-9]{1,3}', m):
            ips.append(m[match.start():match.end()].decode("utf-8"))
            max-=1
            if max==0:
                break
    return json.dumps(ips) 