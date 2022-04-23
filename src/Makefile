IPT = python3
ARCHIVE =xlogin# add archive name

.PHONY: all run test profile pack clean clear help doc
.SILENT: help clean
all:
	chmod +x install/install
	chmod +x install/uninstall
	
run: calcgui.py
	$(IPT) calcgui.py

test: test_calc.py
	$(IPT) test_calc.py 

profile: profiling.py
	$(IPT) profiling.py > ../profiling/profile.txt

doc:
#	?????

help:
	echo "run installation script from the install directory using ./install"
	echo "uninstall the application using the uninstall script in the same directory using ./uninstall"

#generate doc and run profiling beforehand
pack: packfiles
#assuming all generated documentation is .html (i have no idea)
packfiles:
	cd ../ && mkdir -p $(ARCHIVE) && cd $(ARCHIVE) && mkdir -p doc install repo
#	mv *.html ../$(ARCHIVE)/doc/ 
	cp install/* ../$(ARCHIVE)/install/ 
	cd ../ && cp -R `ls | grep -v $(ARCHIVE)` $(ARCHIVE)/repo/ 
	cd ../$(ARCHIVE) && zip -r ../$(ARCHIVE) doc repo install
	cd ../ && rm -rf $(ARCHIVE)
#	cd ../ && rm -rf !$(ARCHIVE).zip -- not sure if this should remove everything else from the parent folder or not
	
clear: clean
clean:
	rm -rf __pycache__ __init__.py 
	