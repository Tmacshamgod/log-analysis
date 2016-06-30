#!/bin/bash 
dd=$(date -v -1d '+%Y-%m-%d')
latest_file=`ssh admin@$1 find $2 -type f -daystart -mtime 1`
for i in $latest_file; do
    scp admin@$1:$i $PWD 
    cat -n $PWD'/'${i##*/} | grep --line-buffered -i -E "err|warn" > $PWD'/tornado/project/statics/files/'$1'.'$dd'.'${i##*/}
    rm $PWD'/'${i##*/}
done
echo Completed.
