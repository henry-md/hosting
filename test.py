
yearly_return = 1.08
yearly_buy = 30000
balance = [0]
for i in range(30):
    balance.append(balance[-1] * yearly_return + yearly_buy)
print([f'{int(b):,}' for b in balance])