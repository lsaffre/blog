from pathlib import Path
pth = Path("django.po")
s = pth.read_text()
mark_start = "<<<<<<< HEAD\n"
mark_middle = "=======\n"
mark_end = ">>>>>>> upstream/master\n"

def remove_upstream(s):
    chunks1 = s.split(mark_start, 1)
    if len(chunks1) != 2:
        return s
    s1 = chunks1[0]
    chunks2 = chunks1[1].split(mark_middle, 1)
    if len(chunks2) != 2:
        return s
    chunks3 = chunks2[1].split(mark_end, 1)
    if len(chunks3) != 2:
        return s
    return chunks1[0] + chunks3[0] + chunks3[1]

def remove_all(s):
    while True:
        s2 = remove_upstream(s)
        if s2 == s:
            return s
        s = s2

pth.write_text(remove_all(s))
