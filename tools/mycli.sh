#!/bin/sh

### Reusable shell script to access MySQL database.
### It collects information required to access the DB from settings.py in your project.
### Additional dependencies other than Python and Django:
###   - GNU Awk (gawk)
###   - mycli(MySQL client written by Python - https://www.mycli.net/) required

hostScript=${0##*/}

[ -x manage.py ] || {
  printf "[ %s ] \e[1;31m ERROR \e[0m Can't find manage.py\n" "${hostScript}"
  exit 1
}

prjname=$( gawk '/DJANGO_SETTINGS_MODULE/ { match($0, /"([[:alnum:]_]*)\.settings/, c); print c[1]; }' manage.py )

db=$( python -c "from $prjname import settings; print(settings.DATABASES['default']['NAME'])" )
[ $? = 0 ] || {
  printf "[ %s ] \e[1;31m ERROR \e[0m Can't acquire db name\n" "${hostScript}"
  exit 1
}

user=$( python -c "from $prjname import settings; print(settings.DATABASES['default']['USER'])" )
[ $? = 0 ] || {
  printf "[ %s ] \e[1;31m ERROR \e[0m Can't acquire user name\n" "${hostScript}"
  exit 1
}

pw=$( python -c "from $prjname import settings; print(settings.DATABASES['default']['PASSWORD'])" )
[ $? = 0 ] || {
  printf "[ %s ] \e[1;31m ERROR \e[0m Can't acquire password\n" "${hostScript}"
  exit 1
}

mycli -h localhost -u$user -p$pw "$db"

