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
candidate_county_names =[]
candidates_vote = {}
candidate_county_votes = {}
winning_candidate = ""
winning_county = ""
winning_count = 0
winning_county_count = 0
winning_percentage = 0
winning_county_percentage = 0

#Writing text to another file using the open function
with  open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("///////////////////////////////\n")
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
        


        #-----------Analyzing by county-------------
        candidate_county = row[1] # Created a list and dictionay for the respective variables
                                  #And kep count for each county and printed results of votes per county

        if candidate_county not in candidate_county_names:
            candidate_county_names.append(candidate_county)
            candidate_county_votes[candidate_county] = 0
        candidate_county_votes[candidate_county] += 1
    #print(candidate_county_votes)  
        #----------Analyzing by county--------------
        #----------Determining Winning County -----
    for candidate_county in candidate_county_votes:
            county_votes = candidate_county_votes[candidate_county]
            county_percentage = round(float(county_votes) / float(total_votes) * 100)

            if (county_votes > winning_county_count) and (county_percentage > winning_county_percentage):
                winning_county_count = county_votes
                winning_county = candidate_county
                winning_county_percentage = county_percentage
            county_result = (f"{candidate_county}: {county_percentage:.1f}% ({county_votes:,})")
            print(county_result)#****Prints out everything****
         # ----------Determining Winning county------  

with open(file_to_save,"w") as txt_file:      
    election_results = (
        f"\n Election Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------{county_result}-----------\n" #*****Only prints out last city*************
        )
    print(election_results,end ="")  
    
    txt_file.write(election_results)  

    candidate_county = row[1] # Created a list and dictionay for the respective variables
                                  #And kep count for each county and printed results of votes per county

            if candidate_county not in candidate_county_names:
                candidate_county_names.append(candidate_county)
                candidate_county_votes[candidate_county] = 0
            candidate_county_votes[candidate_county] += 1
    #print(candidate_county_votes)  
        #----------Analyzing by county--------------
        #----------Determining Winning County -----
    for candidate_county in candidate_county_votes:
            county_votes = candidate_county_votes[candidate_county]
            county_percentage = round(float(county_votes) / float(total_votes) * 100)

            if (county_votes > winning_county_count) and (county_percentage > winning_county_percentage):
                winning_county_count = county_votes
                winning_county = candidate_county
                winning_county_percentage = county_percentage
            county_result = (f"{candidate_county}: {county_percentage:.1f}% ({county_votes:,})")
            print(county_result)#****Prints out everything****
         # ----------Determining Winning county------  


    for candidate_name in candidates_vote:
                    
            votes = candidates_vote[candidate_name]
            vote_percentage = round(float(votes) / float(total_votes) * 100)
            
            if (votes > winning_count) and (vote_percentage > winning_percentage ):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            candidate_result = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_result)
            txt_file.write(candidate_result)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)          
            







