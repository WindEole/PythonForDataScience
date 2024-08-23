from load_csv import load
from projection_life import display

Life_Expect_DF = load("life_expectancy_years.csv")
Income_DF = load(
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
    )
print(Life_Expect_DF)
print(Income_DF)

display(Life_Expect_DF, Income_DF, "1900")
