#Given a fasta and a metadata csv, it checks if all the records ID from the fasta are included in the metadata. It prints the missing ones.
#python 1.1checkIDrec.py H1_fortree.csv 2018_pdmH1_Ref.fasta

import os, sys

listIDrec=[]
with open (sys.argv[1], 'r') as fi:
	for line in fi:
		listIDrec.append(line.split(',')[0])

count=0
with open (sys.argv[2], 'r') as fi2:
	for line in fi2:
		if line[0]==">":
			if line[1:-1].split("|")[0] not in listIDrec:
				print("No metadata available for sample "+line[1:-1])
				count+=1

if count==0:
	print("All samples are included in the metadafa sheet")
