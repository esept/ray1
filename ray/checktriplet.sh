#!/bin/bash

# Pour connaître l'emplacement du script compare.sh
# MYPATH=$(dirname "$0")

python3 "./math_lib/main_math.py" "$1"
# ex:
# ./checktriplet.sh "P 1 1 1,sub,P 2 2 2"
# ./checktriplet.sh "P 1 1 1,add,P 2 2 2"