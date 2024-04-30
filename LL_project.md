LL_project

# Working notes 

Writing
- What do we need to  do/how change?
- Read current version see what comes to mind

- Need to condense down introduction
- What does a good example look like?
- Somnotate paper probably a good examplea
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824458/


- Question
- What evidence of constant light effects on sleep currently?
    - new stuff since 2019 wrote
- Want to read the Borbely effect of light on sleep paper
- Duration, distribution, architecture, NREM/REM, episode duration, 
intensity
- 

- https://pubmed.ncbi.nlm.nih.gov/31720718/
    - agomelatin on constant sleep 

- https://www.sciencedirect.com/science/article/pii/S0028390821002616?dgcid=api_sd_search-api-endpoint
    - agomelatin on constant sleep
    - question what is effect of constant sleep? k

- https://www.sciencedirect.com/science/article/abs/pii/S0091305718301515
    - Appears to be source of constant light effect in 
    tchekalarova studies
    - seem more interested in light at night rather than LL?
    - Does not measure the effects on sleep/circadian, just on 
    behavioural tests and melatonin/corticosterone
    - In rats LL eliminates rhythmicity in melatonin and corticosterone
    - Elevated corticosterone and supressed melatonin
    - what about pulsatile corticosterone secretion?







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
        - New measures for the sleep
        - New data (Sleep score extra days)
        - Simulate new data to test analysis plan?


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



