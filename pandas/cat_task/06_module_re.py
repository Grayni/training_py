import re
string = 'Cat\'s power!'
print(re.split('[^a-z]', string))