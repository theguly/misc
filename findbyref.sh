#!/bin/sh
# Author: guly <MindTheBox>
# License: don't sue me

if [ "$#" -ne 3 ]; then
        echo "usage: $0 startdir reference-date|reference-file minutes"
        echo "./$0 /home \"Dec 14 08:00\" 600"
        echo "./$0 /home /home/guly/user.txt 600"
        exit
fi

dir=${1}
if [ -f $2 ]; then
        ref=`/bin/ls -ld1 $2 |/usr/bin/awk '{printf ("%s %2s %s\n", $6, $7, $8)}'`
else
        ref=$2
fi

mins=$3
format='+%m/%d/%Y %R'

begin=$(/bin/date -d"$ref $mins minute ago" "$format")
end=$(/bin/date -d"$ref $mins minute" "$format")

echo "# ref='$ref'"
echo "# begin='$begin'"
echo "# end='$end'"

/usr/bin/find "$dir" -newermt "$begin" ! -newermt "$end" -ls
