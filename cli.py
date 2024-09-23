import mysql.connector

#Lists out the states and counts the number of customers from those states
connect = mysql.connector.connect(user='root', password='root', host='localhost', database='FLIPCART')

cursor_ = connect.cursor()



while(1):
    print("Welcome to the Command Line Interface made by Jeremiah and Manshaa")
    print("1. Login")
    print("2. Test SQL Queries")
    print("3. Test OLAP Queries")
    print("4. Test Triggers")
    print("5. Test DB Transactions")

    a = int(input())
    if(a == 1):
        while(1):
            print("1. Customer")
            print("2. Seller")
            print("3. Delivery Agent")
            print("Press 0 if you want to go to the previous menu")
            b = int(input())
            if(b == 1):
                while(1):
                    print("1. Search Category")
                    print("2. Search Product")
                    print("3. Buy now")
                    print("4. Wallet Balance")
                    print("5. Update Wallet Balance")
                    print("6. Previous orders")
                    print("7. Cancel Order")
                    print("8. Show cart and Cart amount")
                    print("9. Show Wishlist")
                    print("10. Add to cart")
                    print("Press 0 if you want to go to the previous menu")
                    c = int(input())
                    if(c == 1):
                        sql_query = """ 
    SELECT Category.category_name, SUM(Product.product_price * Product.product_quantity) AS total_sales
    FROM Product
    INNER JOIN Category ON Product.category_id = Category.category_ID
    INNER JOIN Order_ ON Product.product_id = Order_.product_ID
    WHERE Order_.order_date
    GROUP BY Category.category_name WITH ROLLUP;
            """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    if(c == 2):
                        sql_query = """ 
    SELECT Seller.seller_name, SUM(Product.product_price * Product.product_quantity) AS total_revenue, COUNT(Order_.order_ID) AS number_of_orders
    FROM Product
    INNER JOIN Order_ ON Product.product_id = Order_.product_ID
    INNER JOIN Seller ON Order_.seller_ID = Seller.seller_ID
    GROUP BY Seller.seller_name WITH ROLLUP;
            """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    if(c == 3):
                        sql_query = """ 
    SELECT d.agent_name, COUNT(*) AS order_count
    FROM Delivery_Agent d
    JOIN Order_ o ON d.agent_ID = o.agent_id
    WHERE MONTH(o.order_date) = 3
    GROUP BY d.agent_name WITH ROLLUP;
            """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    if(c == 4):
                        sql_query = """ 
    select agent_id, count(order_id) as 'Total Orders'
    from Order_ 
    group by agent_id with rollup;
            """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    else:
                        break
            if(b == 2):
                while(1):
                    print("Press 1 if you want to run the first embedded query")
                    print("Press 2 if you want to run the second embedded query")
                    print("Press 0 if you want to go back")
                    c = int(input())
                    if(c == 1):
                        sql_query = """ 
        SELECT customer_state ,COUNT(*) FROM customer GROUP BY customer_state; 
        """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    if(c == 2):
                        sql_query = """ 
                                SELECT C.category_name, COUNT(*) as num_products_sold
                    FROM Order_ O
                    JOIN Product P ON O.product_ID = P.product_ID
                    JOIN Category C ON P.category_id = C.category_ID
                    GROUP BY C.category_name
                    ORDER BY num_products_sold DESC
                    LIMIT 5;
                                """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print(result)
                    else:
                        break
            if(b == 3):
                while(1):
                    print("Press 1 if you want to run the first Trigger")
                    print("Press 2 if you want to run the second Trigger")
                    print("Press 0 if you want to go back")
                    c = int(input())
                    if(c == 1):
                        sql_query = """ 
                        
create trigger verify_discount
before insert on Product
for each row
if new.product_discount>80 then set new.product_discount=0;
end if;//


                                """
                        cursor_.execute(sql_query)
                    if(c == 2):
                        sql_query = """ 
create trigger update_quantity
before update 
on Product
for each row
IF new.product_quantity<0 then set new.product_quantity=0;
end if; $$ 


        """
                        cursor_.execute(sql_query)
                        result = cursor_.fetchall()
                        print("result")
                    else:
                        break
            else:
                break
    else:
        break
# print(result)
cursor_.close()
connect.close()


