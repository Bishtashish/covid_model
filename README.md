# covid_19_impact_model

## Team Members

1) Nandani Dabhi
2) Aakanksha Chauhan
3) Priyanka Jadhav
4) Salma Khayum
5) Ashish Bisht

## Project Introduction
The COVID-19 outbreak is a sharp reminder that pandemics can change the course of mankind and will continue to do so. Even if we cannot prevent dangerous viruses from emerging, we should be prepared to dampen their effects on society. The current outbreak has consequences not only on on the economy but overall on the society. In less than three months at the beginning of 2020, the COVID-19 crisis developed into a global pandemic. Schools and universities were closed in Spring'20 for more than one billion students of all ages. By June 2020, the virus spread to almost all countries and affected more than eight million people around the world. More than half of the world’s population has experienced a lockdown with strong containment measures – the first time in history that such measures have been applied on such a large scale.

The sectors that have seen the largest increases in unemployment are those that are hedonic in nature and require the physical presence of the customer (e.g., hospitality, tourism, construction and stores), as demand for these services has ceased to exist. Intuitively, we understand that the crisis will not only leave many an organization struggling for survival, but will also force some to look for alternative strategic paths. While on the one hand, the Covid-19 crisis has imposed enormous challenges on business organizations, on the other, it has also necessitated innovations, presenting organizations with opportunities to identify new business models that will allow them to survive through the crisis. Past experience indicates that once someone is outside the job market, it is very difficult to get back on their feet. Therefore, we have decided to measure most impacted people in different sectors like business, public-private sector employment, education and health. We want to visualize the impacts on different sectors in order to help people to prepare for their future job security and to accept beneficial changes taking place during this pandemic.


## Research Question

How COVID-19 has impacted different sectors such as business, education and health.

## Relevant Domain Information (links to three or more articles that relate to your research question)
1. Interim Guidance for Businesses and Employers Responding to Coronavirus Disease 2019 (COVID-19), May 2020
https://www.cdc.gov/coronavirus/2019-ncov/community/guidance-business-response.html

2. The Impact of COVID-19 on Consumers: Preparing for Digital Sales
https://ieeexplore.ieee.org/document/9076858?denied=

3. How many workers are employed in sectors directly affected by COVID-19 shutdowns, where do they work, and how much do they earn?
https://www.bls.gov/opub/mlr/2020/article/covid-19-shutdowns.htm

4. The impact of COVID-19 on small business outcomes and expectations
https://www.pnas.org/content/117/30/17656

5. Impact on the Higher Education Sector
https://www.pwc.com/sg/en/publications/a-resilient-tomorrow-covid-19-response-and-transformation/higher-education.html

## Data Sources (this may be fluid)

### Dataset Information:

Dataset used: **'Household Pulse Survey Data Tables for 2020'**
Reference : https://www.census.gov/programs-surveys/household-pulse-survey/data.html

We are doing Data analysis for **the State of North Carolina**.

Household pulse survey is designed to collect data on how people's lives have been impacted by COVID-19.
Data was collected into 3 phases :
Phase 1 of the Household Pulse Survey began on April 23, 2020 and ended on July 21, 2020. It includes 12 weekly table releases.
Phase 2 of the survey began on August 19, 2020 and ended October 26, 2020, and included 5 biweekly table releases.
Phase 3 of the survey began on October 28, 2020, and the Census Bureau expects to collect data until December 21, 2020, releasing data every two weeks just like in Phase 2.

In all the phases, data was collected on Education, Employment, Food Sufficiency and Food Security, Health, Housing, Peoples' spendings and transportation.

**Phase 1 :**
- Week 1 	: April 23 - May 5
- Week 2	: May 7 - May 12
- Week 3	: May 14 - May 19
- Week 4	: May 21 - May 26
- Week 5	: May 28 - June 2
- Week 6	: June 4 - June 9
- Week 7	: June 11 - June 16
- Week 8	: June 18 - June 23
- Week 9	: June 25 - June 30
- Week 10	: July 2 - July 7
- Week 11	: July 9 - July 14
- Week 12	: July 16 - July 21

**Phase 2 :**
- Week 13	: August 19 - August 31
- Week 14	: Sept 2 - Sept 14
- Week 15	: Sept 16 - Sept 28
- Week 16	: Sept 30 - Oct 12
- Week 17	: Oct 14 - Oct 26

**Phase 3 :**
- Week 18	: Oct 28 - Oct 9


We are using consolidated data for all the phases to come up with our observations.

## Approach:

We plan to do Exploratory data analysis of datasets which gives information about impacts of COVID-19 on different sectors. For that we are going to use the CRISP-DM approach.The Cross-Industry Standard Process for data mining (CRISP-DM) is a process model with six phases that naturally describes the data science life cycle. It’s like a set of guardrails to help you plan, organize, and implement your data science project. Currently we are planning to focus first two phases Business understanding and Data understanding. This will help us to measure the impacts.

Business understanding – What does the business need?
It focuses on understanding the project objectives and requirements from a business perspective, and then this knowledge is converted into a data mining problem definition and a preliminary plan is presented. In order to get an idea about the impact of COVID-19 on various sectors we reviewed various COVID related articles and research papers.

Data understanding – What data do we have / need? Is it clean?
It starts with an initial data collection process and proceeds with activities in order to get familiar with the data, to identify data quality problems, to discover first insights into the data, or to detect interesting subsets to form hypotheses for hidden information.
For data understanding we are planning to do Exploratory Data Analysis and Data visualization.


We will focus on below measures:

Machine Learning (Stretch Goal):

Modeling- In this step, Modeling techniques are selected and applied. Data preparation can have a loopback here as the models have specific techniques regarding the form of data presented.

Evaluation- Once one or more models have been built that appear to have high quality based on whichever loss functions have been selected, these need to be tested in order to ensure that they generalize well against unseen data and that all key business issues have been sufficiently considered.

Deployment- Generally this will mean deploying a code representation of the model into an operating system to score or categorize new unseen data as it arises and to create a mechanism for the use of that new information in the solution of the original business problem.

Finally with the help of visualization techniques, we shall provide our observations.

We have chosen 5 sectors to analyse the impact of Covid-19.
1. Education
2. Employment
3. Spending
4. Health
5. Transportation


## Known Issues (problems with predictors, reporting, bias, etc.) - this will develop over time

1. The most important known issue is finding appropriate data as impact of COVID-19 has a vast scope.
2. Lack of data standardization is also an issue. Huge amount of is available but it is not present in standard form.
3. Bias in identification before proper testing

## Conclusion
Many pandemics have occurred in the past and can even occur in the future as well, so being prepared for such pandemics is always a good idea. We hope that the analysis done by us on the impact of COVID-19 will help people to be better prepared and equipped in case of employment, education or healthcare in future.
