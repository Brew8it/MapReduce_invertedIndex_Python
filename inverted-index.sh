export map_input_start=0
for f in file1.txt file2.txt; do
    export map_input_file=$f
    cat $f | python mapper.py
done | sort -k 1,1 | python reducer.py