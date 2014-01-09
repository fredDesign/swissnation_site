
.PHONY: help install clean delpyc assets scss

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc 
	rm -Rf bin include eggs lib parts django-apps-src develop-eggs .installed.cfg compass/.sass-cache project/webapp_statics/.webassets-cache

assets:
	django-instance collectstatic --pythonpath=project/ --noinput
	django-instance assets build --pythonpath=project/

scss:
	compass compile -c compass/config.rb compass/

install:
	pip install --upgrade setuptools
	mkdir -p eggs
	python bootstrap.py
	buildout -v
	django-instance syncdb --all --settings=project.settings
	django-instance migrate --fake --settings=project.settings
