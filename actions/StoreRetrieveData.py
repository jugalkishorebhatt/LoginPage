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
        self.client.put(entity)

    def __getData(self,key):
        key = self.client.key('StoreRetrieveData', "JugalBhatt")
        entity = datastore.Entity(key=key)
        result = self.client.get(key)
        print(result)
        print('getData Testing {}: {}'.format(result.key.name, result['name']))
        return result['name']

    def __getUser(self,user):
        try:
            key = self.client.key('StoreRetrieveData', user)
            entity = datastore.Entity(key=key)
            result = self.client.get(key)
            print('getUser {}: {}'.format("Testing", result))
            if result:
                return True
            else:
                return False    
        except expression as identifier:
            return False
        