Hotal_name = "Varahi Hotel"
Time_Period = (2001,2010)
items = ["Idle","Bonda","Puri"]
Idle_price = 60
Bonda_price = 70
Puri_price = 50
Idle_sold_2001_2010 = [10000,30000,60000,4500,20000,8000,7000,9000,8520,6710]
Bonda_sold_2001_2010 = [20000,40000,70000,3500,4000,6000,6000,5000,4580,5682]
Puri_slod_2001_2010 = [4564,2154,3265,9856,4578,2215,6632,4556,7889,5223]
Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]


#Annual Sales of Each Year From 2001 to 2010..
a = []
for i in range(0,10):
    a.append(Idle_price*Idle_sold_2001_2010[i] + Bonda_price * Bonda_sold_2001_2010[i] + Puri_price * Puri_slod_2001_2010[i])
    
#Storing Annual sales in Dictionary
sales_data = {}
for i in range(0,10):
    sales_data[Years[i]] = a[i]
    
#Dictionary

#print(sales_data.keys())
#print(sales_data.values())
#print(sales_data.items())
    
#print(sales_data)

#TOTAL SALES

total_sales = sum(a)
#print("Total sales of 10 years is: ",total_sales)

#AVERAGE SALES
Average_sales = sum(a)/len(sales_data)
#print("Average sales of 10 years is: ",Average_sales)

#HIGHEST SALES

p= max(sales_data,key=sales_data.get)
p1 = sales_data[p]
#print(p)
#print(p1)
#print("Maximum sales of 10 years is: ",p1,"in year of ",p)

#LOWEST SALES
#print("Minimum sales of 10 years is: ",min(sales_data.values()))
q = min(sales_data,key=sales_data.get)
q1 = sales_data[q]
#print(q)
#print(q1)
#print("Minimum sales of 10 years is: ",q1,"in year of ",q)


#SORTED DATA
#print(sorted(a))

print("Hotal Name  is",Hotal_name,". Time period of sales data is ",Time_Period[0],"to",Time_Period[1],"\n""The Items are available in Market are ",items[0],",",items[1],",",items[2],". The price of each item is ",Idle_price,",",Bonda_price,",",Puri_price,"respectively""\n","***Annual Sales in 10 Years***""\n",sales_data[2001],"sales in",Years[0],"\n",sales_data[2002],"sales in",Years[1],"\n",sales_data[2003],"sales in",Years[2],"\n",sales_data[2004],"sales in",Years[3],"\n",sales_data[2005],"sales in",Years[4],"\n",sales_data[2006],"sales in",Years[5],"\n",sales_data[2007],"sales in",Years[6],"\n",sales_data[2008],"sales in",Years[7],"\n",sales_data[2009],"sales in",Years[8],"\n",sales_data[2010],"sales in",Years[9],"\n""Total sales of 10 years is: ",total_sales,"\n""Average sales of 10 years is: ",Average_sales,"\n""Maximum sales of 10 years is: ",p1,"in year of ",p,"\n""Minimum sales of 10 years is: ",q1,"in year of ",q,"\n")


#Hotal Name  is Varahi Hotel . Time period of sales data is  2001 to 2010 
#The Items are available in Market are  Idle , Bonda , Puri . The price of each item is  60 , 70 , 50 respectively
# ***Annual Sales in 10 Years***
# 2228200 sales in 2001 
# 4707700 sales in 2002 
# 8663250 sales in 2003 
# 1007800 sales in 2004 
# 1708900 sales in 2005 
# 1010750 sales in 2006 
# 1171600 sales in 2007 
# 1117800 sales in 2008 
# 1226250 sales in 2009 
# 1061490 sales in 2010 
#Total sales of 10 years is:  23903740 
#Average sales of 10 years is:  2390374.0 
#Maximum sales of 10 years is:  8663250 in year of  2003 
#Minimum sales of 10 years is:  1007800 in year of  2004 