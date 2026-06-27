Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
df=pd.read_csv
df=pd.read_csv(r"C:\Users\Lenovo\Downloads\NFHS-5-master\NFHS-5-master\NFHS-5-States.csv")
df
            state state_code  ... nfhs5_total  nfhs4_total
0           India        NaN  ...        71.8         68.8
1           India        NaN  ...        26.5         28.6
2           India        NaN  ...      1020.0        991.0
3           India        NaN  ...       929.0        919.0
4           India        NaN  ...        89.1         79.7
...           ...        ...  ...         ...          ...
4842  West Bengal         WB  ...         9.7          8.9
4843  West Bengal         WB  ...        10.8          NaN
4844  West Bengal         WB  ...        48.1          NaN
4845  West Bengal         WB  ...         1.1          NaN
4846  West Bengal         WB  ...        18.1          NaN

[4847 rows x 7 columns]
#step 1
df.head()
   state state_code  ... nfhs5_total  nfhs4_total
0  India        NaN  ...        71.8         68.8
1  India        NaN  ...        26.5         28.6
2  India        NaN  ...      1020.0        991.0
3  India        NaN  ...       929.0        919.0
4  India        NaN  ...        89.1         79.7

[5 rows x 7 columns]
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 4847 entries, 0 to 4846
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   state        4847 non-null   str    
 1   state_code   4716 non-null   str    
 2   indicator    4847 non-null   str    
 3   nfhs5_urban  4693 non-null   float64
 4   nfhs5_rural  4635 non-null   float64
 5   nfhs5_total  4799 non-null   float64
 6   nfhs4_total  3660 non-null   float64
dtypes: float64(4), str(3)
memory usage: 265.2 KB
\
df["indicator"].unique()
<StringArray>
[                                '1. Female population age 6 years and above who ever attended school (%)',
                                                                    '2. Population below age 15 years (%)',
                                          '3. Sex ratio of the total population (females per 1,000 males)',
                '4. Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                   '5. Children under age 5 years whose birth was registered with the civil authority (%)',
                                   '6. Deaths in the last 3 years registered with the civil authority (%)',
                                                 '7. Population living in households with electricity (%)',
                          '8. Population living in households with an improved drinking-water source1 (%)',
                        '9. Population living in households that use an improved sanitation facility2 (%)',
                                                        '10. Households using clean fuel for cooking3 (%)',
 ...
                                           '123. Women having a mobile phone that they themselves use (%)',
   '124. Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)',
                '125. Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)',
 '126. Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)',
                          '127. Young women age 18-29 years who experienced sexual violence by age 18 (%)',
                                       '128. Women age 15 years and above who use any kind of tobacco (%)',
                                         '129. Men age 15 years and above who use any kind of tobacco (%)',
                                               '130. Women age 15 years and above who consume alcohol (%)',
                                                 '131. Men age 15 years and above who consume alcohol (%)',
                     '66. Children age 9-35 months who received a vitamin A dose in the last 6 months (%)']
Length: 132, dtype: str
#health columns:obesiuty(men/women),anaemia(children/women), high blood sugar/hypertension(men/women)
obesity=df[df["indicator"].str.contains("overweight or obese",case=False)]
df["obesity"]
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'obesity'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df["obesity"]
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'obesity'
obesity
                          state state_code  ... nfhs5_total  nfhs4_total
87                        India        NaN  ...        24.0         20.6
88                        India        NaN  ...        22.9         18.9
218   Andaman & Nicobar Islands         AN  ...        38.1         31.8
219   Andaman & Nicobar Islands         AN  ...        45.3         38.2
349              Andhra Pradesh         AP  ...        36.3         33.2
...                         ...        ...  ...         ...          ...
4542              Uttar Pradesh         UP  ...        18.5         12.5
4672                Uttarakhand         UT  ...        29.7         20.4
4673                Uttarakhand         UT  ...        27.1         17.7
4803                West Bengal         WB  ...        22.7         19.9
4804                West Bengal         WB  ...        16.2         14.2

[74 rows x 7 columns]
obesity["indicator"].unique()
<StringArray>
['88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)', '89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)']
Length: 2, dtype: str
blood = df[
    df["indicator"].str.contains("Blood sugar", case=False)
]
blood
            state state_code  ... nfhs5_total  nfhs4_total
98          India        NaN  ...         6.1          NaN
99          India        NaN  ...         6.3          NaN
100         India        NaN  ...        13.5          NaN
101         India        NaN  ...         7.3          NaN
102         India        NaN  ...         7.2          NaN
...           ...        ...  ...         ...          ...
4815  West Bengal         WB  ...         7.7          NaN
4816  West Bengal         WB  ...        17.5          NaN
4817  West Bengal         WB  ...        10.8          NaN
4818  West Bengal         WB  ...         9.5          NaN
4819  West Bengal         WB  ...        21.3          NaN

[222 rows x 7 columns]
blood["indicator"].unique()
<StringArray>
[                                                           '99. Blood sugar level - high (141-160 mg/dl)23 (%)',
                                                         '100. Blood sugar level - very high (>160 mg/dl)23 (%)',
 '101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)',
                                                           '102. Blood sugar level - high (141-160 mg/dl)23 (%)',
                                                         '103. Blood sugar level - very high (>160 mg/dl)23 (%)',
 '104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)']
Length: 6, dtype: str
anaemia = df[
    df["indicator"].str.contains("anaemia", case=False)
]
hypertension = df[
    df["indicator"].str.contains("hypertension", case=False)
]
hypertension = df[
    df["indicator"].str.contains("blood pressure", case=False)
]
hypertension["indicator"].unique()
<StringArray>
[                                 '105. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)',
                      '106. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)',
 '107. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)',
                                  '108. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)',
                      '109. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)',
 '110. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)']
Length: 6, dtype: str
women_anaemia = df[
    df["indicator"].str.contains(
        "Women age 15-49 years who are anaemic",
        case=False
    )
]
children_anaemia = df[
    df["indicator"].str.contains(
        "Children age 6-59 months who are anaemic",
        case=False
    )
]
for i in df["indicator"].unique():
    print(i)

    
1. Female population age 6 years and above who ever attended school (%)
2. Population below age 15 years (%)
3. Sex ratio of the total population (females per 1,000 males)
4. Sex ratio at birth for children born in the last five years (females per 1,000 males)
5. Children under age 5 years whose birth was registered with the civil authority (%)
6. Deaths in the last 3 years registered with the civil authority (%)
7. Population living in households with electricity (%)
8. Population living in households with an improved drinking-water source1 (%)
9. Population living in households that use an improved sanitation facility2 (%)
10. Households using clean fuel for cooking3 (%)
11. Households using iodized salt (%)
12. Households with any usual member covered under a health insurance/financing scheme (%)
13. Children age 5 years who attended pre-primary school during the school year 2019-20 (%)
14. Women who are literate4 (%)
15. Men who are literate4 (%)
16. Women with 10 or more years of schooling (%)
17. Men with 10 or more years of schooling (%)
18. Women who have ever used the internet (%)
19. Men who have ever used the internet (%)
20. Women age 20-24 years married before age 18 years (%)
21. Men age 25-29 years married before age 21 years (%)
22. Total fertility rate (children per woman)
23. Women age 15-19 years who were already mothers or pregnant at the time of the survey (%)
24. Adolescent fertility rate for women age 15-19 years5
25. Neonatal mortality rate (NNMR)
26. Infant mortality rate (IMR)
27. Under-five mortality rate (U5MR)
28. Any method6 (%)
29. Any modern method6 (%)
30. Female sterilization (%)
31. Male sterilization (%)
32. IUD/PPIUD (%)
33. Pill (%)
34. Condom (%)
35. Injectables (%)
36. Total unmet need7 (%)
37. Unmet need for spacing7 (%)
38. Health worker ever talked to female non-users about family planning (%)
39. Current users ever told about side effects of current method8 (%)
40. Mothers who had an antenatal check-up in the first trimester (%)
41. Mothers who had at least 4 antenatal care visits (%)
42. Mothers whose last birth was protected against neonatal tetanus9 (%)
43. Mothers who consumed iron folic acid for 100 days or more when they were pregnant (%)
44. Mothers who consumed iron folic acid for 180 days or more when they were pregnant (%)
45. Registered pregnancies for which the mother received a Mother and Child Protection (MCP) card (%)
46. Mothers who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)
47. Average out-of-pocket expenditure per delivery in a public health facility (Rs.)
48. Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)
49. Children who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)
50. Institutional births (%)
51. Institutional births in public facility (%)
52. Home births that were conducted by skilled health personnel10 (%)
53. Births attended by skilled health personnel10 (%)
54. Births delivered by caesarean section (%)
55. Births in a private health facility that were delivered by caesarean section (%)
56. Births in a public health facility that were delivered by caesarean section (%)
57. Children age 12-23 months fully vaccinated based on information from either vaccination card or mother's recall11 (%)
58. Children age 12-23 months fully vaccinated based on information from vaccination card only12 (%)
59. Children age 12-23 months who have received BCG (%)
60. Children age 12-23 months who have received 3 doses of polio vaccine13 (%)
61. Children age 12-23 months who have received 3 doses of penta or DPT vaccine (%)
62. Children age 12-23 months who have received the first dose of measles-containing vaccine (MCV) (%)
63. Children age 24-35 months who have received a second dose of measles-containing vaccine (MCV) (%)
64. Children age 12-23 months who have received 3 doses of rotavirus vaccine14 (%)
65. Children age 12-23 months who have received 3 doses of penta or hepatitis B vaccine (%)
66. Children age 9-59 months who received a vitamin A dose in the last 6 months (%)
67. Children age 12-23 months who received most of their vaccinations in a public health facility (%)
68. Children age 12-23 months who received most of their vaccinations in a private health facility (%)
69. Prevalence of diarrhoea in the 2 weeks preceding the survey (%)
70. Children with diarrhoea in the 2 weeks preceding the survey who received oral rehydration salts (ORS) (%)
71. Children with diarrhoea in the 2 weeks preceding the survey who received zinc (%)
72. Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%)
73. Prevalence of symptoms of acute respiratory infection (ARI) in the 2 weeks preceding the survey (%)
74. Children with fever or symptoms of ARI in the 2 weeks preceding the survey taken to a health facility or health provider (%)
75. Children under age 3 years breastfed within one hour of birth15 (%)
76. Children under age 6 months exclusively breastfed16 (%)
77. Children age 6-8 months receiving solid or semi-solid food and breastmilk16 (%)
78. Breastfeeding children age 6-23 months receiving an adequate diet16, 17  (%)
79. Non-breastfeeding children age 6-23 months receiving an adequate diet16, 17 (%)
80. Total children age 6-23 months receiving an adequate diet16, 17  (%)
81. Children under 5 years who are stunted (height-for-age)18 (%)
82. Children under 5 years who are wasted (weight-for-height)18 (%)
83. Children under 5 years who are severely wasted (weight-for-height)19 (%)
84. Children under 5 years who are underweight (weight-for-age)18 (%)
85. Children under 5 years who are overweight (weight-for-height)20 (%)
86. Women whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2)21 (%)
87. Men whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)
88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)
89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)
90. Women who have high risk waist-to-hip ratio (≥0.85) (%)
91. Men who have high risk waist-to-hip ratio (≥0.90) (%)
92. Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)
93. Non-pregnant women age 15-49 years who are anaemic (<12.0 g/dl)22 (%)
94. Pregnant women age 15-49 years who are anaemic (<11.0 g/dl)22 (%)
95. All women age 15-49 years who are anaemic22 (%)
96. All women age 15-19 years who are anaemic22 (%)
97. Men age 15-49 years who are anaemic (<13.0 g/dl)22 (%)
98. Men age 15-19 years who are anaemic (<13.0 g/dl)22 (%)
99. Blood sugar level - high (141-160 mg/dl)23 (%)
100. Blood sugar level - very high (>160 mg/dl)23 (%)
101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
102. Blood sugar level - high (141-160 mg/dl)23 (%)
103. Blood sugar level - very high (>160 mg/dl)23 (%)
104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
105. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)
106. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)
107. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)
108. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)
109. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)
110. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)
111. Ever undergone a screening test for cervical cancer (%)
112. Ever undergone a breast examination for breast cancer (%)
113. Ever undergone an oral cavity examination for oral cancer (%)
114. Ever undergone an oral cavity examination for oral cancer (%)
115. Women who have comprehensive knowledge24 of HIV/AIDS (%)
116. Men who have comprehensive knowledge24 of HIV/AIDS (%)
117. Women who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)
118. Men who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)
119. Currently married women who usually participate in three household decisions25 (%)
120. Women who worked in the last 12 months and were paid in cash (%)
121. Women owning a house and/or land (alone or jointly with others) (%)
122. Women having a bank or savings account that they themselves use (%)
123. Women having a mobile phone that they themselves use (%)
124. Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)
125. Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)
126. Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)
127. Young women age 18-29 years who experienced sexual violence by age 18 (%)
128. Women age 15 years and above who use any kind of tobacco (%)
129. Men age 15 years and above who use any kind of tobacco (%)
130. Women age 15 years and above who consume alcohol (%)
131. Men age 15 years and above who consume alcohol (%)
66. Children age 9-35 months who received a vitamin A dose in the last 6 months (%)
df["Obesity"].mean()
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Obesity'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    df["Obesity"].mean()
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Obesity'
cols = ["nfhs5_urban", "nfhs5_rural", "nfhs5_total", "nfhs4_total"]
for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

    

df.info()
<class 'pandas.DataFrame'>
RangeIndex: 4847 entries, 0 to 4846
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   state        4847 non-null   str    
 1   state_code   4716 non-null   str    
 2   indicator    4847 non-null   str    
 3   nfhs5_urban  4693 non-null   float64
 4   nfhs5_rural  4635 non-null   float64
 5   nfhs5_total  4799 non-null   float64
 6   nfhs4_total  3660 non-null   float64
dtypes: float64(4), str(3)
memory usage: 265.2 KB
KeyboardInterrupt
df.isnull().sum()
df.isnull().sum()
state             0
state_code      131
indicator         0
nfhs5_urban     154
nfhs5_rural     212
nfhs5_total      48
nfhs4_total    1187
dtype: int64
#step 2 done
#step 3 handling missing values
obesity_gap = obesity.pivot(
    index="state",
    columns="indicator",
    values="nfhs5_total"
)
obesity_gap.head()
indicator                  88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)  89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)
state                                                                                                                                              
Andaman & Nicobar Islands                                               38.1                                                           45.3        
Andhra Pradesh                                                          36.3                                                           31.1        
Arunachal Pradesh                                                       23.9                                                           27.6        
Assam                                                                   15.2                                                           16.2        
Bihar                                                                   15.9                                                           14.7        
obesity_gap["Gender_Obesity_Gap"] = (
    obesity_gap.iloc[:, 0] -
    obesity_gap.iloc[:, 1]
)
obesity_gap.head()
indicator                  88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)  ...  Gender_Obesity_Gap
state                                                                                     ...                    
Andaman & Nicobar Islands                                               38.1              ...                -7.2
Andhra Pradesh                                                          36.3              ...                 5.2
Arunachal Pradesh                                                       23.9              ...                -3.7
Assam                                                                   15.2              ...                -1.0
Bihar                                                                   15.9              ...                 1.2

[5 rows x 3 columns]
#phase 1 done
#phase 2
import matplotlib.pyplot as plt
import numpy as np
children_anaemia = df[
    df["indicator"].str.contains(
        "Children age 6-59 months who are anaemic",
        case=False
    )
]
children_anaemia.head()
                         state state_code  ... nfhs5_total  nfhs4_total
91                       India        NaN  ...        67.1         58.6
222  Andaman & Nicobar Islands         AN  ...        40.0         49.0
353             Andhra Pradesh         AP  ...        63.2         58.6
484          Arunachal Pradesh         AR  ...        56.6         54.2
615                      Assam         AS  ...        68.4         35.7

[5 rows x 7 columns]
women_obesity = df[
    df["indicator"].str.contains(
        "Women who are overweight or obese",
        case=False
    )
]
women_obesity.head()
                         state state_code  ... nfhs5_total  nfhs4_total
87                       India        NaN  ...        24.0         20.6
218  Andaman & Nicobar Islands         AN  ...        38.1         31.8
349             Andhra Pradesh         AP  ...        36.3         33.2
480          Arunachal Pradesh         AR  ...        23.9         18.8
611                      Assam         AS  ...        15.2         13.2

[5 rows x 7 columns]
children_anaemia = children_anaemia[
    ["state", "nfhs5_total"]
]
children_anaemia.columns = [
    "state",
    "Children_Anaemia"
]
women_obesity = women_obesity[
    ["state", "nfhs5_total"]
]

women_obesity.columns = [
    "state",
    "Women_Obesity"
]
SyntaxError: multiple statements found while compiling a single statement
women_obesity = women_obesity[
    ["state", "nfhs5_total"]
]
women_obesity.columns = [
    "state",
    "Women_Obesity"
]
KeyboardInterrupt
KeyboardInterrupt
corr_df = pd.merge(
    children_anaemia,
    women_obesity,
    on="state"
)
'
corr_df.head()
                       state  Children_Anaemia  Women_Obesity
0                      India              67.1           24.0
1  Andaman & Nicobar Islands              40.0           38.1
2             Andhra Pradesh              63.2           36.3
3          Arunachal Pradesh              56.6           23.9
4                      Assam              68.4           15.2
corr_df.corr(numeric_only=True)
                  Children_Anaemia  Women_Obesity
Children_Anaemia          1.000000      -0.203419
Women_Obesity            -0.203419       1.000000
corr = corr_df[
    ["Children_Anaemia",
     "Women_Obesity"]
].corr()

print(corr)
SyntaxError: multiple statements found while compiling a single statement
corr = corr_df[
    ["Children_Anaemia",
     "Women_Obesity"]
].corr()
print(corr)
                  Children_Anaemia  Women_Obesity
Children_Anaemia          1.000000      -0.203419
Women_Obesity            -0.203419       1.000000
#same
#task 2
men_hyper = df[
    df["indicator"].str.contains(
        "107.",
        regex=False
    )
]
women_hyper = df[
    df["indicator"].str.contains(
        "110.",
        regex=False
    )
]
]
men_hyper = men_hyper[
    ["state",
     "nfhs5_total"]
]

men_hyper.columns = [
    "state",
    "Men"
]
women_hyper = women_hyper[
    ["state",
     "nfhs5_total"]
]
women_hyper.columns = [
    "state",
    "Women"
]
hyper = pd.merge(
    men_hyper,
    women_hyper,
    on="state"
)
hyper["Average"] = (
    hyper["Men"] +
    hyper["Women"]
)/2
top10 = hyper.sort_values(
    "Average",
    ascending=False
).head(10)
top10.plot(
    x="state",
    y=["Men","Women"],
    kind="bar",
    figsize=(12,6)
)

plt.title("Top 10 States by Hypertension")
plt.ylabel("Percentage")
plt.xticks(rotation=45)

plt.show()
SyntaxError: multiple statements found while compiling a single statement
top10.plot(
    x="state",
    y=["Men","Women"],
    kind="bar",
    figsize=(12,6)
)
<Axes: xlabel='state'>

plt.title("Top 10 States by Hypertension")
Text(0.5, 1.0, 'Top 10 States by Hypertension')
plt.ylabel("Percentage")
Text(0, 0.5, 'Percentage')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [Text(0, 0, 'Sikkim'), Text(1, 0, 'Punjab'), Text(2, 0, 'Kerala'), Text(3, 0, 'Arunachal Pradesh'), Text(4, 0, 'Telangana'), Text(5, 0, 'NCT Delhi'), Text(6, 0, 'Manipur'), Text(7, 0, 'Chandigarh'), Text(8, 0, 'Andaman & Nicobar Islands'), Text(9, 0, 'Tamil Nadu')])
plt.show()
#task 3
women_anaemia = df[
    df["indicator"].str.contains(
        "Women age 15-49 years who are anaemic",
        case=False
    )
]
women_obesity = df[
    df["indicator"].str.contains(
        "Women who are overweight or obese",
        case=False
    )
]
women_anaemia = women_anaemia[
    ["state",
     "state_code",
     "nfhs5_total"]
]
women_anaemia.columns = [
    "state",
    "code",
    "Anaemia"
]
women_obesity = women_obesity[
    ["state",
     "nfhs5_total"]
]
women_obesity.columns = [
    "state",
    "Obesity"
]
scatter_df = pd.merge(
    women_anaemia,
    women_obesity,
    on="state"
)
plt.figure(figsize=(10,8))
<Figure size 1000x800 with 0 Axes>
plt.scatter(
    scatter_df["Anaemia"],
    scatter_df["Obesity"]
)
<matplotlib.collections.PathCollection object at 0x00000225AD17A510>
for i in range(len(scatter_df)):
    plt.text(
        scatter_df["Anaemia"].iloc[i],
        scatter_df["Obesity"].iloc[i],
        scatter_df["code"].iloc[i],
        fontsize=8
    )

    
Text(57.2, 24.0, 'nan')
Text(52.2, 24.0, 'nan')
Text(57.0, 24.0, 'nan')
Text(57.6, 38.1, 'AN')
Text(53.7, 38.1, 'AN')
Text(57.5, 38.1, 'AN')
Text(59.0, 36.3, 'AP')
Text(53.7, 36.3, 'AP')
Text(58.8, 36.3, 'AP')
Text(40.8, 23.9, 'AR')
Text(27.9, 23.9, 'AR')
Text(40.3, 23.9, 'AR')
Text(66.4, 15.2, 'AS')
Text(54.2, 15.2, 'AS')
Text(65.9, 15.2, 'AS')
Text(63.6, 15.9, 'BR')
Text(63.1, 15.9, 'BR')
Text(63.5, 15.9, 'BR')
Text(60.1, 44.0, 'CH')
Text(nan, 44.0, 'CH')
Text(60.3, 44.0, 'CH')
Text(61.2, 14.1, 'CT')
Text(51.8, 14.1, 'CT')
Text(60.8, 14.1, 'CT')
Text(62.6, 26.8, 'DD')
Text(60.7, 26.8, 'DD')
Text(62.5, 26.8, 'DD')
Text(50.2, 41.3, 'DL')
Text(42.2, 41.3, 'DL')
Text(49.9, 41.3, 'DL')
Text(38.9, 36.1, 'GA')
Text(41.0, 36.1, 'GA')
Text(39.0, 36.1, 'GA')
Text(65.1, 22.6, 'GJ')
Text(62.6, 22.6, 'GJ')
Text(65.0, 22.6, 'GJ')
Text(53.4, 30.4, 'HP')
Text(42.2, 30.4, 'HP')
Text(53.0, 30.4, 'HP')
Text(60.6, 33.1, 'HR')
Text(56.5, 33.1, 'HR')
Text(60.4, 33.1, 'HR')
Text(65.7, 11.9, 'JH')
Text(56.8, 11.9, 'JH')
Text(65.3, 11.9, 'JH')
Text(67.3, 29.3, 'JK')
Text(44.1, 29.3, 'JK')
Text(65.9, 29.3, 'JK')
Text(47.8, 30.1, 'KA')
Text(45.7, 30.1, 'KA')
Text(47.8, 30.1, 'KA')
Text(36.5, 38.1, 'KL')
Text(31.4, 38.1, 'KL')
Text(36.3, 38.1, 'KL')
Text(26.0, 33.5, 'LD')
Text(20.9, 33.5, 'LD')
Text(25.8, 33.5, 'LD')
Text(93.7, 28.3, 'LH')
Text(78.1, 28.3, 'LH')
Text(92.8, 28.3, 'LH')
Text(54.5, 23.4, 'MH')
Text(45.7, 23.4, 'MH')
Text(54.2, 23.4, 'MH')
Text(54.4, 11.5, 'ML')
Text(45.0, 11.5, 'ML')
Text(53.8, 11.5, 'ML')
Text(29.3, 34.1, 'MN')
Text(32.4, 34.1, 'MN')
Text(29.4, 34.1, 'MN')
Text(54.7, 16.6, 'MP')
Text(52.9, 16.6, 'MP')
Text(54.7, 16.6, 'MP')
Text(34.8, 24.2, 'MZ')
Text(34.0, 24.2, 'MZ')
Text(34.8, 24.2, 'MZ')
Text(29.3, 14.4, 'NL')
Text(22.2, 14.4, 'NL')
Text(28.9, 14.4, 'NL')
Text(64.4, 23.0, 'OR')
Text(61.8, 23.0, 'OR')
Text(64.3, 23.0, 'OR')
Text(58.8, 40.8, 'PB')
Text(51.7, 40.8, 'PB')
Text(58.7, 40.8, 'PB')
Text(55.5, 46.2, 'PY')
Text(42.5, 46.2, 'PY')
Text(55.1, 46.2, 'PY')
Text(54.7, 12.9, 'RJ')
Text(46.3, 12.9, 'RJ')
Text(54.4, 12.9, 'RJ')
Text(42.1, 34.7, 'SK')
Text(40.7, 34.7, 'SK')
Text(42.1, 34.7, 'SK')
Text(57.8, 30.1, 'TG')
Text(53.2, 30.1, 'TG')
Text(57.6, 30.1, 'TG')
Text(53.6, 40.4, 'TN')
Text(48.3, 40.4, 'TN')
Text(53.4, 40.4, 'TN')
Text(67.4, 21.5, 'TR')
Text(61.5, 21.5, 'TR')
Text(67.2, 21.5, 'TR')
Text(50.6, 21.3, 'UP')
Text(45.9, 21.3, 'UP')
Text(50.4, 21.3, 'UP')
Text(42.4, 29.7, 'UT')
Text(46.4, 29.7, 'UT')
Text(42.6, 29.7, 'UT')
Text(71.7, 22.7, 'WB')
Text(62.3, 22.7, 'WB')
Text(71.4, 22.7, 'WB')
plt.xlabel("Percentage of Anaemic Women")
Text(0.5, 0, 'Percentage of Anaemic Women')
plt.ylabel("Percentage of Obese Women")
Text(0, 0.5, 'Percentage of Obese Women')
plt.title("Anaemia vs Obesity")
Text(0.5, 1.0, 'Anaemia vs Obesity')
plt.grid(True)
plt.show()
#phase3
import follium
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    import follium
ModuleNotFoundError: No module named 'follium'
import folium
india_map = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)
india_map
<folium.folium.Map object at 0x00000225AB797A10>
india_geo = "india_states.geojson"
women_obesity = df[
    df["indicator"].str.contains(
        "Women who are overweight or obese",
        case=False
    )
]
women_obesity = women_obesity[
    ["state", "nfhs5_total"]
]
women_obesity.columns = [
    "state",
    "Obesity"
]
folium.Choropleth(
    geo_data=india_geo,
    data=women_obesity,
    columns=["state", "Obesity"],
    key_on="feature.properties.ST_NM",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Obesity (%)"
).add_to(india_map)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1683, in __init__
    self.geojson = GeoJson(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 733, in __init__
    self.data = self.process_data(data)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 770, in process_data
    with open(data) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'india_states.geojson'
india_geo = r"C:\Users\Lenovo\Downloads\NFHS-5-master\NFHS-5-master\india_state.geojson"
  
folium.Choropleth(
    geo_data=india_geo,
    data=women_obesity,
    columns=["state", "Obesity"],
    key_on="feature.properties.ST_NM",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Obesity (%)"
).add_to(india_map)
  
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1683, in __init__
    self.geojson = GeoJson(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 738, in __init__
    self._validate_function(style_function, "style_function")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 813, in _validate_function
    if not callable(func) or not isinstance(func(test_feature), dict):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1663, in style_function
    color, opacity = color_scale_fun(x)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1635, in color_scale_fun
    raise ValueError(f"key_on `{key_on!r}` not found in GeoJSON.")
ValueError: key_on `'properties.ST_NM'` not found in GeoJSON.
import json
with open("india_states.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

    
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    with open("india_states.geojson", "r", encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'india_states.geojson'
with open("india_states.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)
with open("india_states.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)
    
SyntaxError: invalid syntax
with open("india_states.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    with open("india_states.geojson", "r", encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'india_states.geojson'
import os
print(os.getcwd())
C:\Users\Lenovo\Documents
print(os.getcwd())
C:\Users\Lenovo\Documents
print(os.listdir())
['Custom Office Templates', 'desktop.ini', 'My Music', 'My Pictures', 'My Videos', 'SIC_RISHA', 'WindowsPowerShell']
os.chdir(r"C:\Users\Lenovo\Documents\SIC_RISHA\Daily work\Day11")
KeyboardInterrupt
print(os.getcwd())
C:\Users\Lenovo\Documents\SIC_RISHA\Daily work\Day11
with open("india_state.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

    
print(type(geo))
<class 'dict'>
print(geo.keys())
dict_keys(['type', 'crs', 'features'])
print(geo["features"][0]["properties"])
{'ID_0': 105, 'ISO': 'IND', 'NAME_0': 'India', 'ID_1': 1, 'NAME_1': 'Andaman and Nicobar', 'NL_NAME_1': None, 'VARNAME_1': 'Andaman & Nicobar Islands|Andaman et Nicobar|Iihas de Andama e Nicobar|Inseln Andamanen und Nikobare', 'TYPE_1': 'Union Territor', 'ENGTYPE_1': 'Union Territory'}
print(total_df.index.tolist()[:10])
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    print(total_df.index.tolist()[:10])
NameError: name 'total_df' is not defined
print(df.head())
   state state_code  ... nfhs5_total  nfhs4_total
0  India        NaN  ...        71.8         68.8
1  India        NaN  ...        26.5         28.6
2  India        NaN  ...      1020.0        991.0
3  India        NaN  ...       929.0        919.0
4  India        NaN  ...        89.1         79.7

[5 rows x 7 columns]
m = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)

folium.Choropleth(
    geo_data=geo,
    data=total_df,
    columns=[total_df.index, "Obesity_Women"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Women Obesity (%)"
).add_to(m)
Traceback (most recent call last):
  File "<pyshell#122>", line 4, in <module>
    data=total_df,
NameError: name 'total_df' is not defined

folium.Choropleth(
    geo_data=geo,
    data=total_df,
    columns=[df.index, "Obesity_Women"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Women Obesity (%)"
).add_to(m)
Traceback (most recent call last):
  File "<pyshell#123>", line 4, in <module>
    data=total_df,
NameError: name 'total_df' is not defined

folium.Choropleth(
    geo_data=geo,
    data=df,
    columns=[total_df.index, "Obesity_Women"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Women Obesity (%)"
).add_to(m)
Traceback (most recent call last):
  File "<pyshell#124>", line 5, in <module>
    columns=[total_df.index, "Obesity_Women"],
NameError: name 'total_df' is not defined

folium.Choropleth(
    geo_data=geo,
    data=df,
    columns=[df.index, "Obesity_Women"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Women Obesity (%)"
).add_to(m)
  
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Obesity_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#125>", line 2, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1577, in __init__
    color_data = data.set_index(columns[0])[columns[1]].to_dict()  # type: ignore
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Obesity_Women'
print(women_obesity.head())
                         state  Obesity
87                       India     24.0
218  Andaman & Nicobar Islands     38.1
349             Andhra Pradesh     36.3
480          Arunachal Pradesh     23.9
611                      Assam     15.2
women_obesity["state"] = women_obesity["state"].replace({
    "Andaman & Nicobar Islands": "Andaman and Nicobar",
    "Dadra & Nagar Haveli and Daman & Diu":
        "Dadra and Nagar Haveli and Daman and Diu",
    "NCT Delhi": "Delhi",
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Odisha": "Orissa"
})
m = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)
folium.Choropleth(
    geo_data=geo,
    data=women_obesity,
    columns=["state", "Obesity"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Women Obesity (%)"
).add_to(m)
<folium.features.Choropleth object at 0x00000225AB5316E0>
m
<folium.folium.Map object at 0x00000225B4742490>
blood_sugar = df[
    df["indicator"].str.contains(
        "high or very high",
        case=False
    )
]

blood_sugar = blood_sugar.iloc[::2]
blood_sugar = blood_sugar[
    ["state", "nfhs5_total"]
]

blood_sugar.columns = [
    "state",
    "Blood_Sugar"
]
anaemia = df[
    df["indicator"].str.contains(
        "All women age 15-49 years who are anaemic",
        case=False
    )
]
anaemia = anaemia[
    ["state", "nfhs5_total"]
]
anaemia.columns = [
    "state",
    "Anaemia"
]
popup_df = pd.merge(
    blood_sugar,
    anaemia,
    on="state"
)
state_locations = {
    "Andhra Pradesh": [16.5062, 80.6480],
    "Arunachal Pradesh": [27.0844, 93.6053],
    "Assam": [26.1445, 91.7362],
    "Bihar": [25.5941, 85.1376],
    "Chhattisgarh": [21.2514, 81.6296],
    "Goa": [15.4909, 73.8278],
    "Gujarat": [23.0225, 72.5714],
    "Haryana": [30.7333, 76.7794],
    "Himachal Pradesh": [31.1048, 77.1734],
    "Jharkhand": [23.3441, 85.3096],
    "Karnataka": [12.9716, 77.5946],
    "Kerala": [8.5241, 76.9366],
    "Madhya Pradesh": [23.2599, 77.4126],
    "Maharashtra": [19.0760, 72.8777],
    "Manipur": [24.8170, 93.9368],
    "Meghalaya": [25.5788, 91.8933],
    "Mizoram": [23.7271, 92.7176],
    "Nagaland": [25.6751, 94.1086],
    "Odisha": [20.2961, 85.8245],
    "Punjab": [30.7333, 76.7794],
    "Rajasthan": [26.9124, 75.7873],
    "Sikkim": [27.3389, 88.6065],
    "Tamil Nadu": [13.0827, 80.2707],
    "Telangana": [17.3850, 78.4867],
    "Tripura": [23.8315, 91.2868],
    "Uttar Pradesh": [26.8467, 80.9462],
...     "Uttarakhand": [30.3165, 78.0322],
...     "West Bengal": [22.5726, 88.3639],
...     "Delhi": [28.6139, 77.2090]
... }
>>> for _, row in popup_df.iterrows():
... 
...     if row["state"] in state_locations:
... 
...         folium.CircleMarker(
...             location=state_locations[row["state"]],
...             radius=8,
...             color="blue",
...             fill=True,
...             fill_color="red",
...             fill_opacity=0.7,
...             popup=f"""
...             <b>State:</b> {row['state']}<br>
...             <b>High Blood Sugar:</b> {row['Blood_Sugar']}%<br>
...             <b>Anaemia:</b> {row['Anaemia']}%
...             """
...         ).add_to(m)
... 
...         
<folium.vector_layers.CircleMarker object at 0x00000225ACFBD400>
<folium.vector_layers.CircleMarker object at 0x00000225B4742C10>
<folium.vector_layers.CircleMarker object at 0x00000225B4742FD0>
<folium.vector_layers.CircleMarker object at 0x00000225AB531BA0>
<folium.vector_layers.CircleMarker object at 0x00000225ACEBCFC0>
<folium.vector_layers.CircleMarker object at 0x00000225A9CA4A70>
<folium.vector_layers.CircleMarker object at 0x00000225ACE66AD0>
<folium.vector_layers.CircleMarker object at 0x00000225ACE66E00>
<folium.vector_layers.CircleMarker object at 0x00000225B772C450>
<folium.vector_layers.CircleMarker object at 0x00000225B772C650>
<folium.vector_layers.CircleMarker object at 0x00000225ACF40D70>
<folium.vector_layers.CircleMarker object at 0x00000225ACF41040>
<folium.vector_layers.CircleMarker object at 0x00000225ACE69FD0>
<folium.vector_layers.CircleMarker object at 0x00000225ACE6ACF0>
<folium.vector_layers.CircleMarker object at 0x00000225ACE765B0>
<folium.vector_layers.CircleMarker object at 0x00000225B77204D0>
<folium.vector_layers.CircleMarker object at 0x00000225B7720710>
<folium.vector_layers.CircleMarker object at 0x00000225ACED6F10>
<folium.vector_layers.CircleMarker object at 0x00000225ACED71D0>
<folium.vector_layers.CircleMarker object at 0x00000225B771C370>
<folium.vector_layers.CircleMarker object at 0x00000225B771C190>
<folium.vector_layers.CircleMarker object at 0x00000225B771C690>
<folium.vector_layers.CircleMarker object at 0x00000225B771C2D0>
<folium.vector_layers.CircleMarker object at 0x00000225B771C910>
<folium.vector_layers.CircleMarker object at 0x00000225B771CA50>
<folium.vector_layers.CircleMarker object at 0x00000225B771C550>
<folium.vector_layers.CircleMarker object at 0x00000225B771CCD0>
<folium.vector_layers.CircleMarker object at 0x00000225B771C7D0>
>>> m
<folium.folium.Map object at 0x00000225B4742490>
>>> m.save("india_health_map.html")
>>> 
>>> import webbrowser
>>> m.save("india_health_map.html")
>>> webbrowser.open("india_health_map.html")
True
