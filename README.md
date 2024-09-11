# Snappfood Project

Snappfood is a Django-based web application designed for managing food orders from restaurants. This README provides an overview of the project's models, views, URLs, and API endpoints.

## Project Structure

The project is divided into several Django apps, each handling different aspects of the application:

- **accounts**: Manages user profiles and wallets.
- **food**: Handles food items and categories.
- **order**: Manages orders, order items, and comments.
- **restaurant**: Manages restaurant data and categories.

## Models

### Accounts

**Profile**

- `user` (ForeignKey): Linked to the Django User model.
- `x` (FloatField): X-coordinate for the user's location.
- `y` (FloatField): Y-coordinate for the user's location.
- `address` (TextField): Address of the user.

**Wallet**

- `user` (OneToOneField): Linked to the Django User model.
- `amount` (PositiveBigIntegerField): Amount of money in the wallet.

### Food

**Category**

- `name` (CharField): Name of the food category.

**Food**

- `category` (ForeignKey): Linked to the Category model.
- `name` (CharField): Name of the food item.
- `slug` (CharField): URL-friendly version of the food name.
- `price` (FloatField): Price of the food item.
- `about` (TextField): Description of the food item.
- `stock` (IntegerField): Number of items in stock.
- `created` (DateField): Creation date of the food item.
- `update` (DateTimeField): Last update date of the food item.
- `restaurant` (ForeignKey): Linked to the Restaurant model.
- `discount_special` (BooleanField): Flag indicating if the food item has a discount.
- `discount_rate` (IntegerField): Discount rate on the food item.

**Rate**

- `rate` (FloatField): Rating value.
- `food` (ForeignKey): Linked to the Food model.
- `user` (ForeignKey): Linked to the User model.

### Order

**Order**

- `user` (ForeignKey): Linked to the User model.
- `paid` (BooleanField): Payment status of the order.
- `created` (DateTimeField): Order creation date.
- `delivery_cost` (IntegerField): Delivery cost associated with the order.
- `status` (CharField): Status of the order (`Pending`, `Preparing`, `Delivered`, `Cancelled`).

**OrderItem**

- `order` (ForeignKey): Linked to the Order model.
- `food` (ForeignKey): Linked to the Food model.
- `price` (FloatField): Price of the food item in the order.
- `num` (IntegerField): Number of items ordered.
- `restaurant` (ForeignKey): Linked to the Restaurant model.

**Comment**

- `user` (ForeignKey): Linked to the User model.
- `comment` (TextField): Text of the comment.
- `order` (OneToOneField): Linked to the Order model.

### Restaurant

**Category**

- `name` (CharField): Name of the restaurant category.
- `created` (DateTimeField): Creation date of the category.

**Restaurant**

- `name` (CharField): Name of the restaurant.
- `owner` (ForeignKey): Linked to the User model (restaurant owner).
- `x` (FloatField): X-coordinate for the restaurant location.
- `y` (FloatField): Y-coordinate for the restaurant location.
- `phone_number` (CharField): Contact phone number of the restaurant.
- `created` (DateTimeField): Creation date of the restaurant.
- `category` (ManyToManyField): Linked to the Category model.

## Serializers

### Accounts

**UserRegisterSerializer**

- Serializes the User model for registration.

### Food

**FoodSerializer**

- Serializes the Food model.

### Order

**OrderSerializer**

- Serializes the Order model.

**OrderItemSerializer**

- Serializes the OrderItem model.

### Restaurant

**RestaurantSerializer**

- Serializes the Restaurant model.

## Views

### Accounts

**Register**

- **Endpoint**: `/user/register/`
- **Method**: POST
- **Description**: Registers a new user.

### Food

**FoodListView**

- **Endpoint**: `/food/foodlist/`
- **Method**: GET, POST
- **Description**: Lists all food items or creates a new food item.

**FoodDetailView**

- **Endpoint**: `/food/food/`
- **Method**: GET, PATCH, DELETE
- **Description**: Retrieves, updates, or deletes a food item.

### Order

**CreateOrderView**

- **Endpoint**: `/order/create_order/<user>/<input_food>/<input_num>/`
- **Method**: POST
- **Description**: Creates a new order.

**AddCommentView**

- **Endpoint**: `/order/add_comment/<order_id>/`
- **Method**: POST
- **Description**: Adds a comment to an order.

**UpdateOrderStatusView**

- **Endpoint**: `/order/update_status/<order_id>/`
- **Method**: PATCH
- **Description**: Updates the status of an order.

**MarkOrderAsPaidView**

- **Endpoint**: `/order/mark_as_paid/<order_id>/`
- **Method**: PATCH
- **Description**: Marks an order as paid.

### Restaurant

**RestaurantListView**

- **Endpoint**: `/restaurant/restaurants/`
- **Method**: GET
- **Description**: Lists all restaurants.

## URLs

### Accounts

**accounts/urls.py**

```python
from django.urls import path
from .views import Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]
