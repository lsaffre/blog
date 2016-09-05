s = open('ilovefs-ascii.txt', 'rt').read()

s2 = ''
for c in s:
    if c == '0':
        s2 += '<b><font color="blue">0</font></b>'
    elif c == '\n':
        s2 += "<br>\n"
    else:
        s2 += c

s2 = '<html><font face="Courier">\n%s\n</font></html>' % s2

open('ilovefs-ascii.html', 'wt').write(s2)
