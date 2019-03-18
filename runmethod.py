#coding:utf-8
import requests
import json
from utils.use_json import UseJson
class RunMethod:
    def post(self,url=None,data=None,header=None):
        res = requests.post(url=url,data=data,headers=header,verify=False)
        return res.json()
    def get(self,url=None,data=None,header=None):
        res = requests.get(url=url,data=data,headers=header,verify=False)
        return self.handler(res)
    def put(self,url=None,data=None,header=None):
        res = requests.put(url=url,data=data,headers=header,verify=False)
        return self.handler(res)
    def delete(self,url=None,data=None,header=None):
        res = requests.delete(url=url,data=data,headers=header,verify=False)
        return self.handler(res)
    def handler(self,res):
        if res.status_code != 200:
            return res;
        return res.json()
    
    def main(self,method):
        method = getattr(self, method)
        return method

if __name__ == '__main__':
    jsons = UseJson()
    client = RunMethod()
    data = jsons.get_data("createRoom")
    data = json.dumps(data)
    client.main("post")("https://dev.yunsuit.com/index",data)