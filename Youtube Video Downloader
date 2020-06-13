from pytube import YouTube
link=input("drop your YouTube url:")
yt=YouTube(link)
videos=yt.streams.all()  # This will stream all the formats available for download
video=list(enumerate(videos))  #this will index all the format in list starting with Zero
for i in video:
    print(i)  #Print all the formats for video download
print("enter the desired option to download")
dn_option=int(input("Enter the option:"))
dn_video=videos[dn_option]
dn_video.download()
print("downloaded successfully")
