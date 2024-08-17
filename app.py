from flask import Flask, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

# Set up paths
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Function to download YouTube video and convert to .mp3
def download_youtube_audio(url, output_path=DOWNLOAD_FOLDER):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        mp3_file = os.path.join(output_path, f"{info_dict['title']}.mp3")

    return mp3_file

# Route to list all downloaded songs
@app.route('/')
def index():
    files = os.listdir(DOWNLOAD_FOLDER)
    mp3_files = [f for f in files if f.endswith('.mp3')]
    file_list = ''
    for f in mp3_files:
        file_list += f'<li>{f} <a href="/delete/{f}">Delete</a></li>'
    return f'''
    <!doctype html>
    <title>YouTube to Music Player</title>
    <h1>Enter YouTube Music URL</h1>
    <form method=post action="/download">
      <input type=text name=url placeholder="Enter YouTube URL">
      <input type=submit value="Convert and Download as MP3">
    </form>
    <h2>Downloaded Songs:</h2>
    <ul>
      {file_list}
    </ul>
    '''

# Route to handle the download request
@app.route('/download', methods=['POST'])
def download():
    youtube_url = request.form['url']
    if youtube_url:
        download_youtube_audio(youtube_url)
    return redirect(url_for('index'))

# Route to handle the delete request
@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=19876)
