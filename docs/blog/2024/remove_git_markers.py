import sys
from pathlib import Path

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

def main():
    if len(sys.argv) < 2:
        print("You must specify at least one file to repair")
        sys.exit(-1)
    for fn in sys.argv[1:]:
        pth = Path(fn)
        s = pth.read_text()
        s = remove_all(s)
        pth.write_text(s)

if __name__ == "__main__":
    main()
