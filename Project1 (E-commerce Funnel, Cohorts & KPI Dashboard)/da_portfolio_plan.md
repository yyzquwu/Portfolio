# 12-Week Data Portfolio Project Plan (8–10 Hours/Week)

Priorities:  
1. Data Analyst  
2. Data Scientist  
3. Analytics Engineer  
4. Data Engineer  

You will build 3 flagship projects (plus 1 optional) that you can showcase for all four roles.

---

## Overview Timeline

- **Weeks 1–4 – Project 1 (DA-heavy)**  
  E‑commerce funnel, cohorts, and KPI dashboard  
  → Strong for Data Analyst, some Analytics Engineer

- **Weeks 5–8 – Project 2 (AE/DE/DA)**  
  Modern analytics stack with dbt + warehouse + BI  
  → Strong for Analytics Engineer + Data Engineer + Data Analyst

- **Weeks 9–12 – Project 3 (DS/DA)**  
  Recommendation system on real user–item data  
  → Strong for Data Scientist + Data Analyst

- **Optional Project – City Safety / Crash Analytics**  
  → Extra Data Analyst + storytelling portfolio piece

Each project is designed to be done in ~4 weeks at 8–10 hours per week. You can adjust pace as needed.

---

## Project 1 (Weeks 1–4) – E‑commerce Funnel, Cohorts & KPI Dashboard

**Goal:** Build a full analytical story for an e‑commerce marketplace: funnels, cohorts, and KPIs, with a polished dashboard and written insights.

### Dataset

- **Brazilian E‑Commerce Public Dataset by Olist (Kaggle)**  
  - Multiple tables: orders, order items, customers, payments, reviews, geolocation.  
  - Great for multi-table joins, funnels, cohorts, and geo analysis.

(Optional add-on: **IBM Telco Customer Churn dataset** if you want a small churn analysis or model as a bonus.)

### What You Build

1. **Data Loading & Cleaning**
   - Load Olist CSVs into:
     - A SQL database (e.g., Postgres, BigQuery, Snowflake) or
     - A notebook environment using pandas.
   - Ensure keys and relationships are clear (orders ↔ items, customers, etc.).

2. **Core Business Metrics & Funnels**
   - Define a simple funnel, e.g.:
     - `order_placed → order_approved → order_delivered`
   - Compute:
     - Conversion rates between steps
     - Revenue, average order value (AOV)
     - Repeat purchase rate

3. **Cohort & Retention Analysis**
   - Define cohorts:
     - By first order month or customer signup month.
   - Compute retention:
     - Cohort vs period revenue / active customers.

4. **Dashboard**
   - Use Tableau / Power BI / Metabase / Superset (your choice).
   - Include at least:
     - High-level KPI overview (revenue, orders, customers)
     - Funnel visualization
     - Cohort heatmap / retention chart
     - Filters (date range, region, product category)

5. **Written Insights**
   - Write a 1–2 page summary:
     - Key findings (e.g., strong/weak cohorts, bottlenecks in funnel)
     - Hypotheses about drivers
     - Concrete recommendations for the “business”

### Suggested Week-by-Week Breakdown

- **Week 1**
  - Explore Olist data, understand tables and relationships.
  - Load data into your database / notebook.
  - Do initial EDA and sanity checks.

- **Week 2**
  - Implement main joins and transformations for orders, customers, and products.
  - Build funnel metrics and visualizations (even just in SQL/Notebooks at first).

- **Week 3**
  - Compute cohorts (e.g., by signup/order month) and retention.
  - Build a first-pass dashboard.

- **Week 4**
  - Refine the dashboard, add filters and better visuals.
  - Write the insights report.
  - Clean up SQL/notebooks and README.

---

## Project 2 (Weeks 5–8) – Modern Analytics Stack (dbt + Warehouse + BI)

**Goal:** Turn the Olist dataset into a production-style analytics stack: warehouse + dbt models + tests + docs + BI. This showcases Analytics Engineer and Data Engineer skills, plus supports analytics use cases.

### Dataset

- Re-use the **Olist e‑commerce dataset** from Project 1.

### Stack (Example)

- **Warehouse:** BigQuery / Snowflake / Redshift / Postgres  
- **Transformations:** dbt  
- **Orchestration (optional):** Airflow or Prefect  
- **Data Quality (optional):** Great Expectations or dbt tests only  
- **BI:** Same tool as Project 1 (for consistency)

### What You Build

1. **Warehouse Setup**
   - Create a dataset / schema in your warehouse.
   - Load raw Olist tables as “source” tables.

2. **dbt Project**
   - Create a dbt project connected to your warehouse.
   - Define **sources** (Olist raw tables).
   - Create **staging models** (`stg_`):
     - Standardize column names
     - Convert data types
     - Clean up obvious issues
   - Create **dimension and fact models** (`dim_`, `fct_`):
     - Examples:
       - `dim_customer`, `dim_product`, `dim_geolocation`
       - `fct_orders`, `fct_order_items`, `fct_payments`
   - Add **tests**:
     - Not null and unique tests (e.g., primary keys)
     - Referential integrity tests between facts and dimensions
   - Add **documentation**:
     - Model descriptions
     - Column descriptions

3. **(Optional) Orchestration & Data Quality**
   - Use Airflow/Prefect to:
     - Run data loading (raw → warehouse)
     - Run dbt models
   - Add Great Expectations or extended dbt tests for:
     - Freshness
     - Volume checks
     - Value distribution checks for key columns

4. **BI Layer**
   - Point your BI tool at dbt “marts” tables.
   - Rebuild or refine the Project 1 dashboard on top of dbt models.
   - Demonstrate that multiple dashboards could reuse the same metric definitions.

5. **Docs & Diagrams**
   - Generate dbt docs and take screenshots or host them.
   - Draw a simple architecture diagram showing:
     - Raw data → warehouse → dbt → BI  
   - Write a short design document explaining modeling choices (star schema, naming conventions, tests).

### Suggested Week-by-Week Breakdown

- **Week 5**
  - Set up warehouse and dbt project.
  - Configure sources and basic staging models.

- **Week 6**
  - Build out full set of staging models.
  - Implement core fact and dimension tables.
  - Add essential dbt tests.

- **Week 7**
  - Refine models (performance, clarity).
  - Generate dbt docs and annotate them.
  - Connect BI tool and rebuild dashboards using dbt marts.

- **Week 8**
  - Optional: add Airflow/Prefect DAG and/or Great Expectations.
  - Finalize architecture diagram, docs, and README.
  - Ensure repo is clean and easy to run.

---

## Project 3 (Weeks 9–12) – Recommendation System on Real User–Item Data

**Goal:** Build an end‑to‑end recommendation engine and evaluation pipeline that you can present as a Data Scientist + Data Analyst project.

### Dataset

- **MovieLens (GroupLens)**
  - User–item rating data for movies.
  - Start with `ml-100k` dataset for quick experimentation.
  - Optional: move to a larger MovieLens set if you want to show scaling.

### What You Build

1. **Data Understanding & Setup**
   - Load the ratings, movies metadata, and (if available) users metadata.
   - Basic EDA:
     - Ratings distribution
     - Popular movies
     - Sparsity of the user–item matrix

2. **Baseline Recommenders**
   - Global popularity baseline:
     - Recommend top-N most popular movies overall.
   - Simple personalized baseline:
     - Recommend top-N movies in user’s favorite genres, or based on highest-rated items.

3. **Collaborative Filtering Model**
   - Implement:
     - Matrix factorization (e.g., using ALS or similar approach).
   - Train/test split:
     - Prefer a time-based or user-based split (e.g., last N interactions for test).
   - Evaluation:
     - Metrics like precision@k, recall@k, NDCG.

4. **Model Comparison & Error Analysis**
   - Compare baseline vs collaborative filtering.
   - Look at which users/items each model works well or poorly for.
   - Discuss biases (e.g., popularity bias).

5. **Simple Interface / Demo**
   - In a notebook or small app:
     - Input: user ID (or a few liked movies).
     - Output: top-N recommendations.
   - Optionally, show explanations (e.g., “recommended because you liked X, Y, Z”).

6. **Write-Up**
   - Problem framing: “How can we recommend items users are likely to enjoy?”
   - Approach summary: baselines → CF model → evaluation.
   - Key findings and limitations.
   - Ideas for future work (e.g., content-based features, hybrid models).

### Suggested Week-by-Week Breakdown

- **Week 9**
  - Load and explore MovieLens data.
  - Build basic EDA and popular-item baseline.

- **Week 10**
  - Implement collaborative filtering model.
  - Set up train/test split and evaluation metrics.

- **Week 11**
  - Improve model (tuning, alternative approaches).
  - Add error analysis and plots.

- **Week 12**
  - Build a simple user-facing interface (notebook or minimal web app).
  - Write a 1–2 page summary and clean up the project repo.

---

## Optional Project – City Safety / Crash Analytics (Extra Analyst Story)

**Goal:** A public-interest data story that shows strong analytical thinking, messy-data handling, and visualization.

### Dataset

- **NYC Motor Vehicle Collisions (NYC Open Data)**
  - Detailed crash-level data (location, time, injuries, contributing factors).

### What You Build

1. **Data Cleaning & Integration**
   - Load the collisions table.
   - Clean missing data, parse dates and times.
   - Optionally join with external data:
     - Weather (by date/time)
     - Neighborhood boundaries or demographics

2. **Analysis**
   - Crash trends over time (by year, month, day-of-week, hour).
   - Spatial analysis: hotspots by neighborhood or intersection.
   - Breakdown by severity, contributing factors, vehicle types.

3. **Visualizations & Story**
   - Time series plots (trends, seasonality).
   - Maps with hotspots (using your tool of choice).
   - A narrative about:
     - Which areas/times are most dangerous
     - Patterns (e.g., late-night weekends, specific boroughs)
     - Recommendations for city planners or policymakers.

4. **Deliverables**
   - Notebook(s) with cleaning and analysis.
   - Dashboard or static visualizations.
   - A written “data story” (blog-style post or PDF).

You can do this as a shorter 2–3 week project if you like, or spread it out alongside the main three projects.

---

## Packaging Everything for Your Portfolio

For each project, make sure you have:

1. **GitHub Repository**
   - Clear folder structure (e.g., `data/`, `notebooks/`, `src/`, `dbt/`, `docs/`).
   - `README.md` that explains:
     - Problem statement
     - Data sources
     - Tools and stack
     - How to run it
     - What the key outputs are (dashboards, reports, apps)

2. **Business-Facing Artifact**
   - Dashboard, a short slide deck, or a written report.
   - Explain the “so what?” and what decisions someone could make.

3. **Technical Rigor**
   - Sensible validation (tests for dbt or unit tests where appropriate).
   - Thoughtful evaluation for any models (baselines, metrics, limitations).

4. **Visuals & Diagrams**
   - Architecture diagram(s) for the stack projects.
   - Key charts and maps for analytics-heavy projects.

If you follow this 12-week plan at 8–10 hours per week, you will have 3 polished, end‑to‑end projects (plus an optional one) that you can show to hiring managers for Data Analyst, Data Scientist, Analytics Engineer, and Data Engineer roles.
