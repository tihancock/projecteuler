#! /bin/bash

date=`date +%d%m%y`
output_file=execution_times_$date.txt 

if [ -e execution_times/$output_file ]; then
    rm execution_times/$output_file
fi

for file in `ls -v [0-9]*.py`; do
    problem_num=${file%.*}
    execution_time=`(/usr/bin/time --format="%E" python $file) 2>&1 1>/dev/null`
    echo "$problem_num: $execution_time" >> execution_times/$output_file
done
