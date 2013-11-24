#! /bin/bash

output_file=solutions.txt 

if [ -e $output_file ]; then
    rm $output_file
fi

for file in `ls -v [0-9]*.py`; do
    problem_num=${file%.*}
    echo $problem_num
    solution=`python $file`
    echo "$problem_num: $solution" >> $output_file
done

difference=`diff master_solutions.txt $output_file`

if [ difference=="" ]; then
    echo "All solutions correct!"
else
    echo "The following solution attempts are incorrect:"
    echo diff
fi