from googleapiclient.discovery import build
import os, glob

#================================================================================
# Reference for https://qiita.com/shobota/items/eef7143b574397c8d295
#================================================================================
def initYoutube(API_KEY):
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"
    return build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

def getIdListFromPlaylist(id_,youtube):

    nextPageToken = 'start'
    response = []

    while(nextPageToken is not None):

        if(nextPageToken == 'start'):
            search_response = youtube.playlistItems().list(
            part= 'snippet',
            playlistId=id_,
            maxResults = 50,
            ).execute()
        else:
            search_response = youtube.playlistItems().list(
            part= 'snippet',
            playlistId=id_,
            maxResults = 50,
            pageToken = nextPageToken
            ).execute()

        if('nextPageToken' in search_response):
            nextPageToken = search_response['nextPageToken']
        else:
            nextPageToken = None
        
        for item in search_response['items']:
            response.append(item['snippet']['resourceId']['videoId'])

 
    response.reverse()   
    return response

def getCountDetails(id_, youtube):

    #50件ずつに分割
    idLists = split_list(id_,50)
    response = []

    for idList in idLists:
        search_response = youtube.videos().list(
        part= 'statistics,snippet',
        id=idList,
        ).execute()

        response.extend(search_response['items'])

    return response

def setCountDetail(idList,youtube):

    result = getCountDetails(idList,youtube)

    res = []
    
    for item in result:
        # ["タイトル", "URL"]
        List = []
        List.append(item['snippet']['title'])
        List.append('https://www.youtube.com/watch?v='+item['id'])
        res.append(List)
        # print(len(res)-1, 99-len(res)+2, List)
    return res

def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]



API_KEY = 'AIzaSyDubyMGiVSmzbLjtxJX-AYuKFNL_3KfYXY' #My API key
FILENAME = 'Youtube'
youtube = initYoutube(API_KEY)

def main(url):
    return setCountDetail(getIdListFromPlaylist(url,youtube),youtube)