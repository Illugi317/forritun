# ...add your function(s) here

def open_file(filename:str):
  try:
    return open(filename,"rb")
  except:
    return None

# This line you can keep as is
file_name =input("Enter file name: ")
ans = 0
f = open_file(file_name)
x = 0
f.seek(0,2)
eof = f.tell()
f.seek(0,0)
total = eof - x

print(ans)