
#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

import sys

old_product_category = None
sales_total = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    new_product_category, this_sale = data

    if old_product_category and old_product_category != new_product_category:
        print "{0}\t{1}".format(old_product_category, sales_total)
        sales_total = 0

    old_product_category = new_product_category
    sales_total += float(this_sale)

if old_product_category != None:
    print "{0}\t{1}".format(old_product_category, sales_total)
