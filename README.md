# Data Portfolio: Analytics, Experimentation, and ML

I build practical, decision-focused data projects across product analytics, A/B testing, causal inference, and machine learning. This portfolio emphasizes reproducible workflows, defensible statistical decisions, and clear business communication for Data Analyst, Experimentation Analyst, and Data Scientist roles.

## Project Index

| Project | Problem | Skills | Dataset | Repo Link | Outcome |
|---|---|---|---|---|---|
| E-commerce Funnel, Cohorts & KPI Dashboard | Identify funnel drop-offs and retention patterns | SQL, cohort analysis, KPI design, pandas | Olist Brazilian E-Commerce | [Project folder](./Project1%20(E-commerce%20Funnel,%20Cohorts%20&%20KPI%20Dashboard)/) | Isolated conversion bottlenecks and retention drivers for action planning |
| Customer Segmentation (RFM + Clustering) | Group customers for targeted lifecycle campaigns | RFM, K-Means, feature engineering, visualization | Olist Brazilian E-Commerce | [Project folder](./Project2%20(Customer%20Segmentation)/) | Produced behavior-based customer segments for differentiated marketing |
| MovieLens Recommender | Recommend relevant items to improve engagement | collaborative filtering, ranking, matrix factorization | MovieLens | [Project folder](./Project3%20(MovieLens%20Recommender)/) | Built recommendation baseline demonstrating personalization capability |
| Olist Recommender (Bonus) | Build product recommendations from purchase behavior | recommendation systems, sparse modeling | Olist Brazilian E-Commerce | [Project folder](./Project3%20(Olist%20Recommender%20-%20Bonus)/) | Delivered additional recommender variant to compare recommendation approaches |
| Sentiment Analysis on Reviews | Detect pain points from unstructured customer feedback | NLP, text preprocessing, topic modeling | Olist customer reviews | [Project folder](./Project4%20(Sentiment%20Analysis)/) | Surfaced key complaint themes in delivery, quality, and service |
| Experiment Lab (Flagship) | Design and evaluate A/B tests with guardrails | power/MDE, CUPED, SRM checks, sequential-safe inference | Synthetic + public A/B-ready sources | [yyzquwu/experiment-lab](https://github.com/yyzquwu/experiment-lab) | Reproducible experiment reports with decision-ready outputs |
| Causal Inference: Job Training | Estimate policy impact beyond randomized tests | propensity scores, matching, IPW, doubly robust methods | LaLonde job training data | [yyzquwu/causal-inference-jobs-training](https://github.com/yyzquwu/causal-inference-jobs-training) | Compared estimators and documented trust assumptions for policy decisions |
| Uplift Modeling: Criteo-style Targeting | Optimize who to treat for incremental impact | T-learner, S-learner, transformed outcome, AUUC/Qini | Criteo-style uplift data workflow | [yyzquwu/uplift-modeling-criteo](https://github.com/yyzquwu/uplift-modeling-criteo) | Converted uplift scores into a concrete top-k targeting policy |

## How to Explore

1. Start with the three public repos above for experimentation, causal inference, and uplift modeling.
2. Review the Olist projects in this repository for SQL + product analytics + NLP breadth.
3. For each project, read the markdown report first, then inspect notebooks/scripts for implementation details.

## Security Notes

- Real API tokens are not stored in this repository.
- Use `.env.example` files as templates for local secrets.
