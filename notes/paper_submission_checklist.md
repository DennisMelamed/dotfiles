To be improved over time. Many items drawn from here: https://github.com/philippbayer/submission_checklist

# During writing tasks to complete
- [ ] Write the outline of how you want your paper organized & have someone edit it harshly
	- include experiments, what you hope to have for each figure, and a short abstract
- [ ] Make sure the first sentence of the abstract is really strong and basically conveys the message/main problem of the paper
- [ ] Verify who will be an author on the paper - any technical contacts who should be included?
- [ ] Enter conflicts of interest into conference system
- [ ] Check if there is a paper registration deadline, separate (before) the paper submission deadline
- [ ] Check if there's a supplemental allowed, what is the deadline for it? 

## Useful LaTeX Snippets:

### Make title angry if your paper is over length

Careful - this doesn't quite work right if its a table/figure that is formatted to appear on a page over the limit you set, since they're floating and not tied to the END_OF_TEXT label. You should still double check how many pages the paper has :) 


Insert the following in your preamble:
```
\newcommand{\incpageref}[1]{%
  \number\numexpr\getpagerefnumber{#1}}

```
Then replace your `\title{...}` command with (changing the 8 to the required paper length):
```
\ifnum8<\incpageref{END_OF_TEXT}
    \title{\textcolor{red}{PAPER IS OVER LENGTH: \incpageref{END_OF_TEXT}}}
\else
    \title{Your Awesome Title}
\fi
```
And add the following label to the end of your conclusion:
```
\label{END_OF_TEXT}
```



# Perform these checks on the final version of the paper before uploading for review

## PDF
- [ ] Is the authors section on the first page appropriately blinded?
- [ ] Do any author identifiers appear in the text? emails, urls, etc.
- [ ] Does the paper meet the formatting guidelines?
- [ ] Does the main content of the paper meet the page number restriction?
- [ ] Do the references meet any length restrictions? 
- [ ] Are all calls to \cite or \ref correctly processed? Make sure there are no "as seen in Figure ??" or "as John Doe et al. [??] showed" in the text
- [ ] Is the math formatted appropriately? No formulas running outside of their boxes, text too small to see, unnumbered equations, etc.
- [ ] Double check the margins, ensure nothing bleeds over into them. 
- [ ] Have you used the correct author kit if provided? Make sure its the right one for the current year! 
- [ ] Are all figures and tables referenced somewhere in the text? 
- [ ] Are all figures/tables readable in the final rendering of the pdf? Are they clean?
- [ ] Was the 'review' type formatting applied, or the 'camera-ready' type? This can often be things like line numbers, etc.
- [ ] Are tables/figures ordered? i.e. table 1 is referenced before table 2?
- [ ] If using an ordered set (model 1, model 2, etc), is this order consistent? Does the same number always refer to the same model?
- [ ] Are all special words spelled right? 
- [ ] Check figures for colorblind friendliness (http://mapeper.github.io/jsColorblindSimulator/)
- [ ] Is there any leftover placeholder text like (CITATION), doi://XYZ, Table X, [TODO]?
- [ ] Is it clear who corresponding author is?
- [ ] Author names/affiliations spelled right? 
- [ ] Are all required sections present?
- [ ] Duplicate references?
- [ ] Consistent color scheme across figures/tables? This one isn't critical, but ideally red means something similar throughout the paper
- [ ] Passed the text through spellcheck?
- [ ] If resubmitting, have you changed all references to the original conference(s) you submitted to?
- [ ] If resubmitting, have you included all suggestions you've received that seemed like good ideas? Double check emails/IMs, notes, etc.
- [ ] Are all axis labels named?
- [ ] Are the captions for all figures useful?


## Supplemental PDF
- [ ] Do any author identifiers appear anywhere in the supplemental text?

## Other supplemental material
- [ ] Do any author identifiers appear anywhere in the supplemental material? Check READMEs, code files (via grep/fuzzy finders), video files, datasets (for binary data formats, ensure that names/hostnames/emails don't appear anywhere in the metadata)
- [ ] If required, do you have a readme explaining what each file in the supplemental is, or are files described in a supplemental PDF?

# After uploading
- [ ] Have you actually hit the submit button?
- [ ] Are all required questions answered (e.g. agreement to review other papers)
- [ ] All authors entered conflicts of interest into the conference system? 
- [ ] If there are different tracks to submit to, does the one you have selected make the most sense?
- [ ] If there are options for choosing which area of research your paper falls into, have you selected the one that makes the most sense?

# Checks for camera-ready version
- [ ] Are all of the needed author names on the paper?
- [ ] Are all acknowledgements correct? grants/scholarships/institutions/projects, along with id numbers?
- [ ] Have you answered all the reviewers critical suggestions?

