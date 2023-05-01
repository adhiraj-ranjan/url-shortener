from urllib.parse import urlparse
import random
import string

def get_string(length=7):
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    return random_string

def is_valid_url(url):
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except ValueError:
        return False

def has_illegal_characters(key):
    illegal_characters = ['.', '#', '$', '[', ']', '/', '\n', '\r', '\t', '?']
    for character in key:
        if character in illegal_characters:
            return True
    return False
