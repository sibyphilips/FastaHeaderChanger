#!/usr/bin/python
import re
import shutil
import string
import os

print( "please enter the file name below")
#Raw_input is used to collect data from the user
file_in = input("> ")
format_format = input('which format do you want the output file to be in, 1) gb_G_sp, 2) gi_G_sp, 3) G_sp, 4) 1 or 2 to 3, new) new_format_to_Gb_sp, enter, 1,2, 3, 4 or new: ')
#print( "\n \n your request is to make a file with '%s' format" %(str(format_format)))

#now lets define one function each to change the headers into three different formats    
    
def change_ncbi_to_gb(fl):
    #lets start the loop here for gb format
    i=0
    with open(file_in, 'r') as input_file, open('Fasta_name_changed_gb.fasta', 'w') as output_file:
        for line in input_file:
            if '>' in line:
                #print line
                one=line.split('|')
                two=line.split(' ')
                #print one[1]
                #print one[3]
                #print two[1]
                #print two[2]
                us='_'
                fast='>'
                gb=fast+one[3]+us+two[1]+us+two[2]
                output_file.write(str(gb)) #we are replacing the new file's line with our GB if we need gi nos replace gi here
                output_file.write('\n')
            else:
                output_file.write(line)
            i=i+1
        output_file.close()

def change_ncbi_to_gi(fl):
    #lets start the loop here for gb format
    i=0
    with open(file_in, 'r') as input_file, open('Fasta_name_changed_gi.fasta', 'w') as output_file2:
        for line in input_file:
            if '>' in line:
                #print line
                one=line.split('|')
                two=line.split(' ')
                #print one[1]
                #print one[3]
                #print two[1]
                #print two[2]
                us='_'
                fast='>'
                gi=fast+one[1]+us+two[1]+us+two[2]    
                output_file2.write(str(gi))
                output_file2.write('\n')
            else:
                output_file2.write(line)
            i=i+1
        output_file2.close()
    
def change_ncbi_to_genus_species(fl):
    #lets start the loop here for gb format
    i=0
    with open(file_in, 'r') as input_file, open('Fasta_name_changed_gen_spp.fasta', 'w') as output_file1:
        for line in input_file:
            if '>' in line:
                #print line
                one=line.split('|')
                two=line.split(' ')
                #print one[1]
                #print one[3]
                #print two[1]
                #print two[2]
                us='_'
                fast='>'
                spN=fast+two[1]+us+two[2]    
                output_file1.write(str(spN))
                output_file1.write('\n')
            else:
                output_file1.write(line)
            i=i+1
        output_file1.close()
        
def change_1_2_to_G_SP(fl):
    #lets start the loop here for gb format
    i=0
    with open(file_in, 'r') as input_file, open('Fasta_name_changed_gen_spp.fasta', 'w') as output_file1:
        for line in input_file:
            if '>' in line:
                #print line
                one=line.split('_')
                #two=line.split(' ')
                #print one[1]
                #print one[3]
                #print two[1]
                #print two[2]
                us='_'
                fast='>'
                spN=fast+one[1]+us+one[2]    
                output_file1.write(str(spN))
                output_file1.write('\n')
            else:
                output_file1.write(line)
            i=i+1
        output_file1.close()

def change_ncbi_new_to_gb(fl):
    #lets start the loop here for gb format
    i=0
    with open(file_in, 'r') as input_file, open('Fasta_name_changed_gb.fasta', 'w') as output_file:
        for line in input_file:
            if '>' in line:
                #print line
                #one=line.split('|')
                two=line.split(' ')
                #print one[1]
                #print one[3]
                #print two[1]
                #print two[2]
                us='_'
                fast='>'
                gb=two[0]+us+two[1]+us+two[2]
                output_file.write(str(gb)) #we are replacing the new file's line with our GB if we need gi nos replace gi here
                output_file.write('\n')
            else:
                output_file.write(line)
            i=i+1
        output_file.close()
 
#change_ncbi_to_gb(file_in)
if format_format == "1":
    #print str(format_format)
    change_ncbi_to_gb(file_in)
elif format_format == "2":
    #print str(format_format)
    change_ncbi_to_gi(file_in)
elif format_format == "4":
    change_1_2_to_G_SP(file_in)
#new_format_to_GB_SP
elif format_format == "new":
    change_ncbi_new_to_gb(file_in)
else:
    #print str(format_format)
    change_ncbi_to_genus_species(file_in)

