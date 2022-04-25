IPT = python3
ARCHIVE =xlogin# add archive name

.PHONY: all run test profile pack clean clear help doc
.SILENT: help clean all
all:
	#chmod +x installer/install
	#echo "chmod +x install/install"
	#chmod +x installer/uninstall
	#echo "chmod +x install/uninstall"
	ln  ./installer/install
	ln  ./installer/uninstall
	#echo "run installation script from the install directory using ./install"
	#echo "uninstall the application using the uninstall script in the same directory using ./uninstall"

run: src/calcgui.py
	$(IPT) src/calcgui.py

test: src/test_calc.py
	$(IPT) src/test_calc.py

#TODO -- fix profiling target 
profile: profiling.py
	$(IPT) profiling.py > profiling/profile.txt
	
# TODO -- add target for generating doc
doc:
#	?????

help:
	echo "run installation script from the install directory using ./install"
	echo "uninstall the application using the uninstall script in the same directory using ./uninstall"

#TODO -- generate doc and run profiling beforehand
pack: packfiles 
packfiles:
	cd ../ && mkdir -p $(ARCHIVE) && cd $(ARCHIVE) && mkdir -p doc install repo
#	mv *.html ../$(ARCHIVE)/doc/ --assuming all generated documentation is .html (i have no idea)
	cp install uninstall ../$(ARCHIVE)/install/ 
	cd ../ && cp -R `ls | grep -v $(ARCHIVE)` $(ARCHIVE)/repo/ 
	cd ../$(ARCHIVE) && zip -r ../$(ARCHIVE) doc repo install
	cd ../ && rm -rf $(ARCHIVE)
#	cd ../ && rm -rf !$(ARCHIVE).zip -- not sure if this should remove everything else from the parent folder or not
	
clear: clean
clean:
	rm install uninstall
	rm -rf __pycache__ __init__.py 
	
