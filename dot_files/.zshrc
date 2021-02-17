echo "sourcing /.dot_files/*"
for file in ${PWD}/.dot_files/*; do
	if [ -e "$file" ] ; then
		. "$file"
	fi
done
echo "all files in ${PWD}/.dot_files/ sourced!"
