from pytube import YouTube

link=input('Enter the video link:\t')

videoDetails=YouTube(link)
print('Title:',videoDetails.title)          # video title
print('Thumnail link:',videoDetails.thumbnail_url)          # video thumnail link



print('0 for video:')
print('1 for audio:')
ch=int(input('Enter choice:\t'))
if ch==0:
    content=videoDetails.streams.filter(only_video=True)
elif ch==1:
    content=videoDetails.streams.filter(only_audio=True)
# content=videoDetails.streams.all()       # all video format (audio & video)
else:
    print('Enter valid choice!')

vid_List=list(enumerate(content))
print('Videos Streaming options:\n')
for i in vid_List:
    print(i)
print()

strmQuality=int(input('Enter quality:\t'))

content[strmQuality].download()
print('download successfull')