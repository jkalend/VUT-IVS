IPT = python3
ARCHIVE =xlogin# add archive name

.PHONY: all run test profile pack clean clear help doc
.SILENT: help clean
all: help
	chmod +x install
	chmod +x uninstall
	
run: calcgui.py
	$(IPT) calcgui.py

test: test_calc.py
	$(IPT) test_calc.py 

#TODO -- fix profiling target 
profile: profiling.py
	$(IPT) profiling.py
	

doc: calc.py
	pydoc -w calc

help:
	echo "run installation script from the install directory using ./install"
	echo "uninstall the application using the uninstall script in the same directory using ./uninstall"

#TODO -- generate doc and run profiling beforehand
pack: packfiles 
packfiles:
	cd ../ && mkdir -p $(ARCHIVE) && cd $(ARCHIVE) && mkdir -p doc install repo
	mv *.html ../$(ARCHIVE)/doc/ #--assuming all generated documentation is .html (i have no idea)
	cp install uninstall ../$(ARCHIVE)/install/ 
	cd ../ && cp -r .git .gitignore $(ARCHIVE)/repo
	cd ../ && cp -R `ls | grep -v $(ARCHIVE)` $(ARCHIVE)/repo/ 
	cd ../$(ARCHIVE) && zip -r ../$(ARCHIVE) doc repo install
	cd ../ && rm -rf $(ARCHIVE)
#	cd ../ && rm -rf !$(ARCHIVE).zip -- not sure if this should remove everything else from the parent folder or not
	
clear: clean
clean:
	rm -rf __pycache__ __init__.py calc.html
	
