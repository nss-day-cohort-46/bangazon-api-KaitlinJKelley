from bangazonapi.models.productrating import ProductRating
from bangazonapi.models.product import Product
import json
import datetime
from rest_framework import status
from rest_framework.test import APITestCase


class ProductTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {"username": "steve", "password": "Admin8*", "email": "steve@stevebrownlee.com",
                "address": "100 Infinity Way", "phone_number": "555-1212", "first_name": "Steve", "last_name": "Brownlee"}
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.token = json_response["token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        url = "/productcategories"
        data = {"name": "Sporting Goods"}

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["name"], "Sporting Goods")

        self.product = Product()
        self.product.name = "toy"
        self.product.price = 7.00
        self.product.quantity = 8
        self.product.description = "a toy"
        self.product.category_id = 1
        self.product.location = "Alabama"
        self.product.customer_id = 1

        self.product.save()

    # def test_create_product(self):
    #     """
    #     Ensure we can create a new product.
    #     """
    #     url = "/products"
    #     data = {
    #         "name": "Kite",
    #         "price": 14.99,
    #         "quantity": 60,
    #         "description": "It flies high",
    #         "category_id": 1,
    #         "location": "Pittsburgh"
    #     }
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.post(url, data, format='json')
    #     json_response = json.loads(response.content)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(json_response["name"], "Kite")
    #     self.assertEqual(json_response["price"], 14.99)
    #     self.assertEqual(json_response["quantity"], 60)
    #     self.assertEqual(json_response["description"], "It flies high")
    #     self.assertEqual(json_response["location"], "Pittsburgh")

    # def test_update_product(self):
    #     """
    #     Ensure we can update a product.
    #     """
    #     self.test_create_product()

    #     url = "/products/1"
    #     data = {
    #         "name": "Kite",
    #         "price": 24.99,
    #         "quantity": 40,
    #         "description": "It flies very high",
    #         "category_id": 1,
    #         "created_date": datetime.date.today(),
    #         "location": "Pittsburgh"
    #     }
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     response = self.client.get(url, data, format='json')
    #     json_response = json.loads(response.content)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(json_response["name"], "Kite")
    #     self.assertEqual(json_response["price"], 24.99)
    #     self.assertEqual(json_response["quantity"], 40)
    #     self.assertEqual(json_response["description"], "It flies very high")
    #     self.assertEqual(json_response["location"], "Pittsburgh")

    # def test_get_all_products(self):
    #     """
    #     Ensure we can get a collection of products.
    #     """
    #     self.test_create_product()
    #     self.test_create_product()
    #     self.test_create_product()

    #     url = "/products"

    #     response = self.client.get(url, None, format='json')
    #     json_response = json.loads(response.content)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(json_response), 3)

    # TODO: Delete product

    # TODO: Product can be rated. Assert average rating exists.
    def test_product_rating(self):
        # Write a new test in the tests/product.py module that verifies that a rating can be added to a product. 
        # It should also verify that the avg_rating key exists, and is correct, on a product.
        rating1 = {
            "product_id": 1,
            "customer_id": 1,
            "rating": 2
        }

        rating2 = {
            "product_id": 1,
            "customer_id": 1,
            "rating": 4
        }

        # self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        response = self.client.post("/productratings", rating1, format="json")
        # print(json.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/productratings", rating2, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(f"/products/{self.product.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["average_rating"], 3)
        


