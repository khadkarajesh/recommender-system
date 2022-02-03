import os

import requests

inventory_token = "jmbdx2ol7td91oq6pbmZOeJvGhT7Ke4p8VEVxoWhsndD2V5e3vgAMq7bBN4hdCgz9kMePNzUVQlRamCLThBuTg6mv83ib9pTUQBOCxrK2xk4Q4gZ6LoednizaKke_i6FEJ9GjKEMFbv7hViWs57QPjlMGBCVs4hUSGYMRgMHzqLOaN9EdGjRyI_riPfK6zFjm8njKiJ6e0qo9m_Q-1UwFVfQFb7AkPUcLVk_kZI2FraWQrylxMPPYRhYJ3kCLiRK3e4yAUrfGaFap6hBLifPOikbZEuuZD8oOHXm2QejKeM-j3Zc-7g-8dj95D_ipJqH1H5KXDp1oAZSdrpp8WTS"

bearer = f"Bearer {os.environ.get('TOKEN') or inventory_token}"

headers = {
    'Authorization': bearer
}

product_attributes = ["id", "label", "product_category", "selling_price", "images"]


def fetch(data):
    print(data)
    url = f"{os.environ.get('url') or 'https://odoo.jeevee.com/api/v1'}/products?ids={','.join([str(item_id) for item_id in data])}"
    response = requests.request("GET", url, headers=headers, data={})
    json_payload = response.json()
    return json_payload


def get_payload_by_attributes(payload, attributes):
    return {attribute: payload.get(attribute) for attribute in attributes}


def filter_details_by_product_attributes(product_details_from_odoo):
    product_details = product_details_from_odoo.get('products')
    return [get_payload_by_attributes(product_detail, product_attributes) for product_detail in product_details]


def get_product_details(products):
    product_details_from_odoo = fetch(products)
    product_details = filter_details_by_product_attributes(product_details_from_odoo)
    return product_details
