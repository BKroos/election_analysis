# Election Analysis
## Overview
This analysis takes election data from a congressional race in Western Colorado, determining the overall vote count as well as individual candidate totals and percentages; as well as calculating county vote totals and percentages of the overall vote. 

## Election Audit Results
- A total of 369,711 votes were cast in this election
- Denver county had by far the largest turnout, accounting for nearly 83% of the vote with 306,055 votes cast in the county. Next was Jefferson county, accounting for 10% of the vote and 38,855 votes. Finally was Arapahoe county, at 7% and 24,801, respectively. 
- The runaway winner in this election was Diana DeGette, who received nearly three-quarters (73.8%) of all votes cast, with 272,892 votes. Next up, an entire half of the vote total behind, was Charles Casper Stockham, receiving 23% of votes with 85,213. Finally was Raymon Anthony Doane, who received 3% of the votes, in total 11,606. 

## Summary
The uses of this script are far-reaching. At an obvious level, it can be tweaked slightly to be used for not only future Congressional races in Western Colorado, but across all levels of elections. The analysis is written to analyze "County" names, but depending on the dataset would just as easily apply to cities, neighborhoods, census tracts, and any geographic consideration. With additional analysis, it could deliver even more granular results, as the pattern and shape of the code would be broadly the same if you wanted to receive county-specific candidate results (e.g. "Diana DeGette received 60% of all votes in Denver county.") 

Beyond elections, however, the way the code is written to take rows of data and map out prevalence of a number of options (i.e. **votes** for a **candidate**), it could be applied to relative enrollments within or across schools in school districts (**students** in **schools**) using a dataset of all students enrolled in geographic boundary (state, city, or school district as examples). For areas in which residents have an option on their energy providers, this code could return how many and what percentage of residents each provider utilizes (**customers** selecting **energy companies**). Depending on the dataset, this pattern of code can break out counts and percentages on a large variety of dimensions, saving staff time in having to run arduous, time-consuming foundational analysis, freeing up resources to begin deeper analyses.
