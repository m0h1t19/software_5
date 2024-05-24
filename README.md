# software_5

clone the repository using git bash command git clone https://github.com/m0h1t19/software_5
in the same directory save the maps on which you want to run the code as text files.

The file software_5.py , first takes a input of location of the text file which we are going to use as a mars map. It reads the file as a multi-line array and converts it to a 2d array. 
Then it locates the initial position of of our rover using the check function in the first step and in other upcoming steps the check function checks the locations of zeros in the map and check in their adjacent position where the rover can move.
The count_place function counts the number of locations of freedom of the rover an returns an integer value.
