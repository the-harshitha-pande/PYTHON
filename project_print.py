# shopping cost calculator- printing total cost,discounted cost,final cost
shirt_price=25.00
jeens_price=50.50

shirt_qty=3
jeens_qty=2

shirt_total=shirt_price*shirt_qty
jeens_total=jeens_price*jeens_qty

total_cost=shirt_total+jeens_total
print("total_cost:",total_cost)

discount=total_cost*0.10
print("discounted_cost:",discount)

final_cost=total_cost-discount
print("final cost is:",final_cost)
print("Thank you for purchasing! ")