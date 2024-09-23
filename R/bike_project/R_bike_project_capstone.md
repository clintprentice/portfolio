Bike Data Markdown
================
Clint
2024-09-19

# Introduction

Hello! This is a capstone project for my work in the Google Data
Analytics course on Coursera. In this, I will explain my analysis
process from start to finish. The dataset can be found
[here](https://divvy-tripdata.s3.amazonaws.com/index.html). My goal is
to add this project to my portfolio! I will be using Spreadsheets, R,
and Tableau to complete this project, in varying stages.

## Scenario

##### Text pulled from capstone project file

You are a junior data analyst working on the marketing analyst team at
Cyclistic, a bike-share company in Chicago. The director of marketing
believes the company’s future success depends on maximizing the number
of annual memberships. Therefore, your team wants to understand how
casual riders and annual members use Cyclistic bikes differently. From
these insights, your team will design a new marketing strategy to
convert casual riders into annual members. But first, Cyclistic
executives must approve your recommendations, so they must be backed up
with compelling data insights and professional data visualizations.

## Characters and teams

##### Text pulled from capstone project file

- Cyclistic: A bike-share program that features more than 5,800 bicycles
  and 600 docking stations. Cyclistic sets itself apart by also offering
  reclining bikes, hand tricycles, and cargo bikes, making bike-share
  more inclusive to people with disabilities and riders who can’t use a
  standard two-wheeled bike. The majority of riders opt for traditional
  bikes; about 8% of riders use the assistive options. Cyclistic users
  are more likely to ride for leisure, but about 30% use the bikes to
  commute to work each day.
- Lily Moreno: The director of marketing and your manager. Moreno is
  responsible for the development of campaigns and initiatives to
  promote the bike-share program. These may include email, social media,
  and other channels.
- Cyclistic marketing analytics team: A team of data analysts who are
  responsible for collecting, analyzing, and reporting data that helps
  guide Cyclistic marketing strategy. You joined this team six months
  ago and have been busy learning about Cyclistic’s mission and business
  goals—as well as how you, as a junior data analyst, can help Cyclistic
  achieve them.
- Cyclistic executive team: The notoriously detail-oriented executive
  team will decide whether to approve the recommended marketing program.

## About the company

##### Text pulled from capstone project file

In 2016, Cyclistic launched a successful bike-share offering. Since
then, the program has grown to a fleet of 5,824 bicycles that are
geotracked and locked into a network of 692 stations across Chicago. The
bikes can be unlocked from one station and returned to any other station
in the system anytime.

Until now, Cyclistic’s marketing strategy relied on building general
awareness and appealing to broad consumer segments. One approach that
helped make these things possible was the flexibility of its pricing
plans: single-ride passes, full-day passes, and annual memberships.
Customers who purchase single-ride or full-day passes are referred to as
casual riders. Customers who purchase annual memberships are Cyclistic
members.

Cyclistic’s finance analysts have concluded that annual members are much
more profitable than casual riders. Although the pricing flexibility
helps Cyclistic attract more customers, Moreno believes that maximizing
the number of annual members will be key to future growth. Rather than
creating a marketing campaign that targets all-new customers, Moreno
believes there is a solid opportunity to convert casual riders into
members. She notes that casual riders are already aware of the Cyclistic
program and have chosen Cyclistic for their mobility needs.

Moreno has set a clear goal: Design marketing strategies aimed at
converting casual riders into annual members. In order to do that,
however, the team needs to better understand how annual members and
casual riders differ, why casual riders would buy a membership, and how
digital media could affect their marketing tactics. Moreno and her team
are interested in analyzing the Cyclistic historical bike trip data to
identify trends.

## Ask

Three questions will guide the future marketing program:

1.  How do annual members and casual riders use Cyclistic bikes
    differently?
2.  Why would casual riders buy Cyclistic annual memberships?
3.  How can Cyclistic use digital media to influence casual riders to
    become members?

Moreno has assigned you the first question to answer: **How do annual
members and casual riders use Cyclistic bikes differently?** You will
produce a report with the following deliverables:

1.  A clear statement of the business task
2.  A description of all data sources used
3.  Documentation of any cleaning or manipulation of data
4.  A summary of your analysis
5.  Supporting visualizations and key findings
6.  Your top three recommendations based on your analysis

# Preparing Data

First, I began by downloading the rideshare data for the last 12 months,
which I have stored on my personal computer. This means my data is
locked and cannot be influenced by others. Just how I want it when
analysing a historical dataset. Before manipulating the data at all, I
have stored a backup on my computer in a separate folder, in case I need
to reference the original data again for any reason.

The data for all twelve months is stored in .csv files.

They all include the same 13 columns, which is great because this will
help us smooth out our cleaning stage. Those columns are:

1.  ride_id
2.  rideable_type
3.  started_at
4.  ended_at
5.  start_station_name
6.  start_station_id
7.  end_station_name
8.  end_station_id
9.  start_lat
10. start_lng
11. end_lat
12. end_lng
13. member_casual

The total number of rows is over 5 million! Yikes! Definitely going to
need to use R to compile and analyze these honkers.

Let’s get those uploaded and cleaned in R.

# Analyze the Data using R

Oh boy! The coding part. Here we go, y’all!

First we’re going to set the directory and load the packages we want.

``` r
setwd("C:/Users/clint/Documents/Capstone/bike_project_R/202309-202408_trip_data")
library(tidyverse)
```

    ## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ## ✔ dplyr     1.1.4     ✔ readr     2.1.5
    ## ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ## ✔ ggplot2   3.5.1     ✔ tibble    3.2.1
    ## ✔ lubridate 1.9.3     ✔ tidyr     1.3.1
    ## ✔ purrr     1.0.2     
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()
    ## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
library(conflicted)
conflict_prefer("filter", "dplyr")
```

    ## [conflicted] Will prefer dplyr::filter over any other package.

``` r
conflict_prefer("lag", "dplyr")
```

    ## [conflicted] Will prefer dplyr::lag over any other package.

``` r
library(lubridate)
library(scales)
```

Then we’re going to upload the data for all twelve months into R.

``` r
data_files <- list.files(pattern = "*.csv")
all_data <- map_df(data_files, read_csv)
```

    ## Rows: 666371 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 537113 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 362518 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 224073 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 144873 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 223164 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 301687 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 415025 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 609493 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 710721 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 748962 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 755639 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr  (7): ride_id, rideable_type, start_station_name, start_station_id, end_...
    ## dbl  (4): start_lat, start_lng, end_lat, end_lng
    ## dttm (2): started_at, ended_at
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## Rows: 24 Columns: 3
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (2): months, member_casual
    ## dbl (1): row_count
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

## Clean Up and Add Data to Prepare for Analysis

We will want to add some additional columns of data – such as day,
month, year – that provide additional opportunities to aggregate the
data.

``` r
bike_data <- all_data %>% 
  select("ride_id", "rideable_type", "started_at", "ended_at",
         "start_station_name", "end_station_name", "member_casual") %>% 
  na.omit() %>%
  mutate(
    ride_length = as.numeric(difftime(ended_at, started_at, units = "secs")),
    date = as.Date(started_at),
    weekday = format(date, "%A"),
    month = format(date, "%m"),
    day = format(date, "%d"),
    year = format(date, "%Y"),
  ) %>% 
  distinct(ride_id, .keep_all = TRUE) %>%  # Remove duplicates based on ride_id
  select("ride_id", "rideable_type", "started_at", "ended_at", "start_station_name", 
         "end_station_name", "weekday", "ride_length", "member_casual", "date", 
         "month", "day", "year") %>% 
  filter(ride_length >= 60, ride_length <= (60 * 60 * 24))
```

Look at that! Beautiful. Now that our data is cleaned we can actually do
some analysis.

## Analyzing the Data

#### First we’ll start by finding the average, midpoint, maximum, and minimums for our ride times.

Month Count

``` r
month_count = bike_data %>% 
  group_by(months = month.name[month(started_at)], member_casual) %>% 
  summarize(row_count = n()) %>% 
  arrange(match(months,month.name))
```
``` r
print(month_count)
```

    ## # A tibble: 24 × 3
    ## # Groups:   months [12]
    ##    months   member_casual row_count
    ##    <chr>    <chr>             <int>
    ##  1 January  casual            17364
    ##  2 January  member            93511
    ##  3 February casual            37599
    ##  4 February member           144427
    ##  5 March    casual            61775
    ##  6 March    member           164660
    ##  7 April    casual            92205
    ##  8 April    member           200268
    ##  9 May      casual           164294
    ## 10 May      member           269961
    ## # ℹ 14 more rows

Weekday Count

``` r
weekday_count = bike_data %>% 
  group_by(weekday = weekday, member_casual = member_casual) %>% 
  summarize(row_count = n())
```
``` r
print(weekday_count)
```

    ## # A tibble: 14 × 3
    ## # Groups:   weekday [7]
    ##    weekday   member_casual row_count
    ##    <chr>     <chr>             <int>
    ##  1 Friday    casual           216866
    ##  2 Friday    member           380331
    ##  3 Monday    casual           166280
    ##  4 Monday    member           381681
    ##  5 Saturday  casual           315790
    ##  6 Saturday  member           341552
    ##  7 Sunday    casual           253410
    ##  8 Sunday    member           294729
    ##  9 Thursday  casual           177175
    ## 10 Thursday  member           420648
    ## 11 Tuesday   casual           158295
    ## 12 Tuesday   member           416674
    ## 13 Wednesday casual           180052
    ## 14 Wednesday member           441452

Top Start Station

``` r
top_start_station = bike_data %>% 
  group_by(start_station_name, member_casual) %>% 
  summarize(row_count = n()) %>% 
  arrange(desc(row_count))
```
``` r
print(top_start_station)
```

    ## # A tibble: 3,096 × 3
    ## # Groups:   start_station_name [1,669]
    ##    start_station_name                 member_casual row_count
    ##    <chr>                              <chr>             <int>
    ##  1 Streeter Dr & Grand Ave            casual            45559
    ##  2 DuSable Lake Shore Dr & Monroe St  casual            30099
    ##  3 Kingsbury St & Kinzie St           member            25008
    ##  4 Clinton St & Washington Blvd       member            24810
    ##  5 Michigan Ave & Oak St              casual            22511
    ##  6 Clark St & Elm St                  member            21848
    ##  7 Clinton St & Madison St            member            21229
    ##  8 DuSable Lake Shore Dr & North Blvd casual            20487
    ##  9 Shedd Aquarium                     casual            19025
    ## 10 Millennium Park                    casual            18975
    ## # ℹ 3,086 more rows

Top End Station

``` r
top_end_station = bike_data %>% 
  group_by(end_station_name, member_casual) %>% 
  summarize(row_count = n()) %>% 
  arrange(desc(row_count))
```
``` r
print(top_end_station)
```

    ## # A tibble: 3,118 × 3
    ## # Groups:   end_station_name [1,678]
    ##    end_station_name                   member_casual row_count
    ##    <chr>                              <chr>             <int>
    ##  1 Streeter Dr & Grand Ave            casual            49658
    ##  2 DuSable Lake Shore Dr & Monroe St  casual            27801
    ##  3 Clinton St & Washington Blvd       member            25450
    ##  4 Kingsbury St & Kinzie St           member            24958
    ##  5 DuSable Lake Shore Dr & North Blvd casual            23831
    ##  6 Michigan Ave & Oak St              casual            23364
    ##  7 Clinton St & Madison St            member            22322
    ##  8 Clark St & Elm St                  member            21922
    ##  9 Millennium Park                    casual            21124
    ## 10 Wells St & Concord Ln              member            18154
    ## # ℹ 3,108 more rows

Average Ride Length

``` r
ride_length = bike_data %>% 
  group_by(member_casual) %>% 
  summarize(mean(ride_length))
print(ride_length)
```

    ## # A tibble: 2 × 2
    ##   member_casual `mean(ride_length)`
    ##   <chr>                       <dbl>
    ## 1 casual                      1459.
    ## 2 member                       757.

Rides per Weekday by membership

``` r
ridership_weekday = bike_data %>% 
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(member_casual, weekday) %>% 
  summarise(number_of_rides = n(),
            average_duration = mean(ride_length)) %>% 
  arrange(member_casual, weekday)
```
``` r
print(ridership_weekday)
```

    ## # A tibble: 14 × 4
    ## # Groups:   member_casual [2]
    ##    member_casual weekday number_of_rides average_duration
    ##    <chr>         <ord>             <int>            <dbl>
    ##  1 casual        Sun              253410            1675.
    ##  2 casual        Mon              166280            1408.
    ##  3 casual        Tue              158295            1256.
    ##  4 casual        Wed              180052            1304.
    ##  5 casual        Thu              177175            1265.
    ##  6 casual        Fri              216866            1410.
    ##  7 casual        Sat              315790            1647.
    ##  8 member        Sun              294729             851.
    ##  9 member        Mon              381681             719.
    ## 10 member        Tue              416674             722.
    ## 11 member        Wed              441452             737.
    ## 12 member        Thu              420648             719.
    ## 13 member        Fri              380331             739.
    ## 14 member        Sat              341552             852.

Visualizing Data for number of rides per weekday

``` r
bike_data %>%
  mutate(weekday = wday(started_at, label = TRUE)) %>%
  group_by(member_casual, weekday) %>%
  summarise(number_of_rides = n()
            ,average_duration = mean(ride_length)) %>%
  arrange(member_casual, weekday) %>%
  ggplot(aes(x = weekday, y = number_of_rides, fill = member_casual)) +
  geom_col(position = "dodge") +
  scale_y_continuous(labels = comma)
```

    ## `summarise()` has grouped output by 'member_casual'. You can override using the
    ## `.groups` argument.

![](R_bike_project_capstone_files/figure-gfm/rides%20per%20weekday-1.png)<!-- -->

Visualization for average duration between memberships

``` r
bike_data %>%
  mutate(weekday = wday(started_at, label = TRUE)) %>%
  group_by(member_casual, weekday) %>%
  summarise(number_of_rides = n(),
            average_duration = mean(ride_length)) %>%
  arrange(member_casual, weekday) %>%
  ggplot(aes(x = weekday, y = average_duration, fill = member_casual)) +
  geom_col(position = "dodge") +
  scale_y_continuous(labels = comma)
```

    ## `summarise()` has grouped output by 'member_casual'. You can override using the
    ## `.groups` argument.

![](R_bike_project_capstone_files/figure-gfm/average%20duration-1.png)<!-- -->

# Answering the initial question:

## How do annual members and casual riders use Cyclistic bikes differently?

Judging from the data we can see that casual riders take longer bike
rides than members. Casual riders also take more rides on the weekends
rather than the weekdays.

### What can we determine from this?

Casual riders are taking more leisurely rides while annual members are
more likely to use Cyclistic bikes for commuting or short trips.

### How could the team and business apply these insights?

1.  If we’re trying to convert casual riders to annual members, we can
    target focus ads on the weekends to catch more casual riders.
2.  We can also use the casual riders top_start_station and
    top_end_station as a means to reach that audience more directly.
3.  Figuring out the cost/benefit analysis of casual riders to annual
    members and use that as an additional data point in favor of
    converting to an annual membership. i.e. “Casual riders that upgrade
    to an annual membership save xx% each year.”
