from bangazonreports.views.connection import Connection
import sqlite3
from django.shortcuts import render

def get_favorited_sellers(request):
    # Customer name header
    # Bulleted list of seller names
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        Select 
            c.id,
            uc.first_name || " " || uc.last_name as customer,
            sc.first_name || " " || sc.last_name as seller
        From bangazonapi_favorite f
        Join bangazonapi_customer c On c.id = f.customer_id
        Join auth_user uc On c.user_id = uc.id
        Join bangazonapi_customer cc On cc.id = f.seller_id
        Join auth_user sc On cc.user_id = sc.id
        """)

        dataset = db_cursor.fetchall()

        favorite_list = {}

        for row in dataset:
            customer_id = row["id"]

            if customer_id in favorite_list:
                favorite_list[customer_id]["favorite_sellers"].append(row["seller"])
            else:
                favorite_list[customer_id] = {}
                favorite_list[customer_id]["customer"] = row["customer"]
                favorite_list[customer_id]["favorite_sellers"] = [row["seller"]]
                
        favorites = favorite_list.values()
        
        template = "users/favorited_sellers.html"
        context = {
            "favorites": favorites
        }

        return render(request, template, context)
