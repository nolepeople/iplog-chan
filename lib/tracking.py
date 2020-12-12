from requests import post

class trytrack:

    def __init__(self,ip):
        self.ip = ip.replace('"',"")
        self.url = \
        "http://api.ipapi.com/103.119.54.215?access_key="

    def here(self):
        self.key = "7d2d0f053402c59d89729950f153ff3c"
        self.req = post("{}{}".format(
            self.url,self.key
            )).text
        return self.req
