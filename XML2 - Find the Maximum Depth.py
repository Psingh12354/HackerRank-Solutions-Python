import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if (maxdepth < level):
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
