#Extract from substitutions.tsv (treesub output) the subs.csv to build the tree.
#It take branch/string/non_synonymous and compact.

#how to call
#python 3.build_subs.py subsitutions.tsv subs.csv

import os, sys

subsDict={}
with open (sys.argv[1],'r') as f1:
	for line in f1:
		if line.split("\t")[0]=="1":
			print(line)
		if "*" in line:
			if line.split("\t")[0] in subsDict.keys() and ("*" not in subsDict[line.split("\t")[0]]):
				subsDict[line.split("\t")[0]]=subsDict[line.split("\t")[0]][:-1]+','+line.split("\t")[6]+'"'
			elif (line.split("\t")[0] not in subsDict.keys()) or ("*" in subsDict[line.split("\t")[0]]):
				subsDict[line.split("\t")[0]]='"'+line.split("\t")[6]+'"'
		else:
			if line.split("\t")[0] not in subsDict.keys():
				subsDict[line.split("\t")[0]]="*"	

res="node_num,nonsynsubs\n"
for key in sorted(subsDict.iterkeys()):
	res+=key+","+subsDict[key]+"\n"

with open (sys.argv[2],'w') as fo:
	fo.write(res)


# 166	117	TTC	TTT	F	F	F117F
# 166	282	CCC	CCT	P	P	P282P	
# 313	74	AGC	AGT	S	S	S74S	
# 313	97	GAT	AAT	D	N	D97N	*
# 313	138	CAT	CAC	H	H	H138H	
# 313	163	AAA	CAA	K	Q	K163Q	*
# 313	176	CTA	CTG	L	L	L176L	
# 313	256	GCA	ACA	A	T	A256T	*


# 166	*
# 313 "D97N,K163Q,A256T"
