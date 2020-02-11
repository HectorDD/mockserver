import template 

class SuccessTemplate:
    def __init__(self,url,requestTriggers,response):
        self.url=url
        self.requestTriggers=requestTriggers
        self.response=response
class ErrorTemplate:
    def __init__(self,url,response):
        self.url=url
        self.response=response

class MockServer:
    def __init__(self,successTemplates,errorTemplates):
        self.successTemplates=successTemplates
        self.errorTemplates=errorTemplates
    def executeQuery(self,url,request):
        for i in self.successTemplates:
            if i.url == url:
                for j in i.requestTriggers.keys():
                    if j in request.keys():
                        if request[j] == i.requestTriggers[j]:
                            return i.response
        for i in self.errorTemplates:
            if i.url==url:
                return i.response
        return {'result':'not found'}

t=SuccessTemplate('/helloworld',{'key':'value'},{'result':'success'})
te=ErrorTemplate('/helloworld',{'result':'error','description':'mockError'})
mockServer=MockServer([t],[te])
assert(mockServer.executeQuery('/helloworld',{'key1':'value1','key':'value'})=={'result':'success'})
assert(mockServer.executeQuery('/helloworld',{'key1':'value1','key':'wrongvalue'})=={'result':'error','description':'mockError'})
assert(mockServer.executeQuery('/notMocked',{'key1':'value1','key':'value'})=={'result':'not found'})



        

