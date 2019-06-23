from helloworld import CookieJar

cookie_jar = CookieJar()
class SelfClosing(CookieJar):
    def take(self):

        self.open_jar()
        self.take()
        self.close_jar()

#print(cookie_jar.is_open())
#cookie_jar.open_jar()
with SelfClosing(cookie_jar) as jar:
    jar()
#with SelfClosing(cookie_jar) as jar:
    #jar.take()
    #print(jar.is_open())
#print(cookie_jar.is_open())