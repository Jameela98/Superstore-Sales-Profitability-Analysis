#!/usr/bin/env python
# coding: utf-8

# ## Superstore Sales & Profitability Analysis
# 
# Understanding What Drives Profit and Loss
# 

# ## 1. Import Libraries

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## 2. Load  and  Explore Data

# In[2]:


df = pd.read_excel("C:/Users/jamee/OneDrive/Desktop/Tasks/Superstore Dataset/Superstore_Dirty.xlsx")


# In[3]:


df.head(5)


# In[4]:


df.info()


# In[5]:


df.describe()


# ## 3. Data Cleaning

# In[6]:


df.drop(columns='Postal Code',axis=1,inplace=True)


# In[7]:


df.info()


# In[8]:


df["Order Date"]=pd.to_datetime(df["Order Date"],errors="coerce")
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors="coerce")


# In[9]:


df.duplicated().sum()


# In[10]:


df.drop_duplicates(inplace=True)


# In[11]:


df.isna().sum()


# In[12]:


df[df.duplicated(subset=['Row ID','Order ID','Ship Date','Ship Mode','Customer ID','Customer Name','Segment','City','Sales','Profit','Product ID']
)].count()


# In[13]:


df[df.duplicated(subset='Row ID')].head(20)


# In[14]:


df[df['Row ID'].duplicated()]


# In[15]:


df.sort_values(by='Order Date',na_position='last',inplace=True)
df.drop_duplicates(subset='Row ID',keep='first',inplace=True)


# In[16]:


df.drop(columns='Row ID',axis=1,inplace=True)


# In[17]:


df.duplicated().sum()


# In[18]:


df.drop_duplicates(inplace=True)


# In[19]:


df.duplicated().sum()


# In[20]:


df.isna().sum()


# In[21]:


df[df['Order Date'].isna() & df['Sales'].isna() & df['Profit'].isna()].count()


# In[22]:


df["Sales"].describe()


# In[23]:


df["Sales"].mode()


# In[24]:


df["Sales"].median()


# In[25]:


df["Sales"].fillna(df["Sales"].median(), inplace=True)


# In[26]:


df["Profit"].describe()


# In[27]:


df["Profit"].mode()


# In[28]:


df["Profit"].fillna(df["Profit"].median(), inplace=True)


# In[29]:


df.isna().sum()


# In[30]:


df.count()


# In[31]:


df.groupby('Order ID')['Order Date'].agg(total_rows='size',valid_dates='count')


# In[32]:


check = df.groupby('Order ID')['Order Date'].agg(total_rows='size',valid_dates='count')

check[check['total_rows'] > check['valid_dates']]


# In[33]:


df['Order Date'] = (df.groupby('Order ID')['Order Date'].transform(lambda x: x.ffill().bfill()))


# In[34]:


df['Order Date'].isna().sum()


# In[35]:


df.dropna(subset='Order Date',inplace=True)


# In[36]:


df.isna().sum()


# In[37]:


df.head()


# In[38]:


df.info()


# ## 4. Feature Engineering

# In[39]:


df["Year (Order)"] = df["Order Date"].dt.year.astype(int)
df["Month (Order)"] = df["Order Date"].dt.month

df["Year (Ship)"] = df["Ship Date"].dt.year.astype(int)
df["Month (Ship)"] = df["Ship Date"].dt.month


# ## 5. Exploratory Analysis
# 
# The exploratory analysis focuses on identifying trends in sales and profit, evaluating regional and category performance, understanding customer behavior, and assessing the impact of discounts on profitability.
# 
# ### A) Time Analysis

# In[40]:


monthly_year_order=df.groupby(['Year (Order)', 'Month (Order)'])['Sales'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_year_order,x='Month (Order)',y='Sales',hue='Year (Order)',marker='o',palette='viridis')
plt.title("Ordering Over Month")
plt.xlabel("Month (Order)")
plt.ylabel("Sales")
plt.show()


# In[41]:


monthly_year_ship=df.groupby(['Year (Ship)', 'Month (Ship)'])['Sales'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_year_ship,x='Month (Ship)',y='Sales',hue='Year (Ship)',marker='o',palette='viridis')
plt.title("Shipping Over Month")
plt.xlabel("Month (Ship)")
plt.ylabel("Sales")
plt.show()


# In[42]:


sales_year_order=df.groupby('Year (Order)')['Sales'].sum()/1000
sales_year_order=sales_year_order.reset_index()

profit_year_order=df.groupby('Year (Order)')['Profit'].sum()/1000
profit_year_order=profit_year_order.reset_index()

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
sns.barplot(x='Year (Order)',y='Sales',data=sales_year_order,ci=None,)
plt.title("Yearly Ordering Sales")
plt.xlabel("Year (Order)")
plt.ylabel("Sales $ (Thaousnd)")


plt.subplot(1,2,2)
sns.barplot(x='Year (Order)',y='Profit',data=profit_year_order,ci=None,)
plt.title("Yearly Ordering Profit")
plt.xlabel("Year (Order)")
plt.ylabel("Profit $ (Thaousnd)")

plt.tight_layout()
plt.show()


# In[43]:


sales_year_ship=df.groupby('Year (Ship)')['Sales'].sum()/1000
sales_year_ship=sales_year_ship.reset_index()

profit_year_ship =df.groupby('Year (Ship)')['Profit'].sum()/1000
profit_year_ship =profit_year_ship.reset_index()


plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
sns.barplot(x='Year (Ship)',y='Sales',data=sales_year_ship,ci=None,)
plt.title("Yearly shipping Sales")
plt.xlabel("Year (Ship)")
plt.ylabel("Sales $ (Thaousnd)")


plt.subplot(1,2,2)
sns.barplot(x='Year (Ship)',y='Profit',data=profit_year_ship ,ci=None,)
plt.title("Yearly Shipping Profit")
plt.xlabel("Year (Ship)")
plt.ylabel("Profit $ (Thaousnd)")


plt.tight_layout()
plt.show()


# ### B) Shipping Analysis

# In[44]:


plt.figure(figsize=(8,6))
sns.barplot(x='Ship Mode',y='Profit',data=df,estimator=sum,ci=None)
plt.title("Profitability by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Profit")
plt.show()


# In[45]:


region_mode_profit=df.groupby(['Region','Ship Mode'])['Profit'].mean().reset_index()

plt.figure(figsize=(10,8))
sns.barplot(x='Region',y='Profit',data=region_mode_profit,hue='Ship Mode')
plt.title("Average Profit by Region and Ship Mode")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()


# ### C) Category Analysis

# In[46]:


cat=df.groupby("Category")[["Sales","Profit"]].sum().reset_index()
cat['Sales']=cat['Sales']/1000
cat['Profit']=cat['Profit']/1000


# In[47]:


plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
sns.barplot(x='Category',y='Sales',data=cat)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($ Thaousnd)")

plt.subplot(1,2,2)
sns.barplot(x='Category',y='Profit',data=cat)
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit ($ Thaousnd)")

plt.tight_layout()
plt.show()


# In[48]:


subcat = df.groupby("Sub-Category")["Profit"].sum().sort_values()

subcat.plot(kind="barh", figsize=(10,6))

plt.title("Profit by Sub-Category")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")
plt.show()


# ### D) Region Analysis

# In[49]:


plt.figure(figsize=(8,6))
sns.barplot(x='Region',y='Profit',data=df,ci=None,estimator=sum)
plt.title("Profit by Region")
plt.xlabel('Region')
plt.ylabel("Profit")
plt.show()


# In[50]:


cat_region = df.pivot_table(values='Profit',index='Category',columns='Region',aggfunc='sum')
cat_region
plt.figure(figsize=(10,6))

sns.heatmap(cat_region,annot=True,fmt='.0f')

plt.title("Profit by Category and Region")
plt.show()


# In[51]:


top_cities=df.groupby("City")["Sales"].sum().reset_index().sort_values(by="Sales",ascending=False).head(10)

top_cities.set_index("City").plot(kind="bar",figsize=(10,8))
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()


# ### E) Discount Analysis

# In[52]:


plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x="Discount",y="Profit",hue="Category",alpha=0.5)
plt.title("Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.show()


# In[53]:


discount_profit=df.groupby('Discount')['Profit'].mean().reset_index()

plt.figure(figsize=(8,6))
sns.lineplot(x='Discount',y='Profit',data=discount_profit,marker='v')
plt.title("Average Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()


# ### F) Product Analysis

# In[54]:


loss_products = df.groupby('Product ID')['Profit'].sum().sort_values().head(10).reset_index()
loss_products


# In[55]:


plt.figure(figsize=(12,8))
sns.barplot(x="Product ID",y='Profit',data=loss_products)
plt.title("Top 10 Loss-Making Products")
plt.xlabel("Product ID")
plt.xticks(rotation=25)
plt.ylabel("Profit $")
plt.tight_layout()
plt.show()


# In[56]:


best_products = df.groupby('Product ID')['Profit'].sum().sort_values().tail(10).reset_index()
best_products


# In[57]:


plt.figure(figsize=(12,8))
sns.barplot(x="Product ID",y='Profit',data=best_products)
plt.title("Top 10 Profitable Products")
plt.xlabel("Product ID")
plt.xticks(rotation=25)
plt.ylabel("Profit $")
plt.tight_layout()
plt.show()


# ### G) Customer Analysis

# In[58]:


top_customer=df.groupby("Customer Name")['Profit'].sum().sort_values(ascending=False).head(10)
top_customer=top_customer.reset_index()

plt.figure(figsize=(12,10))
sns.barplot(x='Customer Name',y='Profit',data=top_customer)
plt.title("Top 10 Profitable Customers")
plt.xlabel('Customer Name')
plt.xticks(rotation=30)
plt.ylabel("Profit $")
plt.show()


# ## 6) Insights summary
# 
# This section summarizes the key business findings derived from the exploratory analysis.
# 
# **1. Sales Exhibit Seasonal Trends**
# 
#  Monthly and yearly sales analysis suggests that demand vary over time, with certain periods generating stronger sales than others.
# 
#  **Recommendation**: Use historical trends to improve inventory planning and promotional activities.
# 
# **2. Sales Growth Does Not Always Lead to Higher Profit**
# 
#  Category-level analysis showed that some categories generate notable sales but contribute less to overall profit.
# 
#  **Recommendation**: Focus on product profitability in addition to sales volume when making business decisions.
# 
# **3. Profitability Varies Across Product Sub-Categories**
# 
#  Some sub-categories consistently perform better than others in terms of profit generation.
# 
#  **Recommendation**: Increase focus on high-performing sub-categories and reassess the strategy for underperforming ones.
# 
# **4. Regional Performance Varies Significantly**
# 
#  Profitability differs across regions\cities, indicating that some regions perform much better than others.
# 
#  **Recommendation**: Investigate underperforming regions\cities and identify factors affecting their profitability.
# 
# **5. High Discounts Negatively Impact Profitability**
# 
#  Analysis of discount and profit show a strong negative relationship between the two variables. Orders with higher discounts tend to generate lower profits and may even result in losses.
# 
#  **Recommendation**: Implement a more controlled discount strategy and evaluate the effectiveness of high-discount campaigns.
# 
# **6. A Small Number of Products Drive Losses**
# 
#  The analysis identified several products that consistently generate negative profits.
# 
#  **Recommendation**: Review pricing, discount policies, and operational costs associated with loss-making products.
# 
# **7. Profit Contribution Is Concentrated Among a Limited Number of Customers**
# 
#  A relatively small group of customers contributes a significant share of total profit.
# 
#  **Recommendation**: Develop retention strategies and loyalty programs for high-value customers.

# ## Conclusion
# 
# This analysis of the Superstore dataset helped uncover the main drivers behind the company’s profitability.
# 
# While sales show steady growth over time, profit is not always aligned with sales performance. The analysis clearly shows that discount strategy plays a critical role in overall profitability, where higher discounts often lead to reduced profits or even losses.
# 
# In addition, performance varies significantly across categories, regions, and products, highlighting that not all sales contribute equally to business success. A small group of products and customers has a strong influence on overall profit, which indicates both opportunity and risk in concentration.
# 
# Overall, the results suggest that improving discount policies, optimizing the product mix, and focusing on high-value customers can significantly enhance profitability.
# 
