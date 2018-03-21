# Test Plan

### Menu category displays correctly to user X
input: category
output: formatted string of items and prices
function name: get_menu_items_from_category

## check total order cost is correct X
input: previous total cost plus new item cost
output: new total cost
function name: get_total_price_before_tax

## uuid code
input:
output: valid uuid

## check list of items ordered
input: main menu dict
output: list of keys that have > 0 orders
function name: create_list_of_items_ordered

## calculate tax
input: float
output: float * 10.1%
function name: calculate tax

## calc total price after tax
function name: get_total_price_before_tax

## decrement count of orders on item
input: name of item - key
output: expected total number of orders
function name: decrement_count_of_orders_on_item




