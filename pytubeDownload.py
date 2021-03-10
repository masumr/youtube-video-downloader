from flask import Flask,render_template,request,redirect,url_for
from string import Template
import pytube

import requests
def is_url_ok(url):
    return 200== requests.head(url).status_code


app=Flask(__name__)
app.config['SECRET_KEY']='DemoString'


@app.route('/complete')
def complete():
    return render_template('video.html')

@app.route('/download/<url>')
def  download(url):
    print(is_url_ok(url))
    if True==is_url_ok(url):
        vidTemplate=Template(render_template('video.html'))
        try:
            if True == is_url_ok(url):
                playlist = pytube.Playlist(url)
                print('Number of videos in playlist: %s' % len(playlist.video_urls))
                for video_url in playlist.video_urls:
                    print(video_url)
                    youtube = pytube.YouTube(video_url)
                    video = youtube.streams.first()
                    video.download()
            else:
                return render_template('index.html')


        except Exception as single:
            if True == is_url_ok(url):
                youtube = pytube.YouTube(url)
                video = youtube.streams.first()
                video.download()
            else:
                return render_template('index.html')


        return vidTemplate.substitute(youtube_id=url)
    else:
        vidTemplate = Template(render_template('index.html'))

   # vidTemplate=Template(render_template("video.html"))
    #return vidTemplate.substitute(youtube_id=vid)



@app.route('/', methods=['GET','POST'])
def hello():
    if request.method=='POST':
        url=request.form.get('url')
        download(url)
        return render_template('video.html')
    if request.method=='GET':
        return render_template('index.html')


if __name__=='__main__':
    app.run()