import numpy as np
import pandas as pd

#Reading the DataSet
data_set = pd.read_csv("india_phone_preference.csv")

#Handling missing data
data_set.fillna(0, inplace=True)

print('\n')

#Gender Meta Data - Male, Females and Others
male_data = (data_set['Gender'] == 'Male').sum() 
male_percentage = (male_data/100000)*100
female_data = (data_set['Gender'] == 'Female').sum() 
female_percentage = (female_data/100000)*100
other_data = (data_set['Gender'] == 'Other').sum()
other_percentage = (other_data/100000)*100

print("--- Gender Meta Data - Male, Females and Others ---")
# print("Male Orders:", male_data, "In Percentage:", f'{male_percentage:.2f}%')
# print("Female Orders:", female_data, "In Percentage:", f'{female_percentage:.2f}%')
# print("Other's Orders:", other_data, "In Percentage:", f'{other_percentage:.2f}%')

gender_data = {'Male Orders': [male_data], 
               'Female Orders': [female_data], 
               'Others Orders': [other_data], 
               'Male Percentage': [f'{male_percentage:.2f}%'], 
               'Female Percentage': [f'{female_percentage:.2f}%'], 
               'Others Percentage': [f'{other_percentage:.2f}%']
              }
gender_df = pd.DataFrame(gender_data)
print(gender_df)

print('\n')

#Brand Meta Data Iphone or Android
iphone_data = (data_set['Brand'] == 'iPhone').sum()
iphone_percentage = (iphone_data/100000)*100
android_data = (data_set['Brand'] == 'Android').sum()
android_percentage = (android_data/100000)*100

print("--- Brand Meta Data Iphone or Android ---")
# print("Iphone Orders:", iphone_data, "In Percentage:", f'{iphone_percentage:.2f}%')
# print("Android Orders:", android_data, "In Percentage:", f'{android_percentage:.2f}%')

brand_data = {'iPhone Orders': [iphone_data], 
              'Android Orders': [android_data],
              'iPhone Percentage': [f'{iphone_percentage:.2f}%'],
              'Android Percentage': [f'{android_percentage:.2f}%']
             }

brand_df = pd.DataFrame(brand_data)
print(brand_df)

print('\n')

#Brand Meta Data Iphone based on Gender
iphone_data_male = ((data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Male')).sum()
iphone_data_male_percentage = (iphone_data_male/100000)*100
iphone_data_female = ((data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Female')).sum()
iphone_data_female_percentage = (iphone_data_female/100000)*100
iphone_data_other = ((data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Other')).sum()
iphone_data_other_percentage = (iphone_data_other/100000)*100

print("--- Brand Meta Data Iphone based on Gender ---")
# print("Iphone Orders by Male:", iphone_data_male, "In Percentage:", f'{iphone_data_male_percentage:.2f}%')
# print("Iphone Orders by Female:", iphone_data_female, "In Percentage:", f'{iphone_data_female_percentage:.2f}%')
# print("Iphone Orders by Other's:", iphone_data_other, "In Percentage:", f'{iphone_data_other_percentage:.2f}%')

gender_iphone_data = {'iPhone Orders (Male)': [iphone_data_male],
                      'iPhone Orders (Female)': [iphone_data_female],
                      'iPhone Orders (Others)': [iphone_data_other],
                      'iPhone Male (Percentage)': [iphone_data_male_percentage],
                      'iPhone Female (Percentage)': [iphone_data_female_percentage],
                      'iPhone Others (Percentage)': [iphone_data_other_percentage]
                     }

gender_iphone_df = pd.DataFrame(gender_iphone_data)
print(gender_iphone_df)

print('\n')

#Brand Meta Data Android based on Gender
android_data_male = ((data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Male')).sum()
android_data_male_percentage = (android_data_male/100000)*100
android_data_female = ((data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Female')).sum()
android_data_female_percentage = (android_data_female/100000)*100
android_data_other = ((data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Other')).sum()
android_data_other_percentage = (android_data_other/100000)*100

print("--- Brand Meta Data Android based on Gender ---")
# print("Android Orders by Male:", android_data_male, "In Percentage:", f'{android_data_male_percentage:.2f}%')
# print("Android Orders by Female:", android_data_female, "In Percentage:", f'{android_data_female_percentage:.2f}%')
# print("Android Orders by Other's:", android_data_other, "In Percentage:", f'{android_data_other_percentage:.2f}%')

gender_android_data = {'Android Orders (Male)': [android_data_male],
                       'Android Orders (Female)': [android_data_female], 
                       'Android Orders (Others)': [android_data_other], 
                       'Android Male (Percentage)': [android_data_male_percentage], 
                       'Android Female (Percentage)': [android_data_female_percentage], 
                       'Android Others (Percentage)': [android_data_other_percentage]
                      }
gender_android_df = pd.DataFrame(gender_android_data)
print(gender_android_df)

print('\n')

#Payment mode for iPhone and Android Phones
iphone_emi_payment_mode = ((data_set['Brand'] == 'iPhone') & (data_set['Payment Mode'] == 'EMI')).sum()
iphone_emi_payment_mode_percentage = (iphone_emi_payment_mode/100000)*100
iphone_upi_payment_mode = ((data_set['Brand'] == 'iPhone') & (data_set['Payment Mode'] == 'UPI')).sum()
iphone_upi_payment_mode_percentage = (iphone_upi_payment_mode/100000)*100
iphone_cc_payment_mode = ((data_set['Brand'] == 'iPhone') & (data_set['Payment Mode'] == 'Credit Card')).sum()
iphone_cc_payment_mode_percentage = (iphone_cc_payment_mode/100000)*100
iphone_dc_payment_mode = ((data_set['Brand'] == 'iPhone') & (data_set['Payment Mode'] == 'Debit Card')).sum()
iphone_dc_payment_mode_percentage = (iphone_dc_payment_mode/100000)*100
iphone_cash_payment_mode = ((data_set['Brand'] == 'iPhone') & (data_set['Payment Mode'] == 'Cash')).sum()
iphone_cash_payment_mode_percentage = (iphone_cash_payment_mode/100000)*100

print("--- Payment mode for iPhone Phones EMI/UPI/Credit Card/Debit Card/Cash ---")
# print("Iphone Orders by EMI:", iphone_emi_payment_mode , "In Percentage:", f'{iphone_emi_payment_mode_percentage:.2f}%')
# print("Iphone Orders by UPI:", iphone_upi_payment_mode , "In Percentage:", f'{iphone_upi_payment_mode_percentage:.2f}%')
# print("Iphone Orders by Credit Card:", iphone_cc_payment_mode , "In Percentage:", f'{iphone_cc_payment_mode_percentage:.2f}%')
# print("Iphone Orders by Debit Card:", iphone_dc_payment_mode , "In Percentage:", f'{iphone_dc_payment_mode_percentage:.2f}%')
# print("Iphone Orders by Cash:", iphone_cash_payment_mode , "In Percentage:", f'{iphone_cash_payment_mode_percentage:.2f}%')

iphone_payment_mode_data = {'iPhone bought on EMI': [iphone_emi_payment_mode], 'in Percentage': [f'{iphone_emi_payment_mode_percentage:.2f}%'],
                            'iPhone bought on UPI': [iphone_upi_payment_mode], 'in Percentage': [f'{iphone_upi_payment_mode_percentage:.2f}%'],
                            'iPhone bought on Credit Card': [iphone_cc_payment_mode], 'in Percentage': [f'{iphone_cc_payment_mode_percentage:.2f}%'],
                            'iPhone bought on Debit Card': [iphone_dc_payment_mode], 'in Percentage': [f'{iphone_dc_payment_mode_percentage:.2f}%'],
                            'iPhone bought on Cash': [iphone_cash_payment_mode], 'in Percentage': [f'{iphone_cash_payment_mode_percentage:.2f}%']
                           }

iphone_payment_mode_df = pd.DataFrame(iphone_payment_mode_data)
print(iphone_payment_mode_df)
 
print('\n')

android_emi_payment_mode = ((data_set['Brand'] == 'Android') & (data_set['Payment Mode'] == 'EMI')).sum()
android_emi_payment_mode_percentage = (android_emi_payment_mode/100000)*100
android_upi_payment_mode = ((data_set['Brand'] == 'Android') & (data_set['Payment Mode'] == 'UPI')).sum()
android_upi_payment_mode_percentage = (android_upi_payment_mode/100000)*100
android_cc_payment_mode = ((data_set['Brand'] == 'Android') & (data_set['Payment Mode'] == 'Credit Card')).sum()
android_cc_payment_mode_percentage = (android_cc_payment_mode/100000)*100
android_dc_payment_mode = ((data_set['Brand'] == 'Android') & (data_set['Payment Mode'] == 'Debit Card')).sum()
android_dc_payment_mode_percentage = (android_dc_payment_mode/100000)*100
android_cash_payment_mode = ((data_set['Brand'] == 'Android') & (data_set['Payment Mode'] == 'Cash')).sum()
android_cash_payment_mode_percentage = (android_cash_payment_mode/100000)*100

print("--- Payment mode for Android Phones EMI/UPI/Credit Card/Debit Card/Cash ---")
# print("Android Orders by EMI:", android_emi_payment_mode , "In Percentage:", f'{android_emi_payment_mode_percentage:.2f}%')
# print("Android Orders by UPI:", android_upi_payment_mode , "In Percentage:", f'{android_upi_payment_mode_percentage:.2f}%')
# print("Android Orders by Credit Card:", android_cc_payment_mode , "In Percentage:", f'{android_cc_payment_mode_percentage:.2f}%')
# print("Android Orders by Debit Card:", android_dc_payment_mode , "In Percentage:", f'{android_dc_payment_mode_percentage:.2f}%')
# print("Android Orders by Cash:", android_cash_payment_mode , "In Percentage:", f'{android_cash_payment_mode_percentage:.2f}%')

android_payment_mode_data = {'Android bought on EMI': [android_emi_payment_mode], 'in Percentage': [f'{android_emi_payment_mode_percentage:.2f}%'],
                             'Android bought on UPI': [android_upi_payment_mode], 'in Percentage': [f'{android_upi_payment_mode_percentage:.2f}%'],
                             'Android bought on Credit Card': [android_cc_payment_mode], 'in Percentage': [f'{android_cc_payment_mode_percentage:.2f}%'],
                             'Android bought on Debit Card': [android_dc_payment_mode], 'in Percentage': [f'{android_dc_payment_mode_percentage:.2f}%'],
                             'Android bought on Cash': [android_cash_payment_mode], 'in Percentage': [f'{android_cash_payment_mode_percentage:.2f}%']
                            }

android_payment_mode_df = pd.DataFrame(android_payment_mode_data)
print(android_payment_mode_df)

print('\n')

#Purchase Platforms of iPhone and Android Phones
offline_purchase_of_iphone = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'iPhone')).sum()
offline_purchase_of_iphone_percentage = (offline_purchase_of_iphone/100000)*100
offline_purchase_of_iphone_male = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Male')).sum()
offline_purchase_of_iphone_male_percentage = (offline_purchase_of_iphone_male/100000)*100
offline_purchase_of_iphone_female = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Female')).sum()
offline_purchase_of_iphone_female_percentage = (offline_purchase_of_iphone_female/100000)*100
online_purchase_of_iphone = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'iPhone')).sum()
online_purchase_of_iphone_percentage = (online_purchase_of_iphone/100000)*100
online_purchase_of_iphone_male = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Male')).sum()
online_purchase_of_iphone_male_percentage = (online_purchase_of_iphone_male/100000)*100
online_purchase_of_iphone_female = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'iPhone') & (data_set['Gender'] == 'Female')).sum()
online_purchase_of_iphone_female_percentage = (online_purchase_of_iphone_female/100000)*100

print("--- Purchase Platforms of iPhone Phones Offline/Online/Male/Female ---")
# print("Iphone Orders in Offline:", offline_purchase_of_iphone , "In Percentage:", f'{offline_purchase_of_iphone_percentage:.2f}%')
# print("Iphone Orders in Offline by Male:", offline_purchase_of_iphone_male , "In Percentage:", f'{offline_purchase_of_iphone_male_percentage:.2f}%')
# print("Iphone Orders in Offline by Female:", offline_purchase_of_iphone_female , "In Percentage:", f'{offline_purchase_of_iphone_female_percentage:.2f}%')
# print("Iphone Orders in Online:", online_purchase_of_iphone , "In Percentage:", f'{online_purchase_of_iphone_percentage:.2f}%')
# print("Iphone Orders in Online by Male:", online_purchase_of_iphone_male , "In Percentage:", f'{online_purchase_of_iphone_male_percentage:.2f}%')
# print("Iphone Orders in Online by Female:", online_purchase_of_iphone_female , "In Percentage:", f'{online_purchase_of_iphone_female_percentage:.2f}%')

platform_purchase_of_iphone_data = {
    'iPhone Purchases in Offline': [offline_purchase_of_iphone], 'in Percentage': [f'{offline_purchase_of_iphone_percentage:.2f}%'],
    'iPhone Purchases in Offline (Male)': [offline_purchase_of_iphone_male], 'in Percentage': [f'{offline_purchase_of_iphone_male_percentage:.2f}%'],
    'iPhone Purchases in Offline (Female)': [offline_purchase_of_iphone_female], 'in Percentage': [f'{offline_purchase_of_iphone_female_percentage:.2f}%'],
    'iPhone Purchases in Online (Male)': [online_purchase_of_iphone_male], 'in Percentage': [f'{online_purchase_of_iphone_male_percentage:.2f}%'],
    'iPhone Purchases in Online (Female)': [online_purchase_of_iphone_female], 'in Percentage': [f'{online_purchase_of_iphone_female_percentage:.2f}%']
}

platform_purchase_of_iphone_df = pd.DataFrame(platform_purchase_of_iphone_data)
print(platform_purchase_of_iphone_df)

print('\n')

offline_purchase_of_android = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'Android')).sum()
offline_purchase_of_android_percentage = (offline_purchase_of_android/100000)*100
offline_purchase_of_android_male = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Male')).sum()
offline_purchase_of_android_male_percentage = (offline_purchase_of_android_male/100000)*100
offline_purchase_of_android_female = ((data_set['Purchase Platform'] == 'Offline') & (data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Female')).sum()
offline_purchase_of_android_female_percentage = (offline_purchase_of_android_female/100000)*100
online_purchase_of_android = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'Android')).sum()
online_purchase_of_android_percentage = (online_purchase_of_android/100000)*100
online_purchase_of_android_male = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Male')).sum()
online_purchase_of_android_male_percentage = (online_purchase_of_android_male/100000)*100
online_purchase_of_android_female = ((data_set['Purchase Platform'] == 'Online') & (data_set['Brand'] == 'Android') & (data_set['Gender'] == 'Female')).sum()
online_purchase_of_android_female_percentage = (online_purchase_of_android_female/100000)*100

print("--- Purchase Platforms of Android Phones Offline/Online/Male/Female ---")
# print("Android Orders in Offline:", offline_purchase_of_android , "In Percentage:", f'{offline_purchase_of_android_percentage:.2f}%')
# print("Android Orders in Offline by Male:", offline_purchase_of_android_male , "In Percentage:", f'{offline_purchase_of_android_male_percentage:.2f}%')
# print("Android Orders in Offline by Female:", offline_purchase_of_android_female , "In Percentage:", f'{offline_purchase_of_android_female_percentage:.2f}%')
# print("Android Orders in Online:", online_purchase_of_android , "In Percentage:", f'{online_purchase_of_android_percentage:.2f}%')
# print("Android Orders in Online by Male:", online_purchase_of_android_male , "In Percentage:", f'{online_purchase_of_android_male_percentage:.2f}%')
# print("Android Orders in Online by Female:", online_purchase_of_android_female , "In Percentage:", f'{online_purchase_of_android_female_percentage:.2f}%')

platform_purchase_of_android_data = {
    'Android Purchases in Offline': [offline_purchase_of_android], 'in Percentage': [f'{offline_purchase_of_android_percentage:.2f}%'],
    'Android Purchases in Offline (Male)': [offline_purchase_of_android_male], 'in Percentage': [f'{offline_purchase_of_android_male_percentage:.2f}%'],
    'Android Purchases in Offline (Female)': [offline_purchase_of_android_female], 'in Percentage': [f'{offline_purchase_of_android_female_percentage:.2f}%'],
    'Android Purchases in Online (Male)': [online_purchase_of_android_male], 'in Percentage': [f'{online_purchase_of_android_male_percentage:.2f}%'],
    'Android Purchases in Online (Female)': [online_purchase_of_android_female], 'in Percentage': [f'{online_purchase_of_android_female_percentage:.2f}%']
}

platform_purchase_of_android_df = pd.DataFrame(platform_purchase_of_android_data)
print(platform_purchase_of_android_df)
