# Given a expresion, return True is next the opening tags "({<" has their closed tag in the right possition.
# (1+2) : True; 1+2): False; (1+2<) 1> : False; (1+2) <1> - {5+9}: True


from collections import deque


def is_tag(ch):
    valid_tags = ["[", "]", "(", ")", "<", ">", "{", "}"]
    if ch in valid_tags:
        return True
    else:
        return False


def is_opening_tag(ch):
    opening_tags = ["[", "(", "<", "{"]
    if ch in opening_tags:
        return True
    else:
        return False


def are_matching_tag(opening, closing):
    # instead of using a if for each tag, I will use a dictonary where the key are the opening tags, and the value the closing ones.
    tags_dict = {"[": "]", "(": ")", "<": ">", "{": "}"}
    # I could use match with python 3
    if tags_dict[opening] == closing:
        return True
    else:
        return False



def check_expresion(expresion):
    stack = deque()
    last_appended_tag = ""

    for ch in expresion:
        if is_tag(ch):
            if is_opening_tag(ch):
                stack.append(ch)
            else:
                if len(stack) > 0 :
                    last_appended_tag = stack.pop()
                    if not are_matching_tag(last_appended_tag, ch) : return False
                else:
                    return False

    if len(stack) > 0 : return False


    return True


