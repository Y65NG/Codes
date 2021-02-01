import urllib.request

url = 'https://movie.douban.com/top250'
header = {

}

req = urllib.request.Request(url = url, headers = header)
