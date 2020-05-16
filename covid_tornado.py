from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.mohfw.gov.in/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

rows = soup.findAll('tr')
head = rows[0].findAll('th')

class CovidIndia(RequestHandler):
    def get(self):
        for row in range(1,34):
            d = {}
            for col in range(len(head)):
                a = (head[col].text.strip())
                b = (rows[row].findAll('td')[col].text.strip())
                c = {a:b}
                d.update(c)
            self.write(json.dumps(d))
def make_app():
    urls = [("/",CovidIndia)]
    return Application(urls)
if __name__=="__main__":
    app = make_app()
    app.listen(8090)
    IOLoop.instance().start()
