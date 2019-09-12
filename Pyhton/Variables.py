#Favourite song info
#############
'''Initial variables
Line 6 - 9 String Variables
'''
Artist = "Bruno Mars"
Title = "Just the way you are" 
Album = "Doo-Wops & Hooligans"
Genre = "Pop"
#Size in MB (megabytes) / Float Variable
Size = 3.2
#Duration in seconds / Int Variable
Duration = 262

#Converting duration to minutes and seconds
minutes = Duration // 60
Duration %= 60
seconds = Duration
#Outputs
print("Artist: %s"% Artist)
print("Title: %s"% Title)
print("Album: %s"% Album)
print("Genre: %s"% Genre)

#float var changed to str
print(str("Size:%.2f"%Size)+"MB") \

#Convert int to minutes and seconds
print("Duration: %d:%02d" % (minutes, seconds)) 