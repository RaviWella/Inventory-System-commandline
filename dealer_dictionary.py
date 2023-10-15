import json
dealers = {
    'RAVINDU WELLALAGE': {
        'Contact_Number': '+9471000925',
        'Location':'Colombo',
        'items': [
            {
                'Item_name': 'Lenovo Idea Pad',
                'brand': 'Lenovo',
                'price': 'RS. 389990.00',
                'quantity': '20'
            },
            {
                'Item_name': 'HP Mouse',
                'brand': 'HP',
                'price': 'RS. 5500.00',
                'quantity': '20'
            },
            {
                'Item_name': 'DELL laptop',
                'brand': 'DELL',
                'price': 'RS. 55000.00',
                'quantity': '20'
            }
        ]
    },
    'RADIL DAMSA': {
        'Contact_Number': '+9415555261',
        'Location':'Jaffna',
        'items': [
            {
                'Item_name': 'Apple MacBook Pro',
                'brand': 'Apple',
                'price': 'Rs. 499999.00',
                'quantity': '10'
            },
            {
                'Item_name': 'Dell XPS 13',
                'brand': 'Dell',
                'price': 'Rs. 550000.00',
                'quantity': '15'
            },
            {
                'Item_name': 'heat fan pro',
                'brand': 'Dell',
                'price': 'Rs. 45000.00',
                'quantity': '05'
            }
        ]
    },
    'SEHANDU SIRIWARDANA': {
        'Contact_Number': '+9420898732',
        'Location':'Gampaha',
        'items': [
            {
                'Item_name': 'Samsung Galaxy S21',
                'brand': 'Samsung',
                'price': 'Rs. 220000.00',
                'quantity': '05'
            },
            {
                'Item_name': '8GB pen drive',
                'brand': 'NoobMaster',
                'price': 'Rs. 4700.00',
                'quantity': '08'
            },
            {
                'Item_name': 'DELL monitor',
                'brand': 'Dell',
                'price': 'Rs. 50000.00',
                'quantity': '20'
            }
        ]
    },
    'DEVINDI WIJESINGHE': {
        'Contact_Number': '+9420898752',
        'Location':'Kalubowila',
        'items': [
            {
                'Item_name': 'Samsung Galaxy S21',
                'brand': 'Samsung',
                'price': 'Rs. 220000.00',
                'quantity': '05'
            },
            {
                'Item_name': 'Adjestable chairs',
                'brand': 'Damro',
                'price': 'Rs. 35000.00',
                'quantity': '30'
            },
            {
                'Item_name': 'Warm LED',
                'brand': 'Keels',
                'price': 'Rs. 800.00',
                'quantity': '40'
            }
        ]
    },
    'DINUSHI WANNIARACHCHI': {
        'Contact_Number': '+9425688752',
        'Location':'Matara',
        'items': [
            {
                'Item_name': 'Nice Line Camera',
                'brand': 'Hitachi',
                'price': 'Rs. 100000.00',
                'quantity': '05'
            },
            {
                'Item_name': 'wool carpet',
                'brand': 'Arpico',
                'price': 'Rs. 1000.00',
                'quantity': '20'
            },
            {
                'Item_name': 'DELL SU pro',
                'brand': 'Dell',
                'price': 'Rs. 550000.00',
                'quantity': '25'
            }
        ]
    },
    'SHARITH PAMODA': {
        'Contact_Number': '+9425688752',
        'Location':'Negombo',
        'items': [
            {
                'Item_name': 'Super Cool Air Conditioner',
                'brand': 'Abans',
                'price': 'Rs. 450000.00',
                'quantity': '10'
            },
            {
                'Item_name': 'DELL SU pro',
                'brand': 'Dell',
                'price': 'Rs. 550000.00',
                'quantity': '25'
            },
            {
                'Item_name': 'Graphic Pad',
                'brand': 'Huawei',
                'price': 'Rs. 50000.00',
                'quantity': '05'
            }
        ]
    }
}



# Convert dictionary to JSON string
def ddd():
    dealers_json = json.dumps(dealers)

    # Write JSON string to file
    with open('dealers.txt', 'w') as file:
        file.write(dealers_json)




