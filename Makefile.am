# version first -- they are parsed LTR and later options depend on automake 1.8
AUTOMAKE_OPTIONS = 1.8 dist-bzip2 no-dist-gzip

SUBDIRS = \
	bin \
	yq

release: dist
	make $(PACKAGE)-$(VERSION).tar.bz2.sha1

# generate md5 sum files
%.sha1: %
	sha1sum $< > $@
