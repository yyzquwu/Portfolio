# E-commerce Analytics: Insights Report

## Executive Summary
This report summarizes the findings from the analysis of the Brazilian E-commerce dataset (Olist). We analyzed the conversion funnel, core financial metrics, and customer retention cohorts to understand business performance.

**Key Highlights:**
-   **Strong Fulfillment:** The order delivery rate is exceptionally high at **97%**, indicating a robust logistics network.
-   **Healthy AOV:** The Average Order Value is **~$137**, suggesting a mix of mid-to-high value items.
-   **Retention Challenge:** Cohort analysis reveals low month-over-month retention, which is typical for marketplaces but highlights an opportunity for loyalty programs.

---

## 1. Conversion Funnel Analysis
We tracked orders through three key stages: Placement, Approval, and Delivery.

| Stage | Count | Conversion Rate | Drop-off |
| :--- | :--- | :--- | :--- |
| **1. Order Placed** | 99,441 | 100% | - |
| **2. Order Approved** | 99,281 | 99.8% | 0.2% |
| **3. Order Delivered** | 96,478 | 97.0% | 2.8% |

**Insight:**
The drop-off from placement to approval is negligible (<0.2%), meaning payment processing is efficient. The 3% drop-off at delivery could be due to cancellations or logistics issues, but 97% is a strong performance benchmark.

---

## 2. Core Financial Metrics
-   **Total Revenue:** ~$13.2 Million (BRL)
-   **Total Delivered Orders:** 96,478
-   **Average Order Value (AOV):** ~$137.04

**Insight:**
With an AOV of $137, the platform is transacting significant value per customer. Strategies to increase AOV (bundling, cross-selling) could exponentially increase total revenue given the high volume of orders.

---

## 3. Cohort Analysis & Retention
We analyzed customer retention based on their first purchase month.

**Observations:**
-   **Month 0:** 100% active (by definition).
-   **Month 1+:** Retention rates drop sharply to <1%.
-   **Seasonality:** Some cohorts (e.g., Black Friday periods) show slightly different behaviors, but the general trend is low repeat purchase frequency.

**Recommendation:**
The business model appears to be transactional rather than relationship-based. To improve Customer Lifetime Value (CLV), consider:
1.  **Email Marketing:** Re-engage customers post-delivery.
2.  **Loyalty Program:** Incentivize second purchases.
3.  **Subscription Models:** For consumable categories.

---

## 4. Deep Dive Findings
### Delivery Performance
-   **Average Delivery Time:** 12.06 days.
-   **Average Delay:** -11.92 days (Orders arrive ~12 days *early* on average).
-   **Impact on Reviews:** Strong correlation between delays and lower scores. Late orders almost guarantee negative reviews.

### Payment Behavior
-   **Dominant Method:** Credit Card (74%), followed by Boleto (19%).
-   **Installments:** Credit card users average 3.5 installments, while other methods are mostly single-payment. High-value orders drive installment usage.

### Geospatial Revenue
-   **Top State:** SP (São Paulo) generates ~6M BRL, far outpacing RJ (2.1M) and MG (1.8M).
-   **Strategy:** Logistics optimization should focus heavily on the Southeast region (SP, RJ, MG) where the bulk of revenue originates.

---

## 5. Recommendations
1.  **Optimize Logistics:** While average delivery is early, consistency is key. Focus on reducing the long-tail of late deliveries to boost 1-star reviews to 4-5 stars.
2.  **Payment Incentives:** Since Boletos are 19% of orders but have lower conversion (from previous analysis), offer small discounts for Credit Card or PIX to secure payments faster.
3.  **Regional Marketing:** Double down on SP/RJ/MG for marketing efficiency, but explore under-served states for growth potential.

---

## 6. Next Steps
-   **Segment Analysis:** Break down metrics by product category to find high-performing niches.
-   **Geographic Analysis:** Map revenue by state/city to optimize logistics.
-   **Delivery Time Analysis:** Correlate delivery speed with customer satisfaction (review scores).
