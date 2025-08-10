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
## 📊 Exploratory Data Analysis (EDA) Insights

- **Sales Trends:** Daily sales are highly volatile with no clear long-term growth pattern.  
- **Top Categories:** Beverages, Personal Care, Household, Dairy, and Snacks dominate sales volume.  
- **Seasonality:** Demand peaks in February, June, and October; dips in May and November.  
- **Location Impact:** Urban stores outperform Suburban and Rural in sales volume.  
- **Pricing Impact:** No strong link between price and sales; demand driven by other factors.  
- **Promotion Effect:** Promotions cause a small sales lift; need better targeting for impact.  
- **Weekday Trends:** Saturday sees highest sales; Sunday and Thursday are lowest.  
- **Stock Levels:** Sales occur across varied stock levels; maintain minimum thresholds to avoid stockouts.  
- **Lead Times:** Longer lead times align with bulk buying; manage to avoid overstock.  
- **Profit Trends:** Significant fluctuations; stronger cost control recommended.  

---

## 📈 Forecast Insights (Summary)

1. **Beverages – Rural (SES):** High seasonal swings; SES smooths better. Keep higher safety stock in peak months.  
2. **Beverages – Suburban (Tie):** Moderate spikes; either model works. Replenish steadily.  
3. **Beverages – Urban (Tie):** Volatile demand; SES handles drops better. Use dynamic reorder points.  
4. **Dairy – Rural (SES):** Stable with mild dips; SES best. Slightly above-average safety stock.  
5. **Dairy – Suburban (SES):** Predictable with spikes; SES tracks changes. Stock up pre-peak.  
6. **Dairy – Urban (Tie):** Abrupt shifts; both models similar. Keep emergency procurement ready.  
7. **Household – Rural (Tie):** Large demand swings; flexible supplier contracts needed.  
8. **Household – Suburban (SES):** Pronounced spikes; SES reliable post-peak. Stagger deliveries.  
9. **Household – Urban (SES):** Stable with minor surges; average safety stock.  
10. **Personal Care – Rural (Tie):** Cyclical demand; stock only before peaks.  
11. **Personal Care – Suburban (MA):** Occasional surges; MA catches peaks. Targeted promotions.  
12. **Personal Care – Urban (Tie):** Frequent fluctuations; keep balanced, flexible stock.  
13. **Snacks – Rural (Tie):** Sharp swings; shorter replenishment cycles.  
14. **Snacks – Suburban (MA):** Steep spikes; build buffer pre-surge, reduce after.  
15. **Snacks – Urban (SES):** Moderate swings; steady stock aligned with forecast.
---

## 📈 Forecast Visuals
![All Forecast Charts](Forecast_Charts.png)


---
## 📌 Recommendations
 
1. **SES** for stable categories (Dairy, Urban Beverages) and **MA** for high-volatility segments.  
2. Implement **dynamic safety stock** linked to forecast accuracy.  
3. Integrate forecasts into **automated replenishment systems** for efficiency.

