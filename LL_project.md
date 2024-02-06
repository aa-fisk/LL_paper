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

## Next steps 
- Version control writing and code (separate repos?) - done 2023-11-22
- Get tex file to compile - done 2023-11-22
- Produce figures using current code 

## Scripts to use

###Convert to docx 
    pandoc 01_chapter3.tex -o 02_chapter3.docx --reference-doc tex_word_custom_reference.docx --bibliography=thesis_references.bib --citeproc --link-citations=True
###Convert back to md
    pandoc 02_chapter3.docx -o 03_ch3.md --citeproc --bibliography=thesis_references.bib --link-citations=True
###Create environment
CONDA_SUBDIR=osx-64 conda env create -f environment.yml

### Run preprocessing
python 02_analysis/01_preprocessing/01_clean_fft.py
python 02_analysis/01_preprocessing/02_stage_file.py

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




# Working notes 

## Questions/Ideas
- Ideas graveyard?
    - Rewrite what currently have
        - Increase introduction so have enough info for published paper
    - More data?    
        - Who would let us use sleep score?
        - Joel Raymond at USYD? 
        https://www.sydney.edu.au/science/about/our-people/research-students/joel-raymond-543.html
- What about citations in markdown/Rmarkdown?



## Current

Write pipeline 
    - best version in deprec implement at the moment 

### Tex conversion 
- get tex file compiling to PDF as well
    - okay converting back to tex doesn't work very well 
- Add in and rename what necessary to convert to/from word and pdf  
    - need the bibliography and the reference doc and the code
- get code working to create all figures


## Code produce
Current problem - code_check
- Create environment file
- Run preprocessing
- Run figures 


- All Preprocessing done
- Create figures/other outputs 
- Individual animals graphs ?
- Then figures
- 02_plot_delta_hypnograms.py - working
- Will we run into problems if running from parent dir? 
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
- Figures instead
    - Fig 1 updated and working
    - Fig 2 create_df_for_single_band requiring sum keyword 
        - In local dir but not public one
        - Options
            - Link hardcoded path to new version
            - Upload to new github account and set that to new env path
                - Problem if new stuff has conflicts, but always a risk

- Update on new github accoun
    - Made new account
    - Set URL as origin
    - Got all working, now to update environment file        
        - working for sleepPy
    - now for actiPy
        - Then update environment file
        - Then get back to running fig 2
