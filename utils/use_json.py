import json

class UseJson():
    def __init__(self):
        pass
    def read_data(self):
        with open('./static/data.json','r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data
    def get_data(self,key):
        self.data = self.read_data()
        return self.data[key]
    def write_data(self,key,value=None):
        data = self.read_data()
        with open('./static/data.json',"w+",encoding='utf-8') as f:
            data[key] = value
            return json.dump(data,f)
            
if __name__ == '__main__':
    client = UseJson()
    print(client.get_data('createRoom','111'))