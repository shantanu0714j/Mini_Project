import pandas as pd
import matplotlib.pyplot as plt

#Reading the excel file
df=pd.read_excel("Sales_Sheet2.xlsx")

#Displaying the data
print("Sales Data:")
print(df)

#KPI
total_sales=df['Amount'].sum()

print("\nTotal Sales:",total_sales)

#Sales by states
sales_by_state=df.groupby('ship-state')['Amount'].sum()

#Bar Chart

sales_by_state.plot(kind='bar',title="Sales by State")
plt.xlabel('ship-state')
plt.ylabel('Amount in lakhs')
plt.show()


#Sales By Product category
product_category_sales=df.groupby('Category')['Amount'].sum()

#Pie Chart

product_category_sales.plot(kind='pie',autopct='%1.1f%%',title="Sales By Product")
plt.ylabel("")
plt.show()  


#Sales By Gender
gender_sales=df.groupby('Gender')['Amount'].sum()

#Pie Chart
gender_sales.plot(kind='pie',autopct='%1.1f%%',title="Sales By Gender")
plt.ylabel("")
plt.show()

#Channel (App Wise sales)

sales_by_Months=df.groupby('Month')['Amount'].sum()
#Bar chart

sales_by_Months.plot(kind='bar',title="Sales by months in lakhs")
plt.ylabel("Sales")
plt.show()