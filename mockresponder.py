
class SuccessTemplate:
    def __init__(self,url,requestTriggers,response):
        self.url=url
        self.requestTriggers=requestTriggers
        self.response=response
class DefaultTemplate:
    def __init__(self,url,response):
        self.url=url
        self.response=response

class MockResponder:
    def __init__(self,successTemplates,defaultTemplates):
        self.successTemplates=successTemplates
        self.defaultTemplates=defaultTemplates
    def executeQuery(self,url,request):
        for i in self.successTemplates:
            if i.url == url:
                if request != None:
                    for j in i.requestTriggers.keys():
                        if j in request.keys():
                            if request[j] == i.requestTriggers[j]:
                                return i.response
                
        for i in self.defaultTemplates:
            if i.url==url:
                return i.response
        return {'result':'not found'}

t=SuccessTemplate('/helloworld',{'key':'value'},{'result':'success'})
te=DefaultTemplate('/helloworld',{'result':'error','description':'mockError'})
mockResponder=MockResponder([t],[te])
assert(mockResponder.executeQuery('/helloworld',{'key1':'value1','key':'value'})=={'result':'success'})
assert(mockResponder.executeQuery('/helloworld',{'key1':'value1','key':'wrongvalue'})=={'result':'error','description':'mockError'})
assert(mockResponder.executeQuery('/notMocked',{'key1':'value1','key':'value'})=={'result':'not found'})



        

