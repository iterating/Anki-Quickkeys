#!/bin/bash

if [ $# -eq 0 ]
  then
    # No arguments
    ./ankikeys
else
	./caret_status.sh &
	./ankikeys
fi
