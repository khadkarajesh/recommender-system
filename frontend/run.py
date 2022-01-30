from pathlib import Path

import streamlit as st
from PIL import Image

import requests

API_URL = "http://127.0.0.1:5000/api/v1"

api_data = [
    {
        "id": 2719,
        "label": "ACNE DERMA FACEWASH GEL 60GM",
        "product_category": 104,
        "selling_price": 199.74,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-06-16/5a/5aede9546efe24175f8b28730c5ec04b176cf417",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-06-16/85/85c0edebc067974caa357ba81436be4e4022e9eb",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-06-16/bf/bfdd2e3e13194cacbc59e9a05c176affafe084c5",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-06-16/ef/efccbf95abd2bb18a371fe1a2efc39561b047938",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-06-16/de/de4a1aa0abf113850d1dffff3dfd2ad61a43c5b3"
            }
        ]
    },
    {
        "id": 3589,
        "label": "KODOMO ULTRASHIELD FLORIDE TOOTH PASTE 40 GM GEL (ORANGE)",
        "product_category": 65,
        "selling_price": 120.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-20/a2/a276720a89d6f05f3db1ac33288b2eeafc534943",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-20/aa/aae94b6b6308f28d46ba102c9216575840ff8fb0",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-20/a2/a276720a89d6f05f3db1ac33288b2eeafc534943",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-20/05/05679715ff109a9d2d9204241803ba832322edbe",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-20/01/01ae043983da051a94a3d7627dbed94ed6841162"
            }
        ]
    },
    {
        "id": 8978,
        "label": "DR JK SUNSCREEN LOTION SPF50+++ 200 ML",
        "product_category": 113,
        "selling_price": 1600.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-02-24/65/6556e9fe46c9c545da6c4373239816a53c6fea04",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-02-24/25/25da6695f05b5529da67998fd093d8a8bcd67443",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-02-24/65/6556e9fe46c9c545da6c4373239816a53c6fea04",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-02-24/f5/f527b4ea9820f9a3fb67d01df85b72d203baa623",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-02-24/36/36a885e911775a04c0335b4404b6bd1224c10c97"
            }
        ]
    },
    {
        "id": 3082,
        "label": "UV DOUX SUNSCREEN GEL, SPF 50+, 50GM",
        "product_category": 104,
        "selling_price": 1118.4,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-06/89/899a42c2f4880102ec900bcf0d5aafc903861001",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-06/23/233f9fa4d4b9364d951e943aa315892f8ce89f44",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-06/89/899a42c2f4880102ec900bcf0d5aafc903861001",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-06/a6/a623597b889615b1b5f67f47357c8b2b9b048e98",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-07-06/19/197bd358994e4869d9b69c023598d354602dbb78"
            },
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/a4/a4769748149bb4e2a7c528e887bb5fc6c1d2e7d4",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/1c/1c9681519fc8284407f169364e140e5d54771fed",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/a4/a4769748149bb4e2a7c528e887bb5fc6c1d2e7d4",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/99/9937a4a3c9fc4b16c12dce88bc33c2697b206e26",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/30/302490741ae95da4547841f381433293795cdc2c"
            }
        ]
    },
    {
        "id": 1547,
        "label": "ACMIST MOISTURIZING CREAM GEL 50G",
        "product_category": 104,
        "selling_price": 638.4,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/product/2020-04-18/1547/1024/2020_04_185e9a85cdebf6e_1587185101.jpg",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/product/2020-04-18/1547/128/2020_04_185e9a85cdebf6e_1587185101.jpg",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/product/2020-04-18/1547/1920/2020_04_185e9a85cdebf6e_1587185101.jpg",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/product/2020-04-18/1547/256/2020_04_185e9a85cdebf6e_1587185101.jpg",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/product/2020-04-18/1547/512/2020_04_185e9a85cdebf6e_1587185101.jpg"
            },
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/90/907ecf9977c31c7e7983d517f1e327c6d1b5b4e2",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/5c/5ce52157c980f38c79dec003c9c52d56b01616e2",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/57/57ca5bb61d86448287fb02a72f25ca6866f26203",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/32/323499bfa0a7f2fda789462686b01d17b199f161",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/69/6940c9cdd8d4951420437a938788775d446b892e"
            },
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/c7/c73f6b37991db6bd4f9169345cb7c14f4efe71bb",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/43/43bd7a6668221459197168b0ffecc912b8e13df2",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/c9/c9d591aedca1a9720e9f0598775620ff9066562a",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/64/64cd91747afd32722097d0736ec772685367f7ff",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-27/8f/8fcfb8be0bd1cb449a10d96d0e170b03e3e11267"
            }
        ]
    },
    {
        "id": 2717,
        "label": "UV DOUX SUNSCREEN GEL, SPF 50+, 100GM",
        "product_category": 104,
        "selling_price": 1800.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-20/f5/f52188cbf45052b18371591cc15c93dbe3fbc7f5",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-20/74/74a90764f0e0f9b6def7e534f6ad41ea61050fce",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-20/de/de1aa456af762b74897f39b1c52913f4eba8a678",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-20/41/410408e1c90ce8034b1bd77bd339664019cbe2c2",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-10-20/6c/6cb8b5a2aaa08899a23b6c9526b499f4eefd4505"
            },
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/a4/a4769748149bb4e2a7c528e887bb5fc6c1d2e7d4",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/1c/1c9681519fc8284407f169364e140e5d54771fed",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/a4/a4769748149bb4e2a7c528e887bb5fc6c1d2e7d4",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/99/9937a4a3c9fc4b16c12dce88bc33c2697b206e26",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2020-12-20/30/302490741ae95da4547841f381433293795cdc2c"
            }
        ]
    },
    {
        "id": 13400,
        "label": "BODY AND SOUL VITAMIN C SERUM 30ML",
        "product_category": 104,
        "selling_price": 1000.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-07-16/ca/ca5633a14aaf7d4165919ff5b47a66853f54efc3",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-07-16/41/41df7888f3567433f1aee9bde87477c29f61e8a6",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-07-16/3d/3d5878a7c6213c44d6749ce637efbabdd77439f9",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-07-16/fc/fc82a1edbef3569ca5faebd7a7aa30ac64167c98",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-07-16/0d/0dcca0f9bc03052c808ffebdbf5d493f55125ce2"
            }
        ]
    },
    {
        "id": 1264,
        "label": "KLEIDA SKIN LIGHTENING MOISTURISER 100GM",
        "product_category": 104,
        "selling_price": 1195.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-04-17/5a/5ad06ab2aff673344779dca4f845a858bc496e4d",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-04-17/35/35a2d3d93979e12705e6a82b514c46fd04560637",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-04-17/5a/5ad06ab2aff673344779dca4f845a858bc496e4d",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-04-17/29/292b7d6b9c6fdec85acc73ae052959fab336d9a5",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-04-17/de/ded97ebf75f78589ca3c61d5b95a6606ef412773"
            }
        ]
    },
    {
        "id": 761,
        "label": "PACIMOL 125MG/5ML SYRUP (60ML)",
        "product_category": 70,
        "selling_price": 30.0,
        "images": []
    },
    {
        "id": 189,
        "label": "CETAPHIL DAM 100GM",
        "product_category": 104,
        "selling_price": 760.0,
        "images": [
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/ea/ea73c8e1dcc63c473433307b96f883a513855f13",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/a6/a67ba5142bdc65808cf1b90f065d6d368c78b779",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/ea/ea73c8e1dcc63c473433307b96f883a513855f13",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/40/404c4b0452842c4b2860bbf5dd7ee2a6ccbf8ac9",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/d9/d9177f3c5d878cfdf2ba593bbe93d3527a44523f"
            },
            {
                "1024": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/0c/0c38f9c7c35d1294b54fe2c6c6f505819da183b9",
                "128": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/d5/d59548f1668d2051e50c2a6c6e0dc9cbd8aaea6a",
                "1920": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/0c/0c38f9c7c35d1294b54fe2c6c6f505819da183b9",
                "256": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/c9/c91d07a631389c1b8a7530eee879f4c62a69a50c",
                "512": "https://jeeveedev.s3.us-east-2.amazonaws.com/whetstone-products/jeevee_erp/2021-11-01/3c/3c1c84e073fa7aa106106047ba7bb9286dc7b1e9"
            }
        ]
    }
]


def get_popular_products():
    response = requests.get(API_URL + '/popular-products')
    return response.json()


def get_similar_items(item_id):
    return api_data


def get_recommended_products_for_user(user_id):
    return api_data


with st.container():
    st.write("Popular Products")
    col1, col2, col3, col4, col5 = st.columns(5)

    data = get_popular_products()

    cols = st.columns(len(data) // 2)
    for i, item in enumerate(data):
        col = cols[i % 5]
        col.image(
            item['images'][0]['128'] if item['images'] else Image.open(Path.cwd() / 'frontend' / 'placeholder.png'))
        col.text(item['label'])
        col.text(item['selling_price'])
