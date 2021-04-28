# Liquidity Task

The task is to calculate the liquidity ratio, which allows us to understand much better whether
the ads are popular among seekers.
Based on this, i have prepared an analysis using the available data

**Technical part:**
  1. SQL queries that allow for liquidity calculation.
  2. Preparation also in Python for calculating liquidity for all users, i.e. we want to get a list with information about exactly how much liquidity is for each user

**Analytical part:**
  1. Please prepare a complete analysis of the data that was sent, along with the answers to the following questions

    a. What differences do you see between the segments in terms of the data you have available (including liquidity)?
    b. What do you think may affect the higher or lower liquidity level?

**Form:**
  1. Jupyter / R Markdown preferred for analysis
  2. The scripts can be in separate files or as part of the notebook depending on the methods chosen
  3. Please present the final results and the most important conclusions in the form of a presentation (e.g. Google slides)


**How to calculate the liquidity:**
  Liquidity is understood as the % of ads that received at least 1 response (by phone or e-mail) within 7 days.
  
***Example:*** </br>
  On April 1, the user added 10 ads to the website </br>
  From 1 to 7 April, he received responses to 6 ads. </br>
  On April 2, another 5 ads were added and he received replies to all of them within 7 days of their appearance on the site </br>
  
  The **liquidity calculation** is (6 + 5) / (10 + 5) = 73%
  
## Dataset
The data we have at our disposal:

  1. Data_ads (date, user_id, ad_id, category_id, params) - here you can find information about ads
  2. Data_replies (date, user_id, ad_id, mails, phones) - information about replies to the ads on a given day
  3. Data_categories (category_id, category_name) - mapping to a category tree
  4. Data_segments (user_id, segment) - mapping to segmentation for each user
  
  
