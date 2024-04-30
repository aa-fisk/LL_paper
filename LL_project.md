LL_project



# Overall plan 
- 3 separate projects
    - Turn what I have into a basic thing that can be published as is
        - Get what I have into its own dir 
            - Writing 
            - Data
            - Code
        - Convert to word
        - Reproduce current paper successfully
            - Compile tex file
                - Edit to be standalone not part of bigger file
            - Create figures 
                - Create python environment and run files
                - PPT based ones can leave as is
        -     
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

## steps 
- Version control writing and code (separate repos?) - done 2023-11-22
- Get tex file to compile - done 2023-11-22
- Produce figures using current code - Done 2024-02-07

## Scripts to use


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


# Working notes 



## Current


### Writing

Next step is getting to the point can edit the manuscript!?!?!
- Need to finish up the tex conversion, want in markdown format 
  with citations in it
- So converting to word from tex is working 
    - Including citations 
        - Inline/figures?
- How about from word back to tex
    - Including citations
- Okay what is the problem I'm having
    - How to convert citations from work to markdown in pandoc
    - Have reference .bib file but doesn't want to work?
    - Okay so something to do with the citations extension 
        - https://pandoc.org/chunkedhtml-demo/7.6-other-extensions.html#org-citations
        - How to enable the citations extension?
        - Are the citations in the word fine formatted correctly as citations?
        - Okay this seems to be the problem, renders them fine as 
        bracketed citations but this format not picked up for conversion
        back to markdown, hmmm
        - how to render citations into docx so they keep @formatting 
    - How about convert from .tex to markdown then back and forth from
    word?



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



