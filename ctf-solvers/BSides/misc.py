from PIL import Image
import pytesseract
import os

num = 50
while 1:
	img = Image.open("password.png")
	w,h = img.size
	img1 = Image.new("RGB",(w,h),color='black')
	pixel = img.load()
	pixel1 = img1.load()

	def rotate(l, n):
	    return l[n:] + l[:n]

	rot = open("shift_keys","rb").readlines()

	for j in range(h):
		l = []
		for i in range(w):
			l.append(pixel[i,j])
		l = rotate(l, int(rot[j][:-1].decode()))
		for i in range(len(l)):
			if l[i] != (0,0,0):
				pixel1[i,j] = (255,255,255)

	img1.save('pass.png')
	passwd = pytesseract.image_to_string(Image.open('pass.png')).strip()
	print(passwd)
	os.system("unzip -P "+passwd+" UnzipME"+str(num)+".zip")
	num -= 1
