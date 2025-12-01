# Customer Segmentation Insights Report

## Executive Summary
We performed a comprehensive customer segmentation analysis using both rule-based RFM (Recency, Frequency, Monetary) scoring and machine learning-based K-Means clustering. The goal was to identify distinct customer personas to tailor marketing strategies.

**Key Findings:**
-   **High Churn Risk:** A significant portion of the customer base has not purchased in a long time (high Recency).
-   **Low Frequency:** The vast majority of customers (97%) have only made a single purchase.
-   **High-Value Niche:** A small but valuable segment of "Loyal Customers" exists who purchase frequently (2+ times) and spend more.

## RFM Analysis
We assigned scores (1-5) to each customer for Recency, Frequency, and Monetary value. Based on these scores, we identified key segments:

| Segment | Definition | Strategy |
| :--- | :--- | :--- |
| **Champions** | Recent buyers (R=4-5), Frequent (3+ orders). | Reward loyalty, offer early access, ask for reviews. |
| **Loyal Customers** | Good Recency (R=3-5), Repeat buyers (2+ orders). | Upsell higher value items, loyalty programs. |
| **Recent Users** | Recent buyers (R=4-5), Single order. | Onboarding emails, welcome discounts for next purchase. |
| **About to Sleep** | Average Recency (R=3), Single order. | Reactivation campaigns, limited time offers. |
| **At Risk** | Old Recency (R=1-2), Repeat buyers (2+ orders). | Win-back campaigns, surveys to understand churn. |
| **Hibernating** | Old Recency (R=1-2), Single order. | Low priority, automated re-engagement emails. |

## Methodology Comparison: RFM vs. K-Means
**Are they the same?** No, but they are complementary.
-   **RFM Segments** are based on *fixed rules* we defined (e.g., "Frequency >= 2 means Loyal"). This is great for quick, explainable targeting.
-   **K-Means Clusters** are found by an *algorithm* looking for natural groupings in the data without pre-defined rules.

**Alignment:**
Ideally, the two methods should tell a similar story. In our analysis, they align very well:
-   **RFM "Loyal"** overlaps heavily with **Cluster 2**.
-   **RFM "Recent Users"** overlaps with **Cluster 3**.
-   **RFM "Hibernating"** covers the massive **Clusters 0 & 1**.

## K-Means Clustering
Using K-Means clustering (K=4), we identified four data-driven personas that align well with our RFM segments:

### Cluster 0: "Dormant Big Spenders" (~37k customers)
-   **Characteristics:** High Recency (~278 days), Single Purchase, High Spend (~$237).
-   **Alignment:** Corresponds to high-value **Hibernating** customers.
-   **Insight:** These customers spent a lot but haven't returned. They are a prime target for win-back campaigns highlighting new premium products.

### Cluster 1: "Lost Cheap Customers" (~36k customers)
-   **Characteristics:** High Recency (~284 days), Single Purchase, Low Spend (~$45).
-   **Alignment:** Corresponds to low-value **Hibernating** customers.
-   **Insight:** Low value and churned. Likely not worth high acquisition costs to re-engage. Automated emails only.

## 4. Deep Dive: Segment Profiling
### Product Preferences
-   **Universal Favorites:** "Bed Bath Table" (cama_mesa_banho) and "Health Beauty" (beleza_saude) are top categories across almost all segments.
-   **Tech Lovers:** "Loyal Customers" have a higher affinity for "Computers & Accessories" than other groups.
-   **Home Decor:** "Hibernating" and "Can't Lose Them" customers buy heavily in "Furniture Decor".

### Customer Satisfaction (Review Scores)
-   **Champions:** Highest satisfaction (**4.22/5**). They buy often, spend well, and are happy.
-   **Loyal Customers:** Surprisingly lower satisfaction (**4.07/5**). Despite frequent purchases, they might be experiencing fatigue or minor service issues.
-   **Action:** Investigate why "Loyal Customers" are less happy than "Champions". A small VIP perk or proactive support could boost their sentiment.

## 5. Strategic Recommendations
-   **Champions:** Reward them! Early access to new "Health & Beauty" products.
-   **Loyal Customers:** They need love. Send a "Thank You" discount or survey to address the slightly lower satisfaction.
-   **Recent Users:** Cross-sell "Bed Bath Table" items as they are the most likely next purchase.
-   **At Risk / Hibernating:** Re-engage with "Home Decor" offers, as this is a strong category for them.

### Cluster 2: "Loyal & Active" (~2.8k customers)
-   **Characteristics:** Moderate Recency (~220 days), **High Frequency (~2.1)**, High Spend (~$260).
-   **Alignment:** Corresponds to **Loyal Customers** and **At Risk** (repeat buyers).
-   **Insight:** The most valuable segment. They come back! Focus on retention and community building.

### Cluster 3: "Recent Users" (~16k customers)
-   **Characteristics:** **Low Recency (~41 days)**, Single Purchase, Moderate Spend (~$116).
-   **Alignment:** Corresponds to **Recent Users** and **Champions** (new high potential).
-   **Insight:** New customers. The goal is to convert them into Cluster 2 (Loyal) before they drift into Cluster 0 or 1.

## Recommendations
1.  **Focus on the "Recent Users" (Cluster 3 / RFM Recent Users):** This is the critical window. Implement a strong post-purchase email sequence to encourage a second buy within 60 days.
2.  **Win-Back "Dormant Big Spenders" (Cluster 0):** Since they have high spending power, offer a significant discount or exclusive offer to bring them back.
3.  **Nurture "Loyal" (Cluster 2 / RFM Loyal):** Create a VIP program. Give them reasons to stay (e.g., free shipping, birthday gifts).
4.  **Ignore "Lost Cheap" (Cluster 1):** Don't waste ad spend here. Use low-cost channels like email if at all.
