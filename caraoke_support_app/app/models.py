from django.db import models
import requests
from urllib import request
from bs4 import BeautifulSoup
import time

class Singer(models.Model):
    name = models.CharField(max_length=100)

    def update(self):#歌手の曲をBSで拾ってきてデータベースに無い曲なら新しく作り、各々に対してscrapingする

        return

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT)
    lyrics = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('title', 'singer')

    def __str__(self):
        return self.title

    def scraping(self, url):
        # get html
        response = request.urlopen(url)
        data = response.read()

        # set BueatifulSoup
        soup = BeautifulSoup(data, "lxml")

        select1 = soup.find("div", id="mnb")
        select2 = select1.find("div", class_="lbdy")
        select3 = select2.find("p", id="Lyric")
        scraped_lyric = str(select3).replace('<p id="Lyric">', '').replace('</p>', '').replace('<br/>', '\n')
        self.lyrics = scraped_lyric
        self.save()
        print("scraped")
        time.sleep(1)

