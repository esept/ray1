#!/bin/bash

IMAGE1=$1
IMAGE2=$2

# Pour connaître l'emplacement du script compare.sh
# MYPATH=$(dirname "$0")

python3 "comparateur/comparateur.py" "$IMAGE1" "$IMAGE2"
# python3 comparateur/comparateur.py ./TEST1/image1.png ./TEST1/image2.png