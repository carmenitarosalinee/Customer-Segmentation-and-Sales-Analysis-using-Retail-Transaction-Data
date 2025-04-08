import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Dashboard", layout="wide")

# Fungsi untuk load CSV dari Google Drive
def load_from_gdrive(file_id, parse_dates=None):
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url, parse_dates=parse_dates)

# Load data dari Google Drive
df = load_from_gdrive("1_zEIUvWkEo53Ejzdr4zhB4O8U76vhMmN", parse_dates=['InvoiceDate'])
rfm = load_from_gdrive("1lhBDx7Wk_6btlPQ4b1K80ZvQRJ0XaF8G")

st.title("🛍️ Retail Sales Dashboard")

# KPI Metrics
total_sales = df['TotalPrice'].sum()
total_customers = df['CustomerID'].nunique()

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"£{total_sales:,.0f}")
col2.metric("👥 Total Customers", total_customers)

st.markdown("---")

# 📅 Sales Trend
df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['TotalPrice'].sum().reset_index()

st.subheader("📈 Sales Trend per Month")
st.line_chart(monthly_sales.rename(columns={'Month': 'index'}).set_index('index'))

# 🛒 Top Products
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)

st.subheader("🏆 Top 10 Best-Selling Products")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
st.pyplot(fig)

# 🎯 Customer Segmentation
st.subheader("🎯 Customer Segmentation (RFM)")

segment_counts = rfm['Segment'].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=140)
ax2.axis('equal')
st.pyplot(fig2)

# 🔍 Customer Table by Segment
selected_segment = st.selectbox("Pilih Segment", rfm['Segment'].unique())
st.dataframe(rfm[rfm['Segment'] == selected_segment])
