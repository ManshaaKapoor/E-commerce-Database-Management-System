import mysql.connector

#Lists out the states and counts the number of customers from those states
connect = mysql.connector.connect(user='root', password='Jerry87115', host='localhost', database='FLIPCART')

cursor_ = connect.cursor()

def customer_creation():
    customer_id = int(input("Enter the id of the customer: "))
    customer_username = input("Enter the username of Customer: ")
    customer_password = input("Enter the password of Customer: ")
    customer_DOB = input("Enter the DOB of Customer: ")
    customer_phone1 = input("Enter the primary phone number of Customer: ")
    customer_phone2 = input("Enter the secondary phone number of Customer: ")
    customer_email_id = input("Enter the email of Customer: ")
    customer_city = input("Enter the city of Customer: ")
    customer_state = input("Enter the state of Customer: ")
    cursor2 = connect.cursor()
    query = "INSERT INTO customer(customer_id,customer_username,customer_password,DOB,customer_number,customer_number2,customer_email_id,customer_city,customer_state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(customer_id,customer_username,customer_password,customer_DOB,customer_phone1,customer_phone2,customer_email_id,customer_city,customer_state))
    connect.commit()
    print("Customer added successfully")

def view_categories():
    cursor2 = connect.cursor()
    query = "SELECT DISTINCT category_name from category"
    cursor_.execute(query)
    result = cursor_.fetchall()
    print("Sl No --- Category Name ")
    counter = 1
    for i in result:
        print(counter, i[0])
        counter += 1

def view_products():
    cursor2 = connect.cursor()
    query = "SELECT product_id,product_name,category_id,brand_name,product_price,product_quantity,product_discount from product"
    cursor_.execute(query)
    result = cursor_.fetchall()
    counter = 1
    for i in result:
        print("Product ID --- Product Name --- Category_id --- Brand_Name --- Product_Price --- Product_Quantity --- Product_Discount")

        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        counter += 1

def view_cart():
    cursor2 = connect.cursor()
    query = "SELECT product_id,product_name,category_id,brand_name,product_price,product_quantity,product_discount from product"
    cursor_.execute(query)
    result = cursor_.fetchall()
    counter = 1
    for i in result:
        print("Product ID --- Product Name --- Category_id --- Brand_Name --- Product_Price --- Product_Quantity --- Product_Discount")

        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        counter += 1

while(1):
    print("Submission for the Final Deadline of DBMS")
    print("Made by Jeremiah and Manshaa")
    print()
    print("Press 1 to continue")
    print("Press 0 to exit")
    a = int(input())
    while(1):
        if(a == 1):
            while(1):
                print("Press 1 if you want to enter as Customer")
                print("Press 2 if you want to enter as Seller")
                print("Press 3 if you want to enter as Delivery Agent")
                print("Press 0 to get to the Previous Menu")
                b = int(input())
                if(b == 1):
                    while(1):
                        print("Welcome to the login/signup page of Customer")
                        print("Press 1 if you want to login")
                        print("Press 2 if you want to signup")
                        print("Press 0 to get to the Previous Menu")
                        c = int(input())
                        if(c == 1):
                            id = int(input("Enter the id of the customer: "))
                            customer_username = input("Enter the username of Customer: ")
                            customer_password = input("Enter the password of Customer: ")
                            query = "SELECT customer_username,customer_password from customer where customer_id = %s"
                            cursor_.execute(query,(id,))
                            result = cursor_.fetchall()
                            #example: customer id = 1
                            # customer username = jsimonian0
                            # customer password = T8QAyBTVguz
                            if(customer_username == result[0][0] and customer_password == result[0][1]):
                                print("Welcome to Customer ",customer_username)
                                while(1):
                                    print()
                                    print("1. Change Personal Details")
                                    print("2. View Categories")
                                    print("3. View Products")
                                    print("4. View Cart")
                                    print("5. Add Products to Cart")
                                    print("6. Add Money to Wallet")
                                    print("7. Check Wallet Balance")
                                    print("8. Remove Product from Cart")
                                    print("9. View Orders")
                                    print("10. Checkout")
                                    print("11. View Delivery Status")
                                    print("12. Empty Cart")
                                    print("0. Exit")
                                    
                                    choice = int(input("Enter your choice: "))
                                    if(choice == 1):
                                        while(1):
                                            print()
                                            print("1. Change Username")
                                            print("2. Change Password")
                                            print("3. Change DOB")
                                            print("4. Change Primary Phone Number")
                                            print("5. Change Secondary Phone Number")
                                            print("6. Change Email ID")
                                            print("7. Change City")
                                            print("8. Change State")
                                            print("0. Exit")
                                            d = int(input())
                                            if(d == 1):
                                                new_username = input("Enter the new username: ")
                                                query = "UPDATE customer SET customer_username = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_username,id))
                                                connect.commit()
                                                print("Username updated successfully")
                                            if(d == 2):
                                                new_password = input("Enter the new password: ")
                                                query = "UPDATE customer SET customer_password = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_password,id))
                                                connect.commit()
                                                print("Password updated successfully")
                                            if(d == 3):
                                                new_DOB = input("Enter the new DOB: ")
                                                query = "UPDATE customer SET DOB = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_DOB,id))
                                                connect.commit()
                                                print("DOB updated successfully")
                                            if(d == 4):
                                                new_number = input("Enter the new primary phone number: ")
                                                query = "UPDATE customer SET customer_number = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_number,id))
                                                connect.commit()
                                                print("Primary phone number updated successfully")
                                            if(d == 5):
                                                new_number2 = input("Enter the new secondary phone number: ")
                                                query = "UPDATE customer SET customer_number2 = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_number2,id))
                                                connect.commit()
                                                print("Secondary phone number updated successfully")
                                            if(d == 6):
                                                new_email = input("Enter the new email: ")
                                                query = "UPDATE customer SET customer_email_id = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_email,id))
                                                connect.commit()
                                                print("Email updated successfully")
                                            if(d == 7):
                                                new_city = input("Enter the new city: ")
                                                query = "UPDATE customer SET customer_city = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_city,id))
                                                connect.commit()
                                                print("City updated successfully")
                                            if(d == 8):
                                                new_state = input("Enter the new state: ")
                                                query = "UPDATE customer SET customer_state = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_state,id))
                                                connect.commit()
                                                print("State updated successfully")
                                            if(d == 0):
                                                break
                                    if(choice == 2):
                                        #View categories
                                        view_categories()
                                    if(choice == 3):
                                        #View products
                                        view_products()
                                    if(choice == 4):
                                        #View cart
                                        view_cart()
                                    if(choice == 0):
                                        break

                                    # break
                            else:
                                print("Wrong username or password")
                        if(c == 2):
                            customer_creation()
                        if(c == 0):
                            break
                    
                if(b == 2):
                    #TODO: WORK ON SELLER
                    break

                if(b == 3):
                    #TODO: WORK ON DELIVERY AGENT
                    break
                if(b == 0):
                    break
            break
        if(a == 0):
            break
    if(a == 0):
        break
        
# while(1):
#     print("Welcome to the Command Line Interface made by Jeremiah and Manshaa")
#     print("Press 1 if you want to continue")
#     print("Press 0 if you want to exit")
#     a = int(input())
#     if(a == 1):
#         while(1):
#             print("Press 1 if you want to run OLAP queries")
#             print("Press 2 if you want to embedded queries")
#             print("Press 3 if you want to run Trigger queries")
#             print("Press 0 if you want to go to the previous menu")
#             b = int(input())
#             if(b == 1):
#                 while(1):
#                     print("Press 1 if you want to retrieve the total sales by category")
#                     print("Press 2 if you want to retrieve the total revenue and number of orders by the seller ")
#                     print("Press 3 if you want to find the number of orders delieverd by each delivery agent in a particular month")
#                     print("Press 4 if you want to find the total orders delivered by an agent")
#                     print("Press 0 if you want to go to the previous menu")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
#     SELECT Category.category_name, SUM(Product.product_price * Product.product_quantity) AS total_sales
#     FROM Product
#     INNER JOIN Category ON Product.category_id = Category.category_ID
#     INNER JOIN Order_ ON Product.product_id = Order_.product_ID
#     WHERE Order_.order_date
#     GROUP BY Category.category_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 2):
#                         sql_query = """ 
#     SELECT Seller.seller_name, SUM(Product.product_price * Product.product_quantity) AS total_revenue, COUNT(Order_.order_ID) AS number_of_orders
#     FROM Product
#     INNER JOIN Order_ ON Product.product_id = Order_.product_ID
#     INNER JOIN Seller ON Order_.seller_ID = Seller.seller_ID
#     GROUP BY Seller.seller_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 3):
#                         sql_query = """ 
#     SELECT d.agent_name, COUNT(*) AS order_count
#     FROM Delivery_Agent d
#     JOIN Order_ o ON d.agent_ID = o.agent_id
#     WHERE MONTH(o.order_date) = 3
#     GROUP BY d.agent_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 4):
#                         sql_query = """ 
#     select agent_id, count(order_id) as 'Total Orders'
#     from Order_ 
#     group by agent_id with rollup;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     else:
#                         break
#             if(b == 2):
#                 while(1):
#                     print("Press 1 if you want to run the first embedded query")
#                     print("Press 2 if you want to run the second embedded query")
#                     print("Press 0 if you want to go back")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
#         SELECT customer_state ,COUNT(*) FROM customer GROUP BY customer_state; 
#         """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 2):
#                         sql_query = """ 
#                                 SELECT C.category_name, COUNT(*) as num_products_sold
#                     FROM Order_ O
#                     JOIN Product P ON O.product_ID = P.product_ID
#                     JOIN Category C ON P.category_id = C.category_ID
#                     GROUP BY C.category_name
#                     ORDER BY num_products_sold DESC
#                     LIMIT 5;
#                                 """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     else:
#                         break
#             if(b == 3):
#                 while(1):
#                     print("Press 1 if you want to run the first Trigger")
#                     print("Press 2 if you want to run the second Trigger")
#                     print("Press 0 if you want to go back")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
                        
# create trigger verify_discount
# before insert on Product
# for each row
# if new.product_discount>80 then set new.product_discount=0;
# end if;//


#                                 """
#                         cursor_.execute(sql_query)
#                     if(c == 2):
#                         sql_query = """ 
# create trigger update_quantity
# before update 
# on Product
# for each row
# IF new.product_quantity<0 then set new.product_quantity=0;
# end if; $$ 


#         """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print("result")
#                     else:
#                         break
#             else:
#                 break
#     else:
#         break
# print(result)
# cursor_.close()
# connect.close()

