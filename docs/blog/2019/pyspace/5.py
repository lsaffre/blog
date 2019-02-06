import csv

def sort_file(txt, *, insep=',', inend='\n', outsep=None, outend=None):
    if outsep is None:
        outsep = insep
    if outend is None:
        outend = inend
    def goodlines():
        for ln in txt.split(inend):
            ln = ln.strip()
            if len(ln) and ln[0] != "#":
                yield ln
    rows = [outsep.join(row) for row in csv.reader(goodlines(), delimiter=insep)]
    rows.sort()
    return outend.join(rows)

if __name__ == '__main__':
    try:
        sort_file('abc', 'test')   # -> TypeError
    except TypeError:
        pass
    else:
        raise Exception("1")

    s = sort_file("""2,3,d
    1,4,d
    8,2,z
    2,4,x
    2,4,a
    """)
    #print(repr(s))
    assert s == """\
1,4,d
2,3,d
2,4,a
2,4,x
8,2,z"""

    # A string with only one item per row
    # print(sort_file('b\ny\na'))
    assert sort_file('b\ny\na') == 'a\nb\ny'

    # Providing some keyword arguments
    assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'

    # Blank lines and lines starting with '#' should not appear in the result
    assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'

    # Proper sorting and ignore blank lines at the end
    assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'


