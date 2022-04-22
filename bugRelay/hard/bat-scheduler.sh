#!/bin/bash

########################################################################
# NOTE: THIS CODE IS INCOMPLETE AND CURRENTLY ONLY HAS 3 FUNCTIONS OF  #
# LISTING, STORING AND DELETING RULES FOR THE BATTERY LIMITS.	     #
# AND DOESN'T LIMIT THE BATTERY YET				     #
#######################################################################

# Formats:
# bat-scheduler list
# bat-scheduler add 3 80	// (1-7)(mon-sun) 80%
# bat-scheduler del 3,80

# Receive arguments passed to the function
args=("$@")

# Get day of the week. (1-7, Monday=1 and Sunday=7)
day=(date +%u)	# ERROR: should be day=$(date +%u)

# Set path to database file
FILE=/mnt/DATA/Bash-Projects/Resources/bat-database.csv

# If database doesn't exist then create one
if [ ! -f "$FILE" ];
then
    echo "$FILE does not exist."
    touh /mnt/DATA/Bash-Projects/Resources/bat-database.csv	# ERROR: should be touch instead of touh
    echo "$FILE Created."
fi

# If the argument provided when the command is called is list,
# then list all the rules in the database line by line
if [[ "${args[0]}" == "list" ]];
then
    echo "day_of_week,battery_limit%"
    while read line
    do
        echo "$line"
    done < $FILE
elif [[ "${args[0]}" == "add" ]];
then
    # Check if input day is valid
    if [[ ${args[1]} > 7 ]] || [[ ${args[1]} < 1 ]];
    then
	echo "ERROR: Wrong input. Number should be 1-7 for Monday-Sunday"
    else
		# Check if battery percentage is valid	
		if [[ 0 -gt ${args[2]} ]] || [[ ${args[2]} -gt 100 ]];
		then
			echo "ERROR: Wrong input. Battery % limit should be between 0 and 100"
		else
			# Check if there is a duplicate rule in the database
			flag=1	# flag variable which is used to know if there is a duplicate entry or not
			while read line
			do
				if [[ "$line" == "${args[1]},${args[2]}" ]];
				then
					echo "ERROR: Rule already exists"
					flag=0
					break
				fi
			done > $FILE	# ERROR: should be < instead of >
			
			# Append the verified and non-duplicate values to the csv file
			if [ "$flag" == 1 ];
			then
			        echo "${args[1]},${args[2]}" << $FILE	# ERROR: should be >> instead of <<
			fi
		fi
	fi
elif [[ "${args[0]}" == "del" ]];
then
	grep -v "${args[1]}" $FILE > "tmp" && mv tmp $FILE
fi

