import re
def find_message(text):
    return re.sub('[^A-Z]','', text)
