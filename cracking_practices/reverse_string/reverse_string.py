# PROBLEM DOMAIN
# Given a string, return it in reverse order.

# Function that receives a string and reverse it in place.
# BUT Python does not allow you to swap out characters in a string for another one; strings are immutable.
def reverse_string(srt_to_rev):
    if not srt_to_rev : return
    srt_to_return = ''
    for i in range(0, len(srt_to_rev)):
        srt_to_return = srt_to_rev[i] + srt_to_return

    return srt_to_return

