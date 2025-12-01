# Data Analyst Portfolio: Brazilian E-Commerce Analysis

## Overview
This portfolio contains a comprehensive analysis of the **Olist Brazilian E-Commerce Dataset**. The goal was to derive actionable business insights, segment customers, build recommendation systems, and analyze customer sentiment using advanced data analytics and machine learning techniques.

## Projects

### [Project 1: E-commerce Funnel, Cohorts & KPI Dashboard](./Project1%20(DA)/)
**Goal:** Analyze the customer journey and retention.
-   **Key Findings:**
    -   Identified drop-off points in the conversion funnel.
    -   Calculated Customer Retention Rate using Cohort Analysis.
    -   Analyzed daily revenue trends and Average Order Value (AOV).
-   **Tech Stack:** SQL (SQLite), Python (Pandas, Matplotlib, Seaborn).

### [Project 2: Customer Segmentation (RFM & Clustering)](./Project2%20(Customer%20Segmentation)/)
**Goal:** Segment customers to enable targeted marketing.
-   **Key Findings:**
    -   **RFM Analysis:** Classified customers into segments like "Champions", "Loyal", and "At Risk".
    -   **K-Means Clustering:** Identified 4 distinct customer personas based on purchasing behavior.
    -   **Insight:** "Loyal Customers" (Cluster 2) have high frequency but moderate spending, while "Big Spenders" (Cluster 3) make few but high-value purchases.
-   **Tech Stack:** Python (Scikit-learn, K-Means), RFM Analysis, 3D Visualization.

### [Project 3: Product Recommendation Engine](./Project3%20(Recommendation%20Engine)/)
**Goal:** Build a system to recommend products to users.
-   **Key Findings:**
    -   **Popularity-Based:** Effective for cold-start users (recommends top sellers like "Bed Bath Table").
    -   **Collaborative Filtering (SVD):** Successfully captures latent product features to provide personalized recommendations based on purchase history.
-   **Tech Stack:** Python (Scikit-learn, TruncatedSVD), Sparse Matrices.

### [Project 4: Sentiment Analysis on Reviews (NLP)](./Project4%20(Sentiment%20Analysis)/)
**Goal:** Understand customer sentiment and pain points.
-   **Key Findings:**
    -   **Sentiment Distribution:** Majority of reviews are Positive (5 stars), but a significant portion are Negative (1 star).
    -   **Topic Modeling (LDA):** Identified key themes in negative reviews:
        -   **Topic 1:** Delivery Delays ("entrega", "atraso", "prazo").
        -   **Topic 2:** Product Quality ("produto", "veio", "defeito").
        -   **Topic 3:** Service/Communication ("nao", "recebi", "loja").
-   **Tech Stack:** Python (NLTK, TextBlob, Scikit-learn LDA), NLP.

## How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn nltk textblob jupyter`.
3.  Navigate to each project folder and run the Jupyter Notebooks (`.ipynb`).

## Author
[Your Name]
