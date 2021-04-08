# DALC - Dutch Abusive Language Corpus 

This repository contains:

- the Dutch Abusive Language Corpus v1.0 (DALC v1.0) (folder "data")
- the data statement related to DALC v1.0 (see below);
- the baseline models that have been developed to identify abusive language (both binary and ternary classification)
- a copy of the [GrofLex lexicon](https://github.com/hylkevdveen/GrofLex)

This work was part of the bachelor thesis in Information Science of the University of Groningen for the academic year 2019/2020. 


# Data Statement for DALC

Data set name: Ducth Abusive Language Corpus v1.0

Citation (if available): n/a
 
Data set developer(s): Marieke Weultjes, Arjan Schelhaas, Folkert Leistra, Hylke van der Veen, Menno Robben, Gerben Timmerman 

Data statement author(s): Tommaso Caselli

Others who contributed to this document: 


## A. CURATION RATIONALE 

The corpus is composed by tweets in Ducth extracted using different strategies and covering different time windows. 

- Keywords: we have used a cross-platform approach to identify relevant keywords and reduce bias that may be introduced in manual selection of the data. We first identified a time window in Reddit, extracted all posts that received a controversial label. We then identified keywords (unigram) and retained the top 50 keywords per time window. We then used the keywords to extract tweets in corresponding periods. For each time period, we selected a sample 5,000 messages using two dictionaries containing know profanities in Dutch. An additional 5,000 messages are randomly selected. The messages are then re-shuffled and annotated.

- Geolocation: following Denti and Faggian, [2019](https://dariadenti.org/mapping-the-italian-geography-of-hate-abstract/) that show the existence of a correlation between hateful messages and disenfranchised and economic poor areas, we selected two geo-graphical areas (Zuid-Holland and Groningen) that according to a 2015 study by the Ducth Buraeu of Statistics (CBS) have the highest unemployement rates of the country. We collected 706,044 tweets posted by users whose location was set to the two target areas. The amount of messages was further filtered by removing noise (i.e., messages containing URLs), dropping to 356,401 tweets. Similarly to the keywords approach, we further filtered 2,500 messages using one profanity dictionary and collected an additional 2,500 randomly.

- Authors: we looked for seed users, i.e., users that are likely to post/use abusive language in their tweets. We created an ad-hoc list of 67 profanities, swearwords, and slurs and then searched for messages containing any of these elements in a ten-day window in December 2018 (namely 2018-11-12 – 2018-11-22), corresponding to a moment of heated debate in the country about [Zwarte Piet](https://nl.wikipedia.org/wiki/Zwartepietendebat). We collected an initial amount of 3,105,833 tweets. We then selected as seed users the top 15, i.e., the top 15 users who most frequently use in their messages any of the 67 keywords. For each of them we further collected a maximum of 100 tweets randomly, summing up to a total of 1390 tweets

Dictionaries used: [HADES](https://github.com/clips/hades); [HurtLex v1.2](https://github.com/valeriobasile/hurtlex)

- Time periods: 1) 12-11-2015/22-11-2015 (November 2015 Paris attacks); 2) 07-03-2017/17-03-2017 (2017 Dutch general election); 3) 12-11-2018/22-11-2018 (Intocht Sinterklaas 2018); 4) 2020-08 (Black Lives Matter movement); 5) 2015-04; 6) 2018-06; 7) 2019-05; 2019-09

## B. LANGUAGE VARIETY/VARIETIES

* BCP-47 language tag: nl
* Language variety description: Netherlands and Belgium (Vlaams)

## C. SPEAKER DEMOGRAPHIC

N/A
 
## D. ANNOTATOR DEMOGRAPHIC

Annotator #1: Age: 21; Gender: female; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: BA in Information science

Annotator #2: Age: 21; Gender: male; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: BA in Information science

Annotator #3: Age: 21; Gender: male; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: BA in Information science

Annotator #4: Age: 21; Gender: male; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: BA in Information science

Annotator #5: Age: 23; Gender: male; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: BA in Information science

Annotator #6: Age: 24; Gender: male; Race/ethnicity: caucasian; Native language: Dutch; Socioeconomic status:n/a Training in linguistics/other relevant discipline: MA in Information science

## E. SPEECH SITUATION

N/A

## F. TEXT CHARACTERISTICS

Twitter messages; short messages of max. 280 characters; they may contain multimedia materials, external URL links, and mentions of other others. Time period of collection illustrated in the Curation Rational section.

## G. RECORDING QUALITY

N/A

## About data statement document

A [data statement](https://www.aclweb.org/anthology/Q18-1041/) is a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected in systems built on the software.

Data Statements are from the University of Washington. Contact: [datastatements@uw.edu](mailto:datastatements@uw.edu). The markdown Data Statement we used is from June 4th 2020. The Data Statement template is based on worksheets distributed at the [2020 LREC workshop on Data Statements](https://sites.google.com/uw.edu/data-statements-for-nlp/), by Emily M. Bender, Batya Friedman, and Angelina McMillan-Major. Adapted to community Markdown template by Leon Dercyznski.






