## Sample data for products
categories = ["Sports","Electronics","Furniture"]
items = [["Yonex Badminton Racquet","Felet Badminton Racquet","Nike Runner Shoes Mark II","Puma Jogging Socks"],
         ["iPhone 17 Pro Max 256GB","iPhone Air","Airpods Pro 3","Samsung Z Fold 7 1TB"],
         ["Ikea Essential Chair","3A Plastic Chair","Foldable Table"]]
quantity = [[59,65,90,30],
            [200,582,569,223],
            [477,896,452]]
price = [[200,250,500,90],
         [5999,4999,999,9999],
         [59,120,299]]
reviews = [
    [4.5, 4.2, 4.8, 3.9],
    [4.7, 4.3, 4.6, 4.4],
    [3.8, 3.5, 4.1]
]

# Shopping cart dictionary to store items {(category_index, item_index): quantity}
shopping_cart = {}
    