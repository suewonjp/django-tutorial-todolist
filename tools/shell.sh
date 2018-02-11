#!/bin/sh

### Shell script to make Django Python shell a little more convenient.
### Inside the shell, you can access the following objects by default without importing them.
###  - settings
###  - apps dictionary ( Python dictionary for your own apps )
###  - models (Todo, Category) 
### See .pythonrc.py for details

hostScript=${0##*/}

[ -x manage.py ] || {
  printf "[ %s ] \e[1;31m ERROR \e[0m Can't find manage.py\n" "${hostScript}"
  exit 1
}

scriptDir=${0%/*}

cd "$scriptDir/.." || exit

PYTHONSTARTUP="$scriptDir/.pythonrc.py" python manage.py shell -i python

