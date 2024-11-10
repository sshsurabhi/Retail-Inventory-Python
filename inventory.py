class Product:
    inventory = []  # Class variable to hold all Product instances

    def __init__(self, product_id, name, category, quantity, price, supplier):
        """ 
        Initialize an instance of Product. 
        """ 
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        
        # Append this instance to the inventory list
        Product.inventory.append(self)

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        """ 
        Adds a new product to the inventory. 
        """
        # Determine a unique product ID
        product_id = len(cls.inventory) + 1  
        
        # Create a new product instance
        new_product = cls(product_id, name, category, quantity, price, supplier)
        
        # Return the success message
        return f"Product '{new_product.name}' added successfully with ID: {new_product.product_id}"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        """ 
        Updates existing product information. 
        """
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        """ 
        Deletes a product from the inventory. 
        """
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"

    @classmethod
    def get_product(cls, product_id):
        """ 
        Retrieves a product by its ID. 
        """
        for product in cls.inventory:
            if product.product_id == product_id:
                return product
        return None


class Order:
    def __init__(self, order_id, products=None, customer_info=None):
        """ 
        Initialize an instance of Order. 
        """
        self.order_id = order_id
        self.products = products if products is not None else []  # Initialize products list
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        """ 
        Places an order for a specified product. 
        """
        self.customer_info = customer_info
        
        # Check if the product exists and if there is enough quantity available
        product = Product.get_product(product_id)
        if product is None:
            return "Product not found"
        if product.quantity < quantity:
            return "Insufficient product quantity"

        # Append the product ID and quantity to the order
        self.products.append((product_id, quantity))

        # Reduce the product quantity in inventory
        product.quantity -= quantity

        return f"Order placed successfully. Order ID: {self.order_id}"


# Example Usage
# Adding products to the inventory
print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))  # Should confirm success
print(Product.add_product("T-Shirt", "Clothing", 150, 20, "Supplier B"))  # Should confirm success

# Checking the inventory
for product in Product.inventory:
    print(f"ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}")

# Updating a product
print(Product.update_product(1, quantity=45, price=950))  # Should confirm success

# Placing an order
order = Order(order_id=1)
order_placement = order.place_order(1, 5, customer_info="John Doe")
print(order_placement)  # Should confirm success

# Check remaining quantity of the first product
print(f"Remaining quantity of Laptop: {Product.inventory[0].quantity}")  # Should reflect the updated quantity after the order