from pytube import YouTube

link = str(input("enter the yt link: "))
yt = YouTube(link)
yt.streams.get_highest_resolution()
try:
	yt.streams.first().download()
	print("Downloaded successfully")

except:
	print("Access Denied")
