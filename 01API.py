#pandas is an API
"""An API lets two pieces of software talk to each other. Just like a function, 
you don't have to know how the API works, only its inputs and outputs."""
"""
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    
"""
import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],
       'b':[12,22,32]}

print(dict_)

df = pd.DataFrame(dict_)
print(df)

print("head")
print(df.head())
print("mean")
print(df.mean())