#! /bin/bash

output_file=execution_times.txt 

if [ -e $output_file ]; then
    rm $output_file
fi

for file in `ls -v [0-9]*.py`; do
    problem_num=${file%.*}
    echo $problem_num
    execution_time=`(/usr/bin/time --format="%E" python $file) 2>&1 1>/dev/null`
    echo "$problem_num: $execution_time" >> $output_file
done
