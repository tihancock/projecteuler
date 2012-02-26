#! /bin/bash

date=`date +%d%m%y`
output_file=execution_times_$date.txt 

if [ -e $output_file ]; then
    rm $output_file
fi

for file in `ls -v [0-9]*.py`; do
    problem_num=${file%.*}
    echo "problem $problem_num" >> $output_file
    echo `(/usr/bin/time --format="%E" python $file) >> $output_file 2>&1 1>/dev/null`; 
done
