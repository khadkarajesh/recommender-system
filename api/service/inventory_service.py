import os

import requests

bearer = f"Bearer {os.environ.get('TOKEN')}"

headers = {
    'Authorization': bearer
}

product_attributes = ["id", "label", "product_category", "selling_price", "images"]


def fetch(data):
    print(data)
    url = f"{os.environ.get('URL')}/products?ids={','.join([str(item_id) for item_id in data])}"
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
