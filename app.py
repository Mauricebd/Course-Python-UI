import streamlit as st
import requests

API_URL = 'https://course-python-api-jbpc.onrender.com/items'

### Service fetch_items
def fetch_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    st.error(F"Error fetching items : {response.status_code}")
    return []

### Service fetch_item
def fetch_item(item_id):
    response = requests.get(f"{API_URL}/{item_id}")
    if response.status_code == 200:
        return response.json()
    st.error(F"Error fetching item : {response.status_code}")
    return None

### Frontend
st.title("Custom application with Backend")

### Fetch items by ID
st.subheader("Fetch all items")
if st.button("Fetch all items"):
    items = fetch_items()
    st.write(items)

### Fetch item by ID
st.subheader("Fetch item by ID")
item_id = st.number_input('Item ID', min_value=1)
if st.button("Fetch item"):
    item = fetch_item(item_id)
    st.write(item)
