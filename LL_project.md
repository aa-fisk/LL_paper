LL_project


# Aims
- Publish LL paper
## steps
- update writing
- Feedback vlad/stuart
- sleep score extra days (somnotate)
- Analyse data
- submit for publication




# Working notes 

Okay writing feels a bit hard at the moment
Why don't we start seeing if we can get somnotate to work?

- Raw data on backup hard drives
    - On PC
    - TODO reformat hard drives and update backups 
- Install somnotate
- Train classifier
    - What do we need to do this? 
    - Need annotations in visbrain format
        - Currently in our FFT file format
        - TODO convert to visbrain format
            - conversion script in somnotate already 
    - CSV file with list of trained dataset filepaths 
- Run classifier on new data 

- Steps
- Install somnotate
- convert from FFT to visbrain
- Create spreadsheet (from example in data dir)
- train
- run


- Installing
    - Pomegranate 0.14.4 not available on conda (not on website either?)
        - Changed to 0.14.8
    - osx/arm problem 
        - need to specify as a intel env so
        -  CONDA_SUBDIR=osx-64 conda create --no-default-packages --name somnotate_env
    - DONE!!    

- Convert FFT to visbrain
    - What is our test file?
        - LL1-EEG-EMG-180409.edf
        - don't have the 09 FFT file, just use the 10 instead
    - What arguments is it expecting? 
        - spreadsheet file path 
        - okay so next step is to create a spreadsheet
    - Created spreadsheet with correct file names (except 9/10 mix up)
    - now, how to run?
        - In somnotate dir can just run in terminal
            - python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/00_convert_sleepsign_files.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv 
            - Okay getting got 2 columns instead of 3 problem, 
            - due to using csv as delimiter, added to code now fine 

- preprocess training data 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

- test on training data 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/02_test_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

- train model
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/03_train_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

- preprocess unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

- apply to unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/04_run_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

- manually check intervals
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/05_manual_refinement.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

- hahahahaha! It works!!!!! It all worked!!!

- get more data from more mice and update 

- Okay problem, do not have .edf files for all animals?!?!?!? 
Not the end of the world, do have raw data and matlab scripts
Neurotraces right to turn into edf file? 
- can use pc to do that right?
- Okay so neurotracers can do it 
    - Have to install SikuliX script to run but all on https://github.com/A-Fisk/VVlab_Scripts/ so doable
- also can do with EDF viewer, better supported? 
- Ascii2EDF can do via command line
    - Need to figure out how to run it in loop
    - how to write bash script? 
        - what do we want it to do?
        - get list of all files in dir 
        - run ascii convert on each text file 
    - Create template file 
    - current having issue compiling c script
    - need libxml2 but need to update homebrew first, large file 
    - okay repeatedly failing
    - no idea why? - easy, just had to use makefile!
    - okay got C working, but having trouble getting to run in script, 
    - lets try instead as just running on a single file 
    - okay progress, want from EDF browser, see if can use to make the
    template
    - Aha! made from browser and it's working! Don't know 
    what the difference is !
    



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
- fine statement but basically only asking the question of what does
constant light do? 

- What question am I asking? 
- what happens to sleep when we disrupt the circadian system?
- circadian regulates sleep timing
- constant light disrupts locomotor activity and circadian system
- what happens to homeostatic process when not getting normal circadian 
signals

- Sleep regulated by homeostatic and circadian system
- disruption of the circadian system has many negative effects 
- constant light disrupts the circadian system 
- previous increase in NREM, but what happens to homeostatic 
regulation?




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



