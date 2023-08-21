import pytube
url = input("enter video URL in youtube\n")
my_video = pytube.YouTube(url)
stream = my_video.streams.get_highest_resolution()
stream.download('E:')
print("complete successfully")