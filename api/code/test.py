import mmap,json,re,os,sys
def test():
    ips =[]
    with open(os.path.join(sys.path[0],'list_of_ips.txt'), 'rb') as f:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        for match in re.finditer(b'([0-9]{1,3}\\.){3}[0-9]{1,3}', m):
            ips.append(m[match.start():match.end()].decode("utf-8"))
    print(ips)

if __name__ == '__main__':
    test()