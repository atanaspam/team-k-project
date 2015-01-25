# Source: http://ahoj.io/how-to-convert-mysql-to-sqlite
# AND     http://www.jbip.net/content/how-convert-mysql-sqlite
# Usage:
# To dump the Database:
#   mysqldump -u root -p --compatible=ansi --skip-opt mydb > dumpfile 
#      ^           ^                  ^                 ^       ^       
#   command   mysql username      arguments      schema name    output file name
# To convert it:
#   mysql-to-sqlite.sh dumpfile
#
# - Atanas


#!/bin/bash
if [ "x$1" == "x" ]; then
  echo "Usage: $0 <dumpname>"
  exit
fi

cat $1 |
grep -v ' KEY "' |
grep -v ' UNIQUE KEY "' |
grep -v ' PRIMARY KEY ' |
sed '/^SET/d' |
sed 's/ unsigned / /g' |
sed 's/ auto_increment/ primary key autoincrement/g' |
sed 's/ smallint([0-9]*) / integer /g' |
sed 's/ tinyint([0-9]*) / integer /g' |
sed 's/ int([0-9]*) / integer /g' |
sed 's/ character set [^ ]* / /g' |
sed 's/ enum([^)]*) / varchar(255) /g' |
sed 's/ on update [^,]*//g' |
sed 's/\\r\\n/\\n/g' |
sed 's/\\"/"/g' |
sed 's/ "id" bigint(20) NOT NULL/ "id" integer primary key autoincrement/g' |
perl -e 'local $/;$_=<>;s/,\n\)/\n\)/gs;print "begin;\n";print;print "commit;\n"' |
perl -pe '
if (/^(INSERT.+?)\(/) {
  $a=$1;
  s/\\'\''/'\'\''/g;
  s/\\n/\n/g;
  s/\),\(/\);\n$a\(/g;
}
' > $1.sql
cat $1.sql | sqlite3 $1.db > $1.err
ERRORS=`cat $1.err | wc -l`
if [ $ERRORS == 0 ]; then
  echo "Conversion completed without error. Output file: $1.db"
  rm $1.sql
  rm $1.err
else
  echo "There were errors during conversion.  Please review $1.err and $1.sql for details."
fi