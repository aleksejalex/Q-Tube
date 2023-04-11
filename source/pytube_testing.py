import pytube as pt

the_link = "https://www.youtube.com/watch?v=nE_MF2fwbA4"

video_obj = pt.YouTube(the_link)
print(video_obj.title)
print(video_obj.streams)

print("as a list >>")


#video_stream = video_obj.streams.get_by_itag(134)  # that number you can get with previous line of the code
video_stream = video_obj.streams.get_highest_resolution()

# Open a file dialog to get the filename and path to save the file



video_stream.download(filename="testinggg.mp4")  # saves the video to chosen location with choosen name