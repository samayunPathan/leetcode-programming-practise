def imple_str(haystack,needle):
    h=haystack.split(needle)
    print(h)
    h=':'.join(h)
    print(h)
    for i in range(len(h)):
        if h[i] ==':':
            return i
    return -1


# haystack = "sadbutsad"
# needle = "sad"
haystack = "mississippi"
needle = "a"
print(imple_str(haystack,needle))
    