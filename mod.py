f = open("./sublime_text.exe","rb")
data = f.read()
f.close

f = open("./sublime_text.exe.back","wb")
f.write(data)
f.close()

f = open("./sublime_text.exe","wb")
data = data.replace(b"\x00\x00\x31\xC9\x80\x78\x05\x00",b"\x00\x00\x31\xC9\xC6\x40\x05\x01")
data = data.replace(b"\x0F\x94\xC1\x8D\x14\x09\x80\x78",b"\x48\x85\xC9\x8D\x14\x09\x80\x78")
f.write(data)
f.close()
