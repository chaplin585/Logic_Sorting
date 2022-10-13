TARGET = Logic-Sorting
PY = python

$(TARGET): src\main.py src\Sorting.py src\Parsingfile.py install
	install
	$(PY) src\main.py
	$(PY) src\Parsingfile.py
	$(PY) src\Sorting.py	

install:
	sudo easy_install pip
	pip install tkinker
src\main.py: 
	$(PY) main.py

src\Parsingfile.py: 
	$(PY) Parsingfile.py

src\Sorting.py: 
	$(PY) Sorting.py

test:  
	$(PY) test/test_main_btns.py
	$(PY) test/test_main_btn2.py
	$(PY) test/test_main_label.py
	  


.PHONY: all test clean

clean:
	rm $(TARGET) *.o

