ray/
├── dimension_3/
│   ├── axis/
│   │   ├── Camera.py
|   |   ...
│   │ 
│   │── test_axis.py  
│ 
└── triplet
    ├── mymath 
        ├── Triplet.py    

suppose we have this arborescence, 
how to import some class of Triplet.py from Camera.py

export PYTHONPATH=$PYTHONPATH:/home/user/projects/my_module

# ce ne sera valable que pour le terminal en cours #
export PYTHONPATH=$PYTHONPATH:/path/to/project

# mine: #
export PYTHONPATH=$PYTHONPATH:/home/ghost/L3/s6/TE_techEmergente/ray
echo $PYTHONPATH


# from parent.child.module import some_function