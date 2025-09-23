# Mini Online Shop

A simple console-based online shopping application built with Python. This project simulates an e-commerce experience where users can browse products across different categories, manage their shopping cart, and complete purchases.

## Features

- **Product Browsing**: Browse products across three categories:
  - Sports (Badminton racquets, running shoes, socks)
  - Electronics (iPhones, AirPods, Samsung devices)
  - Furniture (Chairs, tables)

- **Shopping Cart Management**: 
  - Add items to cart with quantity selection
  - View cart contents and total price
  - Edit cart items (modify quantities or remove items)
  - Input validation for all user interactions

- **Product Information**: Each product displays:
  - Name and price
  - Available stock quantity
  - Customer rating (out of 5 stars)

- **Checkout Process**: Complete purchase with order confirmation

- **Inventory Management**: Real-time stock updates as items are added/removed from cart

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Eugene0119666/Mini-Online-Shop.git
cd Mini-Online-Shop
```

2. Ensure you have Python 3.x installed on your system.

## Usage

Run the application:
```bash
python app.py
```

### Main Menu Options:

1. **Browse Sports** - View and shop sports equipment
2. **Browse Electronics** - View and shop electronic devices  
3. **Browse Furniture** - View and shop furniture items
4. **View Cart** - Display current cart contents and total
5. **Edit Cart** - Modify quantities or remove items from cart
6. **Checkout** - Complete your purchase
7. **Exit** - Leave the application

### Shopping Flow:

1. Select a category to browse products
2. Choose a product and specify quantity
3. Items are automatically added to your cart
4. Use "View Cart" to see your selections
5. Use "Edit Cart" to modify quantities or remove items
6. Use "Checkout" to complete your purchase

## Project Structure

```
Mini-Online-Shop/
├── app.py          # Main application file
└── README.md       # Project documentation
```

## Code Features

- **Input Validation**: Robust error handling for all user inputs
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux
- **Clean Interface**: Clear screen functionality for better user experience
- **Data Persistence**: Cart contents maintained throughout the session

## Sample Products

### Sports
- Yonex Badminton Racquet ($200)
- Felet Badminton Racquet ($250)
- Nike Runner Shoes Mark II ($500)
- Puma Jogging Socks ($90)

### Electronics
- iPhone 17 Pro Max 256GB ($5999)
- iPhone Air ($4999)
- Airpods Pro 3 ($999)
- Samsung Z Fold 7 1TB ($9999)

### Furniture
- Ikea Essential Chair ($59)
- 3A Plastic Chair ($120)
- Foldable Table ($299)

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: Only built-in Python modules (`os`, `time`)
- **Architecture**: Procedural programming with modular functions
- **Data Storage**: In-memory lists and dictionaries (session-based)


## Future Enhancements

- [ ] User authentication and profiles
- [ ] Persistent data storage (database integration)
- [ ] Order history tracking
- [ ] Product search functionality
- [ ] Web-based interface
- [ ] Payment processing integration
- [ ] Product categories expansion
- [ ] Inventory management system

