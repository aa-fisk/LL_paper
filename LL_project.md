LL_project

# Working notes 

Writing
- What do we need to  do/how change?
- Read current version see what comes to mind

- Need to condense down introduction
- What does a good example look like?
- Somnotate paper probably a good examplea
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824458/
- probably need to know more about results/discussion
before writing more intro

- Question
- what am I arguing in this paper?

Constant light increases sleep during subjective dark, with reduced
power leading to normally maintained homeostasis

Constant light causes sleep during first few hours of subjective dark
- Cannot be homeostatic as no change
- Can't be circadian as no change?
- must be direct light induced 

What does this sleep look like?
- Homeostatic reduced power but maintained SWE
- circadian ??? abnormal for time of day
- direct 

What do we care about what the sleep looks like? 
- episode duration?
- power spectra - delta power specifically?
- Other ideas - read something like Mathildes paper

What do we know about directly light induced sleep?
- T1/7 etc. 
- depends on circadian phase? 
- What does power, episode duration
- Direct effects previously described as masking circadian effects
- Hubbard 2021
- Does not require melanopsin Tsai 2009, but is stopped by loss 
of iPRGCs 


- important point - not arrhythmic due to low light intensity
100-120 lux super low LED light
Given this Ohta paper shows not desynchronised therefore what
are we even doing?


argh why do we care?
How does this fit with what we know about sleep regulation?

Homeostasis causes increased sleep need and intensity after 
prolonged waking. 
We see normal SWE with increased sleep therefore this cannot
be due to increased homeostatic pressure.

Circadian?
Given see changes immediately, not enough time to cause 
major change to circadian signal, should be robust to 
short term changes as that's the entire point?
How long does it take to cause disruption in the ohta paper?
Housed under LL 3-5 months, arrythmic after 120 days!!!







# Overall plan 
- 3 separate projects
    - Turn what I have into a basic thing that can be published as is
        - DONE 2024-04-30    
    - Improve what I have so tidied up enough to publish code/data 
    behind paper
        - Reformat?
            - Try putting into RMarkdown and see how to get that to 
            convert to word more easily
            - Tidy up or at least look over data dirs structure?
        - Version control
    - Extend the paper
        - Update code?
            - Go through code and see if can tidy up 
                - Preprocessing 
                - Stats
                - Figures 
        - Make a clear workflow from primary data 
        - New measures for the sleer
        - New data (Sleep score extra days)
            - Somnotate
        - Simulate new data to test analysis plan?

# TODO
- Make file
- make convert to/from word
- make run all scripts to generate figures?
- Remove underscores from variable names


## Scripts 

### 01 tex to md
pandoc 01_chapter3.tex -o 02_ch3.md --bibliography=thesis_references.bib --citeproc -M link-citations=True

### 02 md to word 
pandoc 02_ch3.md -o 03_ch3.docx --bibliography=thesis_references.bib --citeproc -M link-citations=True --reference-doc tex_word_custom_reference.docx

### 03 word to md
pandoc 03_ch3.docx -o 04_ch3.md --bibliography=thesis_references.bib --citeproc -M link-citations=True --reference-doc tex_word_custom_reference.docx


###Create environment
CONDA_SUBDIR=osx-64 conda env create -f environment.yml

### Run preprocessing
python 02_analysis/01_preprocessing/01_clean_fft.py
python 02_analysis/01_preprocessing/02_stage_file.py





## Current

## Questions/Ideas
- Ideas graveyard?
    - Rewrite what currently have
        - Increase introduction so have enough info for published paper
    - More data?    
        - Who would let us use sleep score?
        - Joel Raymond at USYD? 
        https://www.sydney.edu.au/science/about/our-people/research-students/joel-raymond-543.html
- What about citations in markdown/Rmarkdown?
- Cumulative plots
    - Bool value ambiguous 
    - Is "processed" in data_list
        - but data list is a dataframe?
        - what is expected?
        - Why are we getting something diff?
        - what does it mean by "Processed" in data_list 
            - Checking if it has a dirname instead of a list of dataframes
        - so, ambiguous because not sure if processed, obviously not? 
        - change in core python behaviour - don't think so?
        - okay so options, change actiPy - eurgh big pain
        - Enough for now - come back to problem later, brain too hurt
Write pipeline 
    - best version in deprec implement at the moment 
What about citations in markdown/Rmarkdown?






# Extra stuff to keep but not current use

## Ideas as things go along/notes
- Write dimensions/structure of data in notes? 
- Write workflow in notes
- Get makefile working to create all figures (need with RMarkdown
integration?)
- Solves problem of short/long term?
    - make all and then only use the short term ones in RMarkdown?
    - How to put together in fig panels? 
        - still need powerpoint for that?
        - or keep workflow of create individuals then combine 
        - separate figures into paper and rest into 
        general project? 
- include blurb in code of why looking at?


# Reference Info
Writing files taken from 
/Users/angusfisk/Dropbox/01_PhD_things/02_Projects/06_thesis/03_lleeg
Analysis files taken from 
/Users/angusfisk/Documents/01_personal_files/01_work/01_dphil/01_projects/01_thesisdata



