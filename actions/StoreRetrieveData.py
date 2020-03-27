from google.cloud import datastore


class StoreRetrieveData:

    client = None
    value = None
    def __init__(self):
        self.client = datastore.Client()
   
    def __saveData(self,key,value):
        key = self.client.key('StoreRetrieveData', key)
        entity = datastore.Entity(key=key)
        print('Key saveData {}: {}'.format(entity, value))
        entity.update(value)
        entity['done'] = True
        self.client.put(entity)
        
    def __getData(self,key):
        key = self.client.key('StoreRetrieveData', "JugalBhatt")
        entity = datastore.Entity(key=key)
        result = self.client.get(key)
        print(result)
        print('getData Testing {}: {}'.format(result.key.name, result['name']))
        return result['name']

    def __getUser(self,user,pwd):
        try:
            key = self.client.key('StoreRetrieveData', user)
            entity = datastore.Entity(key=key)
            result = self.client.get(key)
            print('getUser {}: {}'.format("Testing", result))
            result1 = result['stuPassword']
            print('Pwd: '+ result1)
            if result:
                return (True,pwd)
            else:
                return (False,pwd)    
        except expression as identifier:
            return False
        