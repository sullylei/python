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
    os.mkdir(folder)
    print('path:'+ str(os.path))
    os.chdir(folder)
    img_addrs = find_images(url)
    save_imgs(folder,img_addrs)


def find_next_old_page(url):
    next_older_page = ''
    page_num = 0
    page_num_str = get_page(url)
    if page_num_str != '':
        page_num = int(page_num_str)
    old_page_num = page_num -1
    print('old_page_num:'+str(old_page_num))
    if old_page_num < 1:
        return next_older_page

    html = url_open(url).decode('utf-8')
    current_start = html.find('current-comment-page')+23
    start = html.find('a href=',current_start)
    end = html.find('>',start)
    print('start is {0} and end is {1}'.format(start,end))
    
    next_older_page = html[start+8:end-1]
    print('next_older_page:'+next_older_page)
    return next_older_page

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/MjAyMDA1MTctMTc1#comments'
    download_images(url)
    while len(find_next_old_page(url))>0:
        next_older_page = find_next_old_page(url)
        download_images(next_older_page)
    





