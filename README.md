# RevPalMutFinder
DESCRIPTION:
A tool for locating sites in DNA sequences that can be mutated to introduce restriction endonuclease recognition sites into HDR edited DNA. Helpful for designing CRISPR/Cas9 HDR templates.

I have no idea idea how to install it! Hopefully someone helps me out soon.

EXAMPLE USAGE:
  $ python revPalMutFinder.py
  # you will be prompted for the following user inputs:
  # File name (eg. mySequence.txt)
  # File must be in contained folder
  # RE window size (eg. 6 for 6-cutter enzymes like EcoRI)
  # Whether your sequence should be analyzed for translation (if yes: ORF; if no: UTR)
  # If you indicated translation, reading frame (0, 1, or 2)
  Identify file: mySequence.txt
  Please enter an even-number RE recognition length: 6
  Does cut occur in gene? Enter 'UTR' or 'ORF': ORF
  Please enter a valid reading frame (0, 1, or 2): 
  
OUTPUT:
  If UTR is selected, output will yield every possible reverse palindrome.
  Each result is a list containing the location within the query, the original sequence, and the altered sequence.
    [i, WT, -->, Mut]
  Each potential palindrome exists as a pair, since a change is possible at either location.
  For example CTCGGG will return both CCCGGG and CTCGAG.
    This example is listed as follows:
      [1, CTCGGG, ---->, CCCGGG]
      [4, CTCGGG, ---->, CTCGAG]
  
  If ORF is selected, output will first list translations of each possible reverse palindrome.
    If a potential palindrome is found at location 3, the output would be as follows:
      i =  3
      ['D', 'F', 'K', 'K']  = wtTrans
      ['D', 'I', 'K', 'K']  = mutTrans0
      ['E', 'F', 'K', 'K']  = mutTrans1
    Since this example shows changes to translation in both alterations, it is rejected.
    Secondary output will display successful silent mutations that yield palindromic RE recognition sites.
    For example, a potential palindrome that is found at location 21 yields the following primary output:
      i =  21
      ['G', 'A', 'F', 'Y']  = wtTrans
      ['G', 'T', 'F', 'Y']  = mutTrans0
      ['G', 'A', 'F', 'Y']  = mutTrans1
    Since wtTrans is the same as mutTrans1, this is a successful silent mutation.
    The alteration that yields mutTrans1 will be listed in secondary output.
      [21, GGTGCC, ---->, GGCGCC]
    This location can be scored based upon proximity to CRISPR-guided cut.
    
VERSIONS:
  0.0.1: unreleased, not optimized

LICENSE AND AUTHOR INFO:
  Written by Bradley Benjamin (BB) with help from Michael J. Borys (MJB).
  Developed as part of BB's Master's Thesis at the Icahn School of Medicine at Mount Sinai (ISMMS).
  Copyright 2016 BB and ISMMS
  
  bradbenjamin526@gmail.com
    
  
