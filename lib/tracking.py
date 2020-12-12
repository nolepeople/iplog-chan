from requests import post

class trytrack:

    def __init__(self,ip):
        self.ip = ip.replace('"',"")
        self.url = \
        "http://api.ipapi.com/{}?access_key=".format(self.ip)

    def here(self):
        #kalian bisa gunakan key sendiri bisa daftar di ipapi.com
        self.key = "7d2d0f053402c59d89729950f153ff3c"
        self.req = post("{}{}".format(
            self.url,self.key
            )).text
        return self.req
