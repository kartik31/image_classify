import os
A=['dosa','idli','uttapam','samosa','kachori','cheela','Aloo ki tikki','baati','Bhatura','Butter chicken',
   'Biryani','Chapati','Chole bhature','Poha','Gajar ka halwa','Imarti','Jalebi','Kheer','Kulfi falooda','Makki di roti',
   'Pani puri','Paratha','Tandoori Chicken','Vada','Barfi','Dhokla','Gulab jamun','Laddu','Pav Bhaji',
   'Puri','Momo','Rasgulla','Chow mein','White rice','fried rice','Pasta','Burger','Pizza','hamburger',
   'bread','pastrie','Potato chips','apple','banana','mango','strawberry','Guava','orange','Blueberry','paneer masala',
   'Bhelpuri','Chana masala','Khandvi','Pakora','Vegetable sandwich','badam halwa']

for i in range(0,len(A)):
    #cmd="echo "+A[i]
    os.system("bin/fim A[i] -d A[i]-pics -n 1000")