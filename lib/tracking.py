from requests import post

class trytrack:

    def __init__(self,iptarget):
        # access key bisa diganti punya kalian sendirian
        self.ip = iptarget.replace('"',"")
        self.unkey = \
                "http://api.ipapi.com/{}?access_key=7d2d0f053402c59d89729950f153ff3c".format(
                        self.ip
                        )

    def here(self):
        self.result = post(self.unkey).text
        return self.result



