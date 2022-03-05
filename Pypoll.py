from distutils import text_file
import os
import csv


#cwd = os.getcwd() 

#files = os.listdir(cwd)

#print(files, "here")


#Assign a variable to path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")


#Writing text to another file using the open function
with  open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n///////////////////////////////\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# Open the election results and read the file.
with open(file_to_load) as election_data:

#Read and analyze data here
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)




