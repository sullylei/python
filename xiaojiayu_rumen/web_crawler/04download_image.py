import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
    
def get_page(url):
    html = url_open(url).decode('utf-8')
    start = html.find('current-comment-page')+23
    end = html.find(']',start)
    print(html[start:end])
    return html[start:end]
    
def find_images(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    print('a:'+str(a))
    while a != -1:
        b = html.find('.jpg',a,a+255)
        print('b:'+str(b))
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=',b)
    for each in img_addrs:
        print(each)
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        print('save_imgs_each:'+each)
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open('http:'+each)
            f.write(img)


def download_images(url):
    print(url)
    folder='images'
    pages=10
    #os.mkdir(folder)
    os.chdir(folder)

    page_num = int(get_page(url))
    
    for i in range(pages):
        page_num -= i
        #page_url = 'http://jandan.net/ooxx/MjAyMDA1MTctMTYy#comments'
        img_addrs = find_images(url)
        save_imgs(folder,img_addrs)
    
   


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/MjAyMDA1MTctMTcw#comments'
    download_images(url)





