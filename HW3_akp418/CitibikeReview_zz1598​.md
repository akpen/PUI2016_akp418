###  HW4_zz1598

## Assignment 1: 

## Citibike Peer Review on HW3_2

*Reviewed by Ziman Zhou (zz1598)*

The Github Account assigned to me: **akp418**.


## 1.Content Review

In Akshay's assignment, I did not find the statement of null hypothesis or alternative hypothesis.

He plotted a bar chart to show the average trip durations of subscribers and non-subscribers.

He also plotted a bar chart for weekly average trip durations of subscribers and non-subscribers.

Based on the data collected, I assume that his idea is to test that **The Citi Bike Subscribers have longer average trip duration than Non-Subscribers **(by week/by each weekday).



Therefore, I formulate a reasonable hypothesis:

**NULL HYPOTHESIS**:

The average trip duration of subscribers is the same or less than the average trip duration of customers(non-subscribers)

**H0: Mean(s) <= Mean(c)**

**ALTERNATIVE HYPOTHESIS**:

The average trip duration of subscribers is higher than the average trip duration of customers

**H1: Mean(s) > Mean(c)**

*proposed significance level*: 

**$\alpha$=0.05**


For the proposed *NULL* and *ALTERNATIVE*  hypotheses, the CitiBike dataset collected would be able to perform the hypothesis test.



## 2.Test Selection

To perform the proposed hypothesis test based on features of the data we have so far, it is appropriate to conduct a **T-test**:

* ***T-test*** is suitable to test the differences between two groups. In our case, we want to test whether one group's mean is greater or samller than the mean of the other group.

* Further more, I would suggest use ***Welch's t-test***, which works for testing the null hypothesis that two populations have equal means, with the assumption that the two samples have unequal variance and unequal sample sizes. In our case, the size of subscriber and customer groups are not the same, and the variance is not likely to be the same either.

  According to the analysis above, a proper **t-test** will be my first choice to test the hypothesis. 

*Reference* :

[When to Use Which Test]( http://www.csun.edu/~amarenco/Fcs%20682/When%20to%20use%20what%20test.pdf)

[Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test)



## 3. Suggestion

Based on the output of Akshay's data collection process followed by plotting, I have three suggestions for him:

1. Regarding your weekly trip duration bar chart, you can resize the figure or the legend so the legend will not cover part of your bars. 

2. In the future, please try to write down your ideas and hypothesis before anything else. The **Hypothesis** is very important because formulating it can help you think thoroughly about what information the data can deliver and what question you can answer using the data. This will keep you on the right track during modifying the data frame and choosing the suitable graph or chart to visualize the data, as well as selecting the most suitable test for your hypothesis.

3. Although it is possible to guess what you want to test by observing your weekly plot for subscribers and non-subscribers. However, you might have more detailed 'grouping ideas' such as comparing the trip durations on weekends over weekdays for your two biker groups, and find out if there is a difference between them (like what the lab example does in class). If so, the **null hypothesis** shall become: 

   *The average trip duration on the weekends over the weekdays of the citi bike subscribers is equal or smaller than that of the usual customers(nonsubscribers).*

   ​