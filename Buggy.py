import requests
from requests.compat import urljoin, quote_plus
from bs4 import BeautifulSoup
max_depth = 2
lines = []
crawled = []

write = open("WhoFull.txt", "w+", encoding="utf8")

def crawl(url, depth):
    if depth == max_depth:
        print("PRINTING " + url)
        buffer = requests.get(url)
        x = BeautifulSoup(buffer.content, "html.parser")
        string = x.find_all("table").__getitem__(0).get_text()
        if "Next episode" in string:
            string = (string[:-(len(string)-string.find("Next episode"))])
        elif "Next Episode" in string:
            string = (string[:-(len(string) - string.find("Next Episode"))])
        else:
            string = (string)

        write.write(string)
    else:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        for link in soup.find_all('a'):
            s = urljoin(url, (link.get('href')))
            print(s)
            if s not in crawled and "Doctor" in s and "index" not in s:
                crawled.append(s)
                crawl(s, depth+1)


crawl("http://www.chakoteya.net/DoctorWho/index.html",0)
write.close()
print(lines)
