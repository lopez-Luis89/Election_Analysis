from distutils import text_file
import os
import csv
from telnetlib import theNULL


#cwd = os.getcwd() 

#files = os.listdir(cwd)

#print(files, "here")


#Assign a variable to path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")
total_votes = 0
candidate_options = []
candidates_vote = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Writing text to another file using the open function
with  open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n///////////////////////////////\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# Open the election results and read the file.
with open(file_to_load) as election_data:

#Read and analyze data here
    file_reader = csv.reader(election_data)
    #View the first/header row
    header = next(file_reader)
    print(header)

    for row in file_reader:
        #Add  to the total vote count
        total_votes+= 1
        
       # Print the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count.
            candidates_vote[candidate_name] = 0
    
        candidates_vote[candidate_name] += 1
        
            
    for candidate_name in candidates_vote:
                
        votes = candidates_vote[candidate_name]
        vote_percentage = round(float(votes) / float(total_votes) * 100)
        
          

        if (votes > winning_count) and (vote_percentage > winning_percentage ):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

            
            







