#!/bin/bash

INFILE=README.md
LINES=$1
PATTERN="[0-9]+"
BRANCH="master"

commit_message="Add daily problem, ()"
line_arr=()
num_arr=()
declare -r CHAR_CON=3
declare -i index_num_long=0

mapfile -t line_arr < <(tail -n $LINES $INFILE)

for i in "${line_arr[@]}"
do
	[[ $i =~ $PATTERN ]] 
	num_arr+=("${BASH_REMATCH[0]}")
done

for i in "${num_arr[@]}"
do
	if [ ${num_arr[-1]} = $i ]
	then
		commit_message="${commit_message:0:(($index_num_long+20))}#$i${commit_message:(($index_num_long+20))}"
	elif [ ${num_arr[0]} = $i ]
	then
		commit_message="${commit_message:0:20}#$i, ${commit_message:20}"
	else
		commit_message="${commit_message:0:(($index_num_long+20))}#$i, ${commit_message:(($index_num_long+20))}"
	fi
	((index_num_long+=(${#i} + $CHAR_CON)))
done

echo "commit -m: ${commit_message}"

git add .
git commit -m "$commit_message"
git push origin $BRANCH


