NAME = mtd
PDF = $(NAME).pdf
SRC = $(NAME).tex
BIB = sources.bib
FIGS = $(wildcard fig/*.pdf)
BUILDDIR = build
LATEX = latexmk -pdf -halt-on-error -synctex=1 -output-directory=$(BUILDDIR)

all: $(PDF)

$(PDF): $(SRC) $(BIB) $(FIGS)
	$(LATEX) $(NAME)
	mv $(BUILDDIR)/$(PDF) .

clean:
	rm -rf $(BUILDDIR)
