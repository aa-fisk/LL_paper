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
- Version control writing and code (separate repos?)
- Get tex file to compile
- Produce figures using current code 

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


## Ideas to keep
- Ideas graveyard?
    - Convert into word somehow
        - Pandoc
            - Write custom stylesheet to use? Figure out what was 
            not working last time?
        - Question to work in word or latex?
        - Need a word version to use 
            - So either work directly in word version
                - Poor version control/experience
            - Convert between word and tex version
                - Should be easy?
                - References?
                - Looking pretty? 
                - https://en.wikibooks.org/wiki/LaTeX/Collaborative_Writing_of_LaTeX_Documents
        - What about using Rmarkdown instead of tex?
            - Seems easier? 
            - https://rmarkdown.rstudio.com/articles_docx.html
            - Guide uses RStudio
            - How to do straight from file?
    - Rewrite what currently have
        - Increase introduction so have enough info for published paper
    - More data?    
        - Who would let us use sleep score?
        - Joel Raymond at USYD? 
        https://www.sydney.edu.au/science/about/our-people/research-students/joel-raymond-543.html



- Write paper
- Convert chapter into word for VV/SNP?
- Save the tex file into its own separate project dir?
- Update code to make prettier


Analysis files taken from 
/Users/angusfisk/Documents/01_personal_files/01_work/01_dphil/01_projects/01_thesisdata





Questions

Do I want to version control data files?
    - Definitely not all
    - Do I want originals? 
    - Not now, can add in later 
    - done added to gitignore.
Version control code 
    - Don't have to worry about intermediates as already covered by \*.png
    - ignore csvs as well
Write pipeline 
    - best version in deprec implement at the moment 

Next step? 
    - Remove excess to tidy up dirs? 
    - Just get going as is?
    - New branch almost definitely then tidy from there 

- Need to remove edf and raf files? From deprec? - remove all _deprec
    
