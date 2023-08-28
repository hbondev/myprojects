import asyncio
import tornado
import newproj1M
FDB = newproj1M.newproj1M()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("loginform.html")

    def post(self):

        email = self.get_argument('email')
        password = self.get_argument('password')
        if FDB.checkPassword(email , password):
            self.write('welcom')
        else:
            self.write('invalid password')



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", Login),

    ])

async def main():
    app = make_app()
    app.listen(80)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())