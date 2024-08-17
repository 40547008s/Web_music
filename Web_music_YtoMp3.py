from flask import Flask, request
import yt_dlp
import os

app = Flask(__name__)

# Set up paths
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Function to download YouTube video and convert to .webm
def download_youtube_audio(url, output_path=DOWNLOAD_FOLDER):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        webm_file = os.path.join(output_path, f"{info_dict['title']}.webm")

    return webm_file

# Function to play .webm using VLC
def play_webm(webm_file):
    player = vlc.MediaPlayer()
    media = vlc.Media(webm_file)
    player.set_media(media)
    player.play()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form['url']
        if youtube_url:
            webm_file = download_youtube_audio(youtube_url)
            #play_webm(webm_file)
            return f'<p>Playing: {webm_file}</p>'
    return '''
    <!doctype html>
    <title>YouTube to Music Player</title>
    <h1>Enter YouTube Music URL</h1>
    <form method=post>
      <input type=text name=url placeholder="Enter YouTube URL">
      <input type=submit value="Convert and Play">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)