# Purpose
Python implement anagram in common as practice.  

# References
## Data Structures - Anagram Problem Solution-3MwRGPPB4tw
https://youtu.be/3MwRGPPB4tw

# Results
I watched the problem statement.
Then coded answer.

## Problem
Given two strings a and b, each contains only ascii lowercase a-z.
Remove the minumum number of letters from each so that the remaining letters are anagrams.
How many letters must you remove?

Assume for purposes of this puzzle, an "anagram" does not have to be a valid English word.
It just represents a sequence of letters.


## Appendix Anaconda create and activate virtual environment

### create virtual environment
In project root directory  

If using Anaconda, python3 -m venv ./venv may throw error  

Error: Command '['/Users/stevebaker/Documents/projects/pythonProjects/anagram_in_common/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  
http://stackoverflow.com/questions/41857088/new-python-3-6-venv-giving-error-on-macos  
http://stackoverflow.com/questions/41412876/how-do-you-activate-an-anaconda-environment-in-the-terminal-with-mac-os-x?noredirect=1&lq=1  

So instead use anaconda command  

    conda create -n anagram_in_common python=3.6

### activate virtual environment
cd project root directory  
activate virtual environment

#### macOS, linux

    source activate anagram_in_common

(anagram_in_common) should show at beginning of command prompt  

    source deactivate anagram_in_common

