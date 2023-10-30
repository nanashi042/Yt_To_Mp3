# importing packages 
from pytube import YouTube 
import os 

def downloader(url):
    yt = YouTube(str(url))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    destination = "./static/audio"  # You don't need to add a space at the end

    # download the file
    out_file = video.download(output_path=destination)

    # Define the new file name
    new_file_name = os.path.join(destination, "music.mp3")

    # Rename the downloaded file to "music.mp3"
    os.rename(out_file, new_file_name)

    # Result of success
    print(yt.title + " has been successfully downloaded as music.mp3.")

