

-- orders/cart
-- retrieve orders and orders by order_reference
SELECT order_reference,order_item_name_id,order_item_quantity
FROM cart_cart 
ORDER BY order_reference;

-- join with menu
SELECT cart_cart.order_reference,cart_cart.order_item_name_id,cart_cart.order_item_quantity,menu_menu.menu_id,menu_menu.menu_item,menu_menu.menu_price
FROM cart_cart INNER JOIN menu_menu ON cart_cart.order_item_name_id = menu_menu.menu_id
ORDER BY cart_cart.order_reference;

-- join with menu where order_reference
SELECT cart_cart.order_reference,cart_cart.order_item_name_id,cart_cart.order_item_quantity,menu_menu.menu_id,menu_menu.menu_item,menu_menu.menu_price
FROM cart_cart 
INNER JOIN menu_menu 
ON cart_cart.order_item_name_id = menu_menu.menu_id 
AND cart_cart.order_reference = '899b6baa-a17b-4739-ab34-1ecb42ce6a09';


