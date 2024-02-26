import streamlit as st
import pandas as pd
import json
import requests

df = pd.read_csv('winequality-red.csv', sep=';')
columns = df.columns
st.title("Basic ML App for 🍷 quality prediction")
st.write('Example Data:')
st.dataframe(df.head())
meta_data = df.describe()
min_data = meta_data.loc['min', :]
max_data = meta_data.loc['max', :]

data_dict = {}
for c in list(df.columns)[:-1]:
    data_dict[c] = st.slider(c, min_data[c], max_data[c], 0.05)

# coverting the inputs into a json format
inputs = {
  "data": [list(data_dict.values())]
}

if st.button('Predict'):
    res = requests.post(url = 'http://127.0.0.1:8000/predict', data = json.dumps(inputs))
    print(inputs, res.text)
    if int(res.text) != 0:
        st.subheader(f'This wine is good 👍')
    else:
        st.subheader(f'This wine is bad 👎')
    st.write(data_dict)