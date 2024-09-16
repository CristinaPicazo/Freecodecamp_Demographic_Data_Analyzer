import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df['education'])) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    total_higher_education_rich =  round(len(df.loc[(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])* 100 / (len(df['education'])))

    # What percentage of people without advanced education make more than 50K?
    total_lower_education_rich = round(len(df.loc[(~df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])* 100 / (len(df['education'])))

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(len(df.loc[(df['education'].isin(['Bachelors','Masters','Doctorate']))]))
    # higher_education = round(df[((df["education"]=='Bachelors')|
    #                            (df["education"]=='Masters')|
    #                            (df["education"]=='Doctorate'))])  /////////
    lower_education = round(len(df.loc[(~df['education'].isin(['Bachelors','Masters','Doctorate']))]))
    # print('lower_education: ', lower_education)

    # percentage with salary >50K
    higher_education_rich = round(len(df.loc[(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])* 100 / (len(df['education'])))
    educacion = len((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
    print('educacion: ', educacion)
    print('total en educación: ', len(df['education']))
    print('higher_education_rich: *********************46.5   --', higher_education_rich)

    # higher_education_rich = round(len(df.loc[(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])* 100 / (len(df['education'])))

    # higher_education_rich = round(df[((df["education"]=='Bachelors')|
    #                            (df["education"]=='Masters')|
    #                            (df["education"]=='Doctorate'))
    #                            & (df['salary'] == '>50K')]) ///////

    lower_education = round(len(df.loc[(~df['education'].isin(['Bachelors','Masters','Doctorate']))]))



    lower_education_rich = round(len(df.loc[(~df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K')])* 100 / (len(df['education'])),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50')])
    # num_min_workers = len(df[(df['hours-per-week'] == min_work_hours)]) ////

    rich_percentage = len((df['salary'] == '>50K') & df['hours-per-week'].min())
    # rich_percentage = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50')]) ////

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.loc[df['salary'] == '>50K'].max()['native-country']
    highest_earning_country_percentage = sorted(round((df[(df['salary'] == '>50K')]['native-country'].value_counts()/df['native-country'].value_counts()) * 100, 1),reverse=True) [0]
    print('highest_earning_country_percentage: **********', highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts(ascending=False).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        # [27816, 3124, 1039, 311, 271]
        print("Average age of men:", average_age_men)
        # 39.4
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        # 16.4
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        # 46.5 *
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        # 17.4 *
        print(f"Min work time: {min_work_hours} hours/week")
        # 1
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        # 10 *
        print("Country with highest percentage of rich:", highest_earning_country)
        # 'Iran' *
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        # 41.9 *
        print("Top occupations in India:", top_IN_occupation)
        # 'Prof-specialty' *

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
