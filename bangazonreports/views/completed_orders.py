from bangazonreports.views.connection import Connection
import sqlite3
from django.shortcuts import render

def get_completed_orders(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        Select 
            o.id,
            u.first_name || " " || u.last_name as customer,
            sum(p.price) as total,
            pt.merchant_name as payment
        From bangazonapi_Order o
        Join bangazonapi_Customer c On c.id = o.customer_id
        Join auth_user u On u.id = c.user_id
        Join bangazonapi_OrderProduct op On op.order_id = o.id
        Join bangazonapi_Product p On p.id = op.product_id
        Join bangazonapi_Payment pt On pt.id = o.payment_type_id
        Where payment_type_id Is Not Null
        """)        

        dataset = db_cursor.fetchall()

        order_list = []

        for row in dataset:
            order = {
                "id": row["id"],
                "customer": row["customer"],
                "total": row["total"],
                "payment": row["payment"]
            }

            order_list.append(order)
        
        template = "orders/completed_orders.html"
        context = {
            "order_list": order_list
        }

        return render(request, template, context)