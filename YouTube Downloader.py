from pytube import YouTube
url = "Enter youtube url here"
my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

my_video = my_video.streams.get_highest_resolution()

my_video.download()
