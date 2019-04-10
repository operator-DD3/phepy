import hashlib

def hash(data):
    return hashlib.sha256(data.encode('utf8')).hexdigest()

message = "Hello World!"

for i in range(len(message)):
    print(hash(message[:i+1]))
