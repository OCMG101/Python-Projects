from pytube import YouTube
url = "https://youtu.be/SJ79Z0nn2x4?si=EcJqTUuQeqmcnuXC"
my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

my_video = my_video.streams.get_highest_resolution()

my_video.download()