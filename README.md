# Customer Segmentation and Sales Analysis using Retail Transaction Data

This project analyzes retail transaction data and segments customers using RFM (Recency, Frequency, Monetary) metrics. It also includes an interactive dashboard built with Streamlit to display key insights and visualizations.

## 📌 Project Objectives
- Clean and analyze retail transaction data
- Perform RFM analysis for customer segmentation
- Visualize customer behavior and key patterns
- Build an interactive dashboard using Streamlit

## 📁 Dataset

For the analyzes retail transaction data and segments customers using RFM (Recency, Frequency, Monetary) metrics, i download the dataset from kaggle dataset by an author Laura Fink, here's the original link:

[E-Commerce Sales Forecast](https://www.kaggle.com/code/allunia/e-commerce-sales-forecast/input?select=data.csv)

For the dashboard loads data directly from Google Drive using shared public links. These dataset are the data that i already process and i put in Google Drive:

- **[cleaned_data.csv](https://drive.google.com/file/d/1_zEIUvWkEo53Ejzdr4zhB4O8U76vhMmN/view?usp=sharing)**: Transaction-level sales data 
- **[rfm_segment.csv](https://drive.google.com/file/d/1lhBDx7Wk_6btlPQ4b1K80ZvQRJ0XaF8G/view?usp=sharing)**: Pre-processed RFM segmentation results

## 🧰 Tools and Libraries
- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Google Colab

## 📊 Analysis Summary
1. Data Cleaning
    - Removed invalid or canceled transactions
    - Handled missing values
    
2. Exploratory Data Analysis (EDA)
    - Top countries by transactions
    - Distribution of frequency, price, and quantity
    - Visualizations with Matplotlib & Seaborn
    
3. RFM Analysis
    - Recency: Days since last purchase
    - Frequency: Number of purchases
    - Monetary: Total spending
    - RFM scoring using quantiles

4. Interactive Dashboard
  - Built with Streamlit
  - Displays RFM distribution, heatmaps, segment summaries
  - Easy to use for business users

## 🔗 Live Demo Dashboard 

👉 [Click here to view the live app on Streamlit Cloud](https://customer-segmentationdashboard.streamlit.app/)


## 📈 Key Insights
- Customers with high Frequency and Monetary scores are highly valuable.
- RFM scores help prioritize marketing strategies.
- The dashboard provides a dynamic way to explore customer segments.

## 📌 Future Improvements
- Add predictive modeling (e.g. Customer Lifetime Value)
- Expand dashboard with filters and segment drilldowns
- Apply clustering techniques (e.g. KMeans) for enhanced segmentation

## 📬 Contact
[Linkedin](https://www.linkedin.com/in/carmenita-lamba-6a7555220/)

carmenitalamba17@gmail.com
