# Django Online Food Delivery Project

## Project Overview

This project is a Django-based online food delivery platform that allows users to order food from various restaurants, rate foods, and view their order history. The system also supports restaurant management, including categorization and owner details.

## Project Breakdown

### Apps

1. **`user_profile`**
   - **Models:**
     - `Profile`: Extends the Django `User` model to include additional fields for user location and address.

2. **`food_app`**
   - **Models:**
     - `Category`: Represents food categories.
     - `Food`: Represents food items, including details such as name, price, stock, and discount information.
     - `Rate`: Represents user ratings for food items.
   
3. **`order_app`**
   - **Models:**
     - `Order`: Represents a user's order, including the total price and payment status.
     - `OrderItem`: Represents items within an order, including the food item and quantity.
     - `Comment`: Represents user comments associated with orders.

4. **`restaurant_app`**
   - **Models:**
     - `Category`: Represents restaurant categories.
     - `Restaurant`: Represents restaurant details, including name, owner, location, and phone number.

## Model Details

### User Profile (`user_profile` app)

- **`Profile`**: 
  - `user`: Foreign key linking to the Django `User` model.
  - `x` and `y`: Coordinates for user location.
  - `address`: User's address.

### Food Management (`food_app` app)

- **`Category`**: 
  - `name`: Name of the category.

- **`Food`**:
  - `category`: Many-to-many relationship with `Category`.
  - `name`: Name of the food item.
  - `slug`: URL-friendly identifier for the food item.
  - `price`: Price of the food item.
  - `about`: Description of the food item.
  - `stock`: Available quantity.
  - `created`: Date when the food item was created.
  - `update`: Last update timestamp.
  - `restaurant`: Foreign key linking to `Restaurant`.
  - `discount_spachial`: Boolean indicating if there is a special discount.
  - `discount_rate`: Discount percentage.

- **`Rate`**:
  - `rate`: Rating value.
  - `food`: Foreign key linking to `Food`.
  - `user`: Foreign key linking to `User`.

### Order Management (`order_app` app)

- **`Order`**:
  - `user`: Foreign key linking to `User`.
  - `paid`: Boolean indicating if the order is paid.
  - `created`: Timestamp when the order was created.
  - `delivery_cost`: Delivery cost for the order.

- **`OrderItem`**:
  - `order`: Foreign key linking to `Order`.
  - `foods`: Foreign key linking to `Food`.
  - `price`: Price of the food item.
  - `num`: Quantity of the food item.

- **`Comment`**:
  - `user`: Foreign key linking to `User`.
  - `comment`: Text of the comment.
  - `order`: One-to-one relationship with `Order`.

### Restaurant Management (`restaurant_app` app)

- **`Category`**:
  - `name`: Name of the category.
  - `create`: Timestamp when the category was created.

- **`Restaurant`**:
  - `name`: Name of the restaurant.
  - `owner`: Foreign key linking to `User`.
  - `x` and `y`: Coordinates for restaurant location.
  - `phone_number`: Contact number of the restaurant.
  - `created`: Timestamp when the restaurant was created.
  - `category`: Many-to-many relationship with `Category`.


