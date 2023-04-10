# naver_api에서 블로그 검색결과 크롤링
import json
from config import client_id, client_secret
import urllib.request
import datetime
import json


# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id) #add_header 역할?
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node # 굳이?
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText 형태로 만들어줌

    url = base + node + parameters
    responseDecode = getRequestUrl(url) # [CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)


# [CODE 3]
def getPostData(post, jsonResult, cnt):
    # https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4
    # 위 링크에서 '4 출력결과' 필드와 동일하게 설정
    title = post['title']
    link = post['link']
    description = post['description']
    bloggername = post['bloggername']
    pDate = post['postdate']

    #pDate = datetime.datetime.striptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    #pDate = pDate.striptime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'link':link, 'postdate':pDate, 'bloggername':bloggername})

    return


# [CODE 0]
def main():
    node = 'blog' # 크롤링 할 대상
    srcText = input('검색어를 입력하세요:')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100) # [CODE 2]
    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt) # [CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) # [CODE 2]

    print('전체검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False) # 파이썬 객체를 JSON 파일로 저장

        outfile.write(jsonFile)

    print('가져온데이터 : %d 건' %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))



# 전체를 사용하는게 아니라 그 중에 main 부분만 사용하겠다는 의미
if __name__ == '__main__':
    main()

