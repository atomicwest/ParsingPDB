# Parsing a Protein Database File

## Example using the bone morphogenic protein (BMP)

BMP promotes bone growth and has applications in
orthopedics and dentistry. The model in this repository
has been taken from the Research Collaboratory for
Structural Bioinformatics, found [here][bmpSite]

Run the Python script in the same directory as the pdb file
to view the different amino acids in the protein
and BMP's ratios of carbon, nitrogen, sulfur,
and oxygen among all amino acids.

    atomicwest:~/workspace/python/ParsePDB (master) $ python parseBMP.py
    Amino Acid      C       N       S       O 
                  ALA     0.03    0.04    0.00    0.04
                  ARG     0.03    0.08    0.00    0.03
                  ASN     0.05    0.10    0.00    0.09
                  ASP     0.05    0.04    0.00    0.12
                  CYS     0.04    0.05    0.78    0.04
                  GLN     0.02    0.03    0.00    0.03
                  GLU     0.05    0.04    0.00    0.11
                  GLY     0.02    0.04    0.00    0.03
                  HIS     0.06    0.11    0.00    0.03
                  ILE     0.05    0.03    0.00    0.03
                  LEU     0.10    0.06    0.00    0.06
                  LYS     0.07    0.08    0.00    0.04
                  MET     0.02    0.01    0.22    0.01
                  PHE     0.05    0.02    0.00    0.02
                  PRO     0.07    0.05    0.00    0.04
                  SER     0.05    0.06    0.00    0.10
                  THR     0.02    0.02    0.00    0.04
                  TRP     0.04    0.03    0.00    0.01
                  TYR     0.08    0.04    0.00    0.06
                  VAL     0.10    0.08    0.00    0.07
          Total:          531     142     9       156
          atomicwest:~/workspace/python/ParsePDB (master) $ 

[bmpSite]:http://www.rcsb.org/pdb/explore.do?structureId=3BMP
