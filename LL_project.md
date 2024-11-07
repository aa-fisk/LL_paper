Scoring seems to be completely wrong? LL_project


# Aims
- Publish LL paper
## steps
- update writing
- Feedback vlad/stuart
- sleep score extra days (somnotate)
- Analyse data
- submit for publication




# Working notes 

### Current plans 
- Make total sleep/REM/non-REM plots 
- Do totals for light/dark split 
- Plot amount of sleep per hour 
- Plot cumulative NREM sleep per hour 
- Plot SWA per hour
- Plot cumulative SWE per hour 
- plot single plot for each individual animal to start (too busy to have 
all animals on single plot) 
    - Then plot mean +/- SEM for group as a whole 


### current notes 
Do I want to put light/dark split on the same plot as totals?
- Getting busy having all animals on one plot for 3 different time series 
- can just do same thing for light and dark? 
    - but then difficult to compare as have to look at plot
    - unless force shared y axis 
- Options
    - Individual animal total/light/dark with separate plot for mean +/- SEM
    for all
        - REM - total - LL1 .... Mean
              - Light - LL1 .... Mean
              - Dark - LL1 .... Mean
        - non-REM - ...
    - Total/light/dark with individual traces and mean and SEM on each
        - REM - Total, light, dark
        - non-REM - Total, light, dark
    - One plot with total/light/dark on single plot 
        - REM plot, non-REM plot, Wake plot
    - think want option 2, best balance of all 
    - Hmmm but nagging feeling good practice to have data for each 
    individual animal as separate so can look into more 
    - so option 1 it is 
- So how do I do option 1? 
    - Modify current total script or write new script?
    - ah so because have separate calculation and plotting script
    - first step is to calculate for just light and dark 
    - ask chatgpt
    - gives big ugle messy script, surely can do with zip? 



### problems 
LL2 waaaay more sleep than everyone else 
- scoring problem
- free running period correction problem?
    - Period is the longest at 25 hours but shouldn't cause this big 
    a problem
    - but the fact that baseline is normal does suggest this is the problem





# TODO general
- check how well scoring has done 
- graph all days by vigilance state (fig 2? from paper )
- write notes on pipeline 
    - add pyedflib
- correct for free running period? 
- label as baseline/ll1,2,3 etc.
- Use wavelet analysis for period detection (also finds non-stationary periods)
- add autopep8 to make file?
- add proper docstrings to functions 


What's next?
- Scoring still has problems but good enough if go through
with refined state intervals and adjust using somnotate
- Can avoid doing manual sleep scoring for now 
- Options 
    - Plotting 
        - SWA per hour and SWE over time 
        - total sleep time / NREM/REM light/dark
        - update hynpgram colours 
    - Processing
        - manually review sleep scoring
            - how do one at a time?
        - Find period and correct for each animal to get 24 hour days
        - Figure out brief awakenings
            - Do they break episode duration at the moment?


- problem
    - since selecting more data, always going to be higher in corrected?

So what am I actually trying to do? 
do state count for each animal, all states
so have calculate state_count, next is do for all animals 



- TODO 
- change colours 
- do for all derivations 
- move where saving hypnograms 
- change away from test dir for fft and cropping
- check about sleep movement scoring vs awake 
- Why does thesis xaxis start at 0 and mine start at 5e4?
    - fill na as 0?


- Labelling days
- which days are which? 
    - 09 is baseline day
    - 10 is first day of lights on - starting at 0837
    - how does this lineup with the time index we have created? 
    - what time do the recordings actually start? 0837?
    - assuming that lights on and start of recording are at the same time
        - check later
        - check PIR files 


Pipeline
- TDT tanks recordings 
- use matlab (VVLab scripts) to convert to .mat files then export as ascii

ll_env
- convert to edf using 
bash /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/10_edf_create/01_convert_to_edf.sh

- crop edfs to just 24 hours 
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/crop_edfs.py

- Calculate FFT from EDFs
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/03_fft_autoscore.py
 
#- Crop manual annotation to match edf files 
#python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/10_edf_create/03_edf_crop.py

somnotate_env
- convert fft to visbrain 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/00_convert_sleepsign_files.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv 

- preprocess training data 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

- test on training data 
- trains full model in hold one out fashion 
- add -s to get plot as well 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/02_test_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

- train model
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/03_train_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

- preprocess unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

- apply to unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/04_run_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

- manually check intervals
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/05_manual_refinement.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

- compare intervals 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/06_compare_state_annotations.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

back to ll_env
- FFT on raw edf files 
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/03_fft_autoscore.py


- hahahahaha! It works!!!!! It all worked!!!




- Problems
- Missing LL8 180411/12 edf/ascii files? but have scored so they do
exist? hmm
- Found why some are stupidly long, they start at 2367 for some reason?


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

### Update 
CONDA_SUBDIR=osx-64 conda env update -f environment.yml

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



