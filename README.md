# JSONComparator
Utility function to compare two different JSON response

# To Execute the tests from command line
Execute the command pytest -v -s inside JSONComparator directory

# Class Compare
It has a method json_comparator which will read the files passed to it and makes GET call on the requests of those files and call the comparator method

# comparator method 
This method compares the json responses of two different URLs, irrespective of its type dict or list reccursively 
and returns TRUE or False

# RequestURLFiles
This directory contains all the files with the API endpoints which has to be compared

# src, test
These directories contains the source code and test code of our utility function
