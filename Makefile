SOURCES = talk/lino.rst
THEME = light
# THEME = tango
# THEME = leapmotion
# THEME = ribbon
# THEME = default


.PHONY: all
.SUFFIXES: .rst .html .pdf

.rst.html:
	landslide -i -t $(THEME) -d docs/dl/$*.html $*.rst

.rst.pdf:
	landslide -d $*.pdf $*.rst

default: html

all: html pdf

html: $(SOURCES:.rst=.html)
pdf: $(SOURCES:.rst=.pdf)


