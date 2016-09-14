#! /usr/bin/python

from __future__ import division
import collections

#open file and read each line, parse each line
pdb = open('3BMP.pdb')

#initialize dictionary to store amino acids and frequencies
amdct = {}

for line in pdb:
    if line[0:4] == 'ATOM':
        #save amino acid
        aacid = line[17:20]
        #print aacid
        element = line[len(line) - 4]
        #print element
        if aacid in amdct:
            #increase count per element
            if element == 'C':
                amdct[aacid][0] += 1
            elif element == 'N':
                amdct[aacid][1] += 1
            elif element == 'S':
                amdct[aacid][2] += 1
            elif element == 'O':
                amdct[aacid][3] += 1
            else:
                print aacid
        else:
            #count element
            #add amino acid to dictionary
            #element format: [C, N, S, O]
            amdct[aacid] = [0,0,0,0]
            if element == 'C':
                amdct[aacid][0] += 1
            elif element == 'N':
                amdct[aacid][1] += 1
            elif element == 'S':
                amdct[aacid][2] += 1
            elif element == 'O':
                amdct[aacid][3] += 1
            else:
                print aacid

#sort dictionary by key, alphabetically 
namdct = collections.OrderedDict(sorted(amdct.items()))

#Initialize total element counts
Ct = 0
Nt = 0
St = 0
Ot = 0

print ('Amino Acid \t' + 'C \t' + 'N \t' + 'S \t' + 'O \t')

#maintain running sum of element totals/number of element atoms in  protein
for key in namdct:

    Ct = Ct + namdct[key][0]
    Nt = Nt + namdct[key][1]
    St = St + namdct[key][2]
    Ot = Ot + namdct[key][3]

#counting number of C,N,S,O atoms that occur in each amino acid 
#compute frequencies for each amino acid
#i.e. how much of the carbon in the entire protein is in each amino acid?
for key in namdct:
    Cc = namdct[key][0]/Ct
    Nc = namdct[key][1]/Nt
    Sc = namdct[key][2]/St
    Oc = namdct[key][3]/Ot
    print ('\t' + key + '\t' + '%.2f' % Cc +'\t' + '%.2f' % Nc + '\t' + '%.2f' % Sc + '\t' + '%.2f' % Oc + '\t')

print ('Total: \t\t' + str(Ct) + '\t' + str(Nt) + '\t' + str(St) + '\t' + str(Ot) + '\t')
