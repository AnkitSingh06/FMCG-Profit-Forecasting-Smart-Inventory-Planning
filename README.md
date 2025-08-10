# 📦 Profit Forecasting & Smart Inventory Planning – HUL Supply Chain Trainee Project

## 📝 Project Overview
This project demonstrates **profit-based demand forecasting** and **smart inventory planning** for an FMCG supply chain, tailored for **Hindustan Unilever Limited (HUL)**.  
It integrates **statistical forecasting methods**, **inventory control models**, and **actionable replenishment strategies** to minimize stockouts, reduce working capital, and align inventory with profitability goals.

---

## 🎯 Objectives
- **Forecast Profits by Category & Market Type** using Moving Average (MA) and Simple Exponential Smoothing (SES).
- **Optimize Safety Stock & Reorder Points** using forecasted demand, demand variability, and lead times.
- **Generate SKU-level Replenishment Decisions** to balance service level targets with cost efficiency.

---

## 📊 Key Insights

### **1. Forecasting Accuracy**
- **Best-performing segment:** Personal Care (Urban) – MAE: ₹3,418, RMSE: ₹4,912.
- **High variability segment:** Snacks (Rural) – MAE: ₹5,813, RMSE: ₹6,940.
- **SES outperforms MA** for Dairy (Rural), improving MAE from ₹4,982 to ₹4,765.
- **Average MAE across all categories:** ₹4,650 – indicating moderate predictability in profit trends.

### **2. Inventory Planning**
- **Highest Safety Stock:** Beverages (Urban) – ₹1,373.76 (high fluctuation + 6-day lead time).
- **High volatility:** Dairy (Suburban) – Safety Stock ₹1,219.19 with shorter 4-day lead time.
- **Stockout Risk:** 68% of SKUs below ROP – require urgent replenishment.
- **Suggested Order Quantities:** ~1,100 units (Snacks Rural) to ~1,600 units (Beverages Urban).

---

## 🛠️ Methodology
1. **Data Preparation:** Cleaned and segmented sales & profit data by category and market type (Rural, Suburban, Urban).
2. **Forecasting Models:**
   - Moving Average (MA)
   - Simple Exponential Smoothing (SES)
3. **Inventory Calculations:**
   - **Safety Stock:** `Z * σ_demand * sqrt(Lead Time)`
   - **Reorder Point (ROP):** `(Average Demand × Lead Time) + Safety Stock`
   - **Order Quantity:** `ROP – Current Stock`
4. **Visualization:** Profit trend plots and SKU-level inventory dashboards.

---

## 📂 Repository Structure
