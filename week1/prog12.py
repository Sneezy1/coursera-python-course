pie_price = int(input())
pie_price_cop = int(input())
pie_amount = int(input())
pie_full_price = (pie_price * 100 + pie_price_cop) * pie_amount
print(pie_full_price // 100, pie_full_price % 100)
