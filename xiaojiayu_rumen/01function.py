def discounts(price,rate):
    final_price = price * rate
    old_price = 50
    print('修改后的old_price的值是:',old_price)
    return final_price

old_price = float(input('请输入原件：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('修改后的old_price的值是:',old_price)
print('打折后价格是:',new_price)
