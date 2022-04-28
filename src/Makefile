IPT =python3
ARCHIVE =xkalen07_xkubin27_xstrei06_xmashl00

.PHONY: all run test profile pack clean clear help doc
.SILENT: help clean
all: help
	chmod +x install
	chmod +x uninstall
	
run: calcgui.py
	$(IPT) calcgui.py

test: test_calc.py
	$(IPT) test_calc.py 

profile: profiling.py
	$(IPT) profiling.py < ../profiling/"vstup 1000.txt"
	

doc: calc.py
	pydoc -w calc

help:
	echo "run installation script from the install directory using ./install"
	echo "uninstall the application using the uninstall script in the same directory using ./uninstall"

pack: all doc packfiles 
packfiles:
	cd ../ && mkdir -p $(ARCHIVE) && cd $(ARCHIVE) && mkdir -p doc install repo
	mv *.html ../$(ARCHIVE)/doc/
	cp ../dokumentace.pdf ../$(ARCHIVE)/doc
	cp install uninstall ../$(ARCHIVE)/install/ 
	cd ../ && cp -r .git .gitignore $(ARCHIVE)/repo
	cd ../ && cp -R `ls | grep -v $(ARCHIVE)` $(ARCHIVE)/repo/ 
	cd ../$(ARCHIVE)/repo/src/ && make clean
	cd ../ && zip -r ../$(ARCHIVE) $(ARCHIVE)
	cd ../ && rm -rf $(ARCHIVE)
	
clear: clean
clean:
	rm -rf __pycache__ __init__.py *.html *.prof
	
