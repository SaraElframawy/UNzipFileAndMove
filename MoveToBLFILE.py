import os 
source = "/home/sara/Downloads/Test"
destination ="/home/sara/Downloads/Blfiles"
try:
    if os.path.exists(destination):
        print("THere is already a file there")
    else: 
     os.replace(source,destination)
     print(source+'was moved')

except FileNotFoundError:
    print(source+"was not found")
