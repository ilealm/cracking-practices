# PROBLEM DOMAIN
# URLify 1.3: Write a method to replace all the white spaces in a str_to_url with '%20'.
# You may assume that the str_to_url has sufficient space at the end to hold the additional characters
# and that you are given the true length of the str_to_url.


# In Python, strings are immutable, so you can't change their characters in-place.
# create a function (URLify) that receives two parameters: str_to_url and length
def URLify(str_to_url, letters_count):
    URLify_string = ''
    str_to_url = str_to_url.strip()
    for i in range(0, len(str_to_url)):
        if str_to_url[i] == ' ':
            URLify_string += '%20'
        else:
            URLify_string += str_to_url[i]

    return URLify_string


