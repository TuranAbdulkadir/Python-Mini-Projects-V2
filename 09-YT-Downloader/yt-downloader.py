from pytubefix import YouTube
url = input("URL: ")
YouTube(url).streams.filter(only_audio=True).first().download(filename="audio.mp3")
print("Done.")