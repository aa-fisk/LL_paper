# LL_project


# Aims
- Publish LL paper
## Plan
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
## steps
- update writing
- Feedback vlad/stuart
- sleep score extra days (somnotate/manual)
- Analyse data
- submit for publication

# Workingnotes 

## TODO
- Make total sleep/REM/non-REM plots 
- Do totals for light/dark split 
- Plot amount of sleep per hour 
- Plot cumulative NREM sleep per hour 
- Plot SWA per hour
- Plot cumulative SWE per hour 
- plot single plot for each individual animal to start (too busy to have 
all animals on single plot) 
    - Then plot mean +/- SEM for group as a whole 
- Make file
- make convert to/from word
- make run all scripts to generate figures?
- Remove underscores from variable names

### TODO general/later 
- investigate LL2 more sleep
- check how well scoring has done 
- graph all days by vigilance state (fig 2? from paper )
- write notes on pipeline 
    - add pyedflib
- correct for free running period? 
- label as baseline/ll1,2,3 etc.
- Use wavelet analysis for period detection (also finds non-stationary periods)
- add autopep8 to make file?
- add proper docstrings to functions 
- Brief awakenings? 

### Issues 
LL2 waaaay more sleep than everyone else 
- scoring problem
- free running period correction problem?
    - Period is the longest at 25 hours but shouldn't cause this big 
    a problem
    - but the fact that baseline is normal does suggest this is the problem
- Labelling days
- which days are which? 
    - 09 is baseline day
    - 10 is first day of lights on - starting at 0837
    - how does this lineup with the time index we have created? 
    - what time do the recordings actually start? 0837?
    - assuming that lights on and start of recording are at the same time
        - check later
        - check PIR files 


## Make total sleep/REM/nREM plots  
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
- Okay so good start but currently doing selection of first 12 hours then 
the offset which is awkward because want the other way around, 
- can't I just resample every 12 hours instead and then choose just the
first/second
- YES BUT aarrggh error handling
- depends on when starts day? - wait no it doesn't, 7 is just the offset 
so should handle it? 
- what am I worried about? - if data recording started after 7pm that 
will be selected as the light period instead of dark 
- why is this one getting 19:00 as the start then? 
- ah LL8 always causing me problems 
- so data recording says it starts at 00:00:00 - where is this coming from? 
- from clean_fft_files - this feels like an artefact then 

- Splitting into light/dark totals
- Trying to understand what offset is doing and if doing what I want it to
- Looking at clean_fft_files to figure out how timeindex constructed
    - Is it arbitrary or when recording actually started?
    - 



# Scripts 
## Pipeline
- TDT tanks recordings 
- use matlab (VVLab scripts) to convert to .mat files then export as ascii

#### in ll_env

1. convert to edf using 
bash /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/10_edf_create/01_convert_to_edf.sh

2. crop edfs to just 24 hours 
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/crop_edfs.py

3. Calculate FFT from EDFs
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/03_fft_autoscore.py
 
#- Crop manual annotation to match edf files 
#python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/10_edf_create/03_edf_crop.py

#### in somnotate_env
4. convert fft to visbrain 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/00_convert_sleepsign_files.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv 

5. preprocess training data 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

6. test on training data 
- trains full model in hold one out fashion 
- add -s to get plot as well 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/02_test_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

7. train model
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/03_train_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

8. preprocess unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/01_preprocess_signals.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

9. apply to unannotated 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/04_run_state_annotation.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/01_model/model.pickle

10. manually check intervals
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/05_manual_refinement.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_unannotated.csv

11. compare intervals 
python /Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/somnotate/example_pipeline/06_compare_state_annotations.py /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/09_somnotate/spreadsheet_annotated.csv

#### in ll_env
12. FFT on raw edf files 
python /Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/02_analysis_files/01_preprocessing/03_fft_autoscore.py


## Writing conversion

### 01 tex to md
pandoc 01_chapter3.tex -o 02_ch3.md --bibliography=thesis_references.bib --citeproc -M link-citations=True

### 02 md to word 
pandoc 02_ch3.md -o 03_ch3.docx --bibliography=thesis_references.bib --citeproc -M link-citations=True --reference-doc tex_word_custom_reference.docx

### 03 word to md
pandoc 03_ch3.docx -o 04_ch3.md --bibliography=thesis_references.bib --citeproc -M link-citations=True --reference-doc tex_word_custom_reference.docx

## environment creation 

### Create environment
CONDA_SUBDIR=osx-64 conda env create -f environment.yml

### Update 
CONDA_SUBDIR=osx-64 conda env update -f environment.yml

## Analysis
### Run preprocessing
python 02_analysis/01_preprocessing/01_clean_fft.py
python 02_analysis/01_preprocessing/02_stage_file.py






# Reference Info
Writing files taken from 
/Users/angusfisk/Dropbox/01_PhD_things/02_Projects/06_thesis/03_lleeg
Analysis files taken from 
/Users/angusfisk/Documents/01_personal_files/01_work/01_dphil/01_projects/01_thesisdata



