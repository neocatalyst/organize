#!/usr/bin/python
import shutil,os,time,sys

def stripnulls(data):
	#strip whitespace and nulls
	return data.replace("\00","").strip()


print("\n\t \t MUSIZ ORGANIZER \m/ \n \n")

path = raw_input('Enter the path u want to organise : ')
mode = int(input('\nPlz choose how you would like your music files to be oragnised :\n\n1.Artist \n2.Album \n3.Year \n\n:'))

if mode==1:
	(start,end)=(33,63)
elif mode==2:
	(start,end)=(63,93)
elif mode==3:
	(start,end)=(93,97)

else:
	print("enter an option between 1 and 4 ")
#copies all files to main path

for root,dirs,filenames in os.walk(path):
	for f in filenames :
		if os.path.splitext(f)[1]=='.mp3':
			try:
				shutil.move(os.path.join(root,f),path)
			except shutil.Error:
				pass

#delets all the empty directories now left

for root, dirs, files in os.walk(path, topdown=False):
    for name in dirs:
        shutil.rmtree(os.path.join(root, name))

for files in os.listdir(path):
	try:
		fsock=open(os.path.join(path,files),'rb',0)
		fsock.seek(-128,2)
		tagdata=fsock.read()
		fold=stripnulls(tagdata[start:end]).upper()
		if fold in os.listdir(path):
			shutil.move(os.path.join(path,files),os.path.join(path,fold))
		else:
			os.mkdir(os.path.join(path,fold),0777)
			shutil.move(os.path.join(path,files),os.path.join(path,fold))
	except OSError:
		pass

print("\n\n\t \t COMPLETE\n\n")
''' written by jaydev '''

