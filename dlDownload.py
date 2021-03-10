import youtube_dl

ydl_opts={}

def downloadedVideo():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

linkOfTheVideo=input("Copy Paste your Video: ")
zxt=linkOfTheVideo.strip()
downloadedVideo()