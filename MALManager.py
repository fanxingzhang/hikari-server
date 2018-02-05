import requests
import xml.etree.ElementTree as ET
import pymysql

host = 'hikaridb.c9umgfyeannc.us-east-2.rds.amazonaws.com'
port = 3306
dbname = 'hikariDB'
user = 'UeusugiErii'
password = "SayonaraSensei123"


conn = pymysql.connect(host, user=user,port=port, passwd=password, db=dbname)


class Anime:
    def __init__(self, animeId):
        self.id = animeId
        self.title = None
        self.episodes = None
        self.image = None
        self.year = None

myAniList = []

def init():
    r = requests.get('https://myanimelist.net/malappinfo.php?u=domokun1134&status=all&type=anime')
    aniList = ET.fromstring(r.content)
    for anime in aniList.findall('anime'):
        animeId = anime.find('series_animedb_id').text
        title = anime.find('series_title').text
        episodes = anime.find('series_episodes').text

        myAnime = Anime(animeId)
        myAnime.title = title
        myAnime.episodes = episodes
        
        myAniList.append(myAnime)

def getList():
    return myAniList