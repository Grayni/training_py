import re
string = 'Cat\'s power!'.lower()
print(re.split('[^a-z]', string))
