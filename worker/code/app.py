from flask import Flask,request
import ips,os,sys,geoip,json
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

def getIps(max):
    return ips.getIps(os.path.join(sys.path[0],'data/list_of_ips.txt'),max)

def getGeoip(filter,ips):
    list_ips = json.loads(ips)
    response =[]
    for (ip) in list_ips:
        response.append(geoip.getGeoip(ip,filter))
    return json.dumps(response) 

@app.route('/filter/')
def filter():
    data = json.loads(request.json)
    limit = data['limit']
    geoip = data['geoip']
    ips= getIps(limit)
    response=getGeoip(geoip,ips)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

