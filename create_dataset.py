import numpy as np
import pandas as pd
import random

prices = np.random.randint(100,5000,100)
print(prices)

mode = ["card","cash","upi"]
payment_mode = []
for i in range(0,100):
    a = random.choice(mode)
    payment_mode.append(a)

print(payment_mode)

df = pd.DataFrame({"Prices":prices, "Payment Mode":payment_mode})

df.to_csv("new_data.csv")
