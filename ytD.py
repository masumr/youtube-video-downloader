from pytube import Playlist

p=Playlist("https://www.youtube.com/playlist?list=PL0BgiG4bfDwrAVa--1MgGDc3fXkr_NFLF")


for video in p.videos:
    video.streams.first().download()