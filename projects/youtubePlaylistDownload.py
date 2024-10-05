from pytube import Playlist

plyList = Playlist(input('Enter playlist link:\n'))

# print('Qualities are:\n')

print('0 for video:')
print('1 for audio:')
ch = int(input('Enter choice:\t'))

print(f'Downloading: {plyList.title}')
if ch == 0:
    for video in plyList.videos:
        print(video.streams.first().download())
elif ch == 1:
    for video in plyList.videos:
        print(video.streams.first().download())
else:
    print('Enter valid choice!')


