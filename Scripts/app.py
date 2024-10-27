import pickle
import pandas as pd

with open('HouseModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#RM, PTRATIO, LSTAT

RM = float(input("Enter the number of rooms: "))
PTRATIO = float(input("Enter the number of rooms: "))
LSTAT = float(input("Enter the number of rooms: "))

arr = pd.DataFrame([{'RM': RM, 'PTRATIO': PTRATIO, 'LSTAT': LSTAT}])
result = model.predict(arr)

print(f"Result is: {result}")