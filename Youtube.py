from pytube import YouTube

url = "https://www.youtube.com/watch?v=-Aj8IlC0IEA"    #Enter the url of the video you want to download

video = YouTube(url)

print(video.title)    #Prints the title of the youtube video

print(video.thumbnail_url)    #Prints the link of the youtube thumbnail image

print(video.views)    #Prints the number of views of the video

print(video.description)    #Prints the description of the video

video = video.streams.get_highest_resolution()

video.download()    #Downloads the video in your current directory
