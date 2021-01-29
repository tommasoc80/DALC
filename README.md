# DALC - Dutch Abusive Language Corpus 


# Data Statement for DALC

Data set name: Ducth Abusive Language Corpus v1.0

Citation (if available): n/a
 
Data set developer(s): Arjan Schelhaas, Marieke Weultjes, Folkert Leistra, Hylke van der Veen, Gerben Timmerman 

Data statement author(s): Tommaso Caselli

Others who contributed to this document: 


## A. CURATION RATIONALE 

The corpus is composed by tweets in Ducth extracted using different strategies and covering different time windows. 

- Keywords: we have used a cross-platform approach to identify relevant keywords and reduce bias that may be introduced in manual selection of the data. We first identified a time window in Reddit, extracted all posts that received a controversial label. We then identified keywords (unigram) and retained the top 50 keywords per time window. We then used the keywords to extract tweets in corresponding periods. For each time period, we selected a sample 5,000 messages using two dictionaries containing know profanities in Dutch. An additional 5,000 messages are randomly selected. The messages are then re-shuffled and annotated.

- Geolocation: following Denti and Faggian, [2019](https://dariadenti.org/mapping-the-italian-geography-of-hate-abstract/) that show the existence of a correlation between hateful messages and disenfranchised and economic poor areas, we selected two geo-graphical areas (Zuid-Holland and Groningen) that according to a 2015 study by the Ducth Buraeu of Statistics (CBS) have the highest unemployement rates of the country. We collected 706,044 tweets posted by users whose location was set to the two target areas. The amount of messages was further filtered by removing noise (i.e., messages containing URLs), dropping to 356,401 tweets. Similarly to the keywords approach, we further filtered 2,500 messages using one profanity dictionary and collected an additional 2,500 randomly.

- Authors: we looked for seed users, i.e., users that are likely to post/use abusive language in their tweets. We created an ad-hoc list of 67 profanities, swearwords, and slurs and then searched for messages containing any of these elements in a ten-day window in December 2018 (namely 2018-11-12 – 2018-11-22), corresponding to a moment of heated debate in the country about [Zwarte Piet](https://nl.wikipedia.org/wiki/Zwartepietendebat). We collected an initial amount of 3,105,833 tweets. We then selected as seed users the top 15, i.e., the top 15 users who most frequently use in their messages any of the 67 keywords. For each of them we further collected a maximum of 100 tweets randomly, summing up to a total of 1390 tweets

Dictionaries used: [HADES](https://github.com/clips/hades); [HurtLex v1.2](https://github.com/valeriobasile/hurtlex)


12-11-2015 07-03-2017 12-11-2018
22-11-2015 17-03-2017 22-11-2018
November 2015 Paris attacks 2017 Dutch general election Intocht Sinterklaas 2018

> *Explanation.* Which texts were included and what were the goals in selecting texts, both in the original collection and in any further sub-selection? This can be especially important in datasets too large to thoroughly inspect by hand. An explicit statement of the curation rationale can help dataset users make inferences about what other kinds of texts systems trained with them could conceivably generalize to.

## B. LANGUAGE VARIETY/VARIETIES

> *Explanation.* Languages differ from each other in structural ways that can interact with NLP algorithms. Within a language, regional or social dialects can also show great variation (Chambers and Trudgill, 1998). The language and language variety should be described with a language tag from BCP-47 identifying the language variety (e.g., en-US or yue-Hant-HK), and a prose description of the language variety, glossing the BCP-47 tag and also providing further information (e.g., "English as spoken in Palo Alto, California", or "Cantonese written with traditional characters by speakers in Hong Kong who are bilingual in Mandarin").

* BCP-47 language tag: 
* Language variety description: 

## C. SPEAKER DEMOGRAPHIC

> *Explanation.* Sociolinguistics has found that variation (in pronunciation, prosody, word choice, and grammar) correlates with speaker demographic characteristics (Labov, 1966), as speakers use linguistic variation to construct and project identities (Eckert and Rickford, 2001). Transfer from native languages (L1) can affect the language produced by non-native (L2) speakers (Ellis, 1994, Ch. 8). A further important type of variation is disordered speech (e.g., dysarthria). Specifications include: 

* Description: 
* Age: 
* Gender: 
* Race/ethnicity (according to locally appropriate categories): 
* First language(s): 
* Socioeconomic status: 
* Number of different speakers represented: 
* Presence of disordered speech: 
 
## D. ANNOTATOR DEMOGRAPHIC

> *Explanation.* What are the demographic characteristics of the annotators and annotation guideline developers? Their own “social address” influences their experience with language and thus their perception of what they are annotating. Specifications include:

* Description: 
* Age: 
* Gender: 
* Race/ethnicity (according to locally appropriate categories): 
* First language(s): 
* Training in linguistics/other relevant discipline: 


## E. SPEECH SITUATION

> *Explanation.* Characteristics of the speech situation can affect linguistic structure and patterns at many levels. The intended audience of a linguistic performance can also affect linguistic choices on the part of speakers. The time and place provide broader context for understanding how the texts collected relate to their historical moment and should also be made evident in the data statement. Specifications include:

* Description: 
* Time: 
* Place: 
* Modality (spoken/signed, written): 
* Scripted/edited vs. spontaneous: 
* Synchronous vs. asynchronous interaction: 
* Intended audience: 

## F. TEXT CHARACTERISTICS

> *Explanation.* Both genre and topic influence the vocabulary and structural characteristics of texts (Biber, 1995), and should be specified.

## G. RECORDING QUALITY

> *Explanation.* For data that include audiovisual recordings, indicate the quality of the recording equipment and any aspects of the recording situation that could impact recording quality.

## H. OTHER

> *Explanation.* There may be other information of relevance as well. Please use this space to develop any further categories that are relevant for your dataset. 

## I. PROVENANCE APPENDIX

> *Explanation.* For datasets built out of existing datasets, the data statements for the source datasets should be included as an appendix.


## About this document

A data statement is a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected in systems built on the software.

Data Statements are from the University of Washington. Contact: [datastatements@uw.edu](mailto:datastatements@uw.edu). This document template is licensed as [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).

This version of the markdown Data Statement is from June 4th 2020. The Data Statement template is based on worksheets distributed at the [2020 LREC workshop on Data Statements](https://sites.google.com/uw.edu/data-statements-for-nlp/), by Emily M. Bender, Batya Friedman, and Angelina McMillan-Major. Adapted to community Markdown template by Leon Dercyznski.



Data Statements paper, here: https://www.aclweb.org/anthology/Q18-1041/ .



