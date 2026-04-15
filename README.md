# Data Portfolio

This is a small collection of projects I use to show how I work with data: finding patterns, testing ideas, and turning messy inputs into something useful. The mix here covers product analytics, experimentation, causal inference, recommendation systems, and NLP.

## Projects

| Project | What it looks at | Main skills | Dataset | Link | Result |
|---|---|---|---|---|---|
| E-commerce Funnel, Cohorts & KPI Dashboard | Funnel drop-offs and retention patterns | SQL, cohort analysis, KPI design, pandas | Olist Brazilian E-Commerce | [Project folder](./Project1%20(E-commerce%20Funnel,%20Cohorts%20&%20KPI%20Dashboard)/) | Highlighted conversion bottlenecks and retention drivers |
| Customer Segmentation (RFM + Clustering) | Grouping customers for lifecycle campaigns | RFM, K-Means, feature engineering, visualization | Olist Brazilian E-Commerce | [Project folder](./Project2%20(Customer%20Segmentation)/) | Created behavior-based customer segments |
| MovieLens Recommender | Recommending relevant items | collaborative filtering, ranking, matrix factorization | MovieLens | [Project folder](./Project3%20(MovieLens%20Recommender)/) | Built a recommendation baseline |
| Olist Recommender (Bonus) | Product recommendations from purchase behavior | recommendation systems, sparse modeling | Olist Brazilian E-Commerce | [Project folder](./Project3%20(Olist%20Recommender%20-%20Bonus)/) | Added a second recommender for comparison |
| Sentiment Analysis on Reviews | Pain points in customer feedback | NLP, text preprocessing, topic modeling | Olist customer reviews | [Project folder](./Project4%20(Sentiment%20Analysis)/) | Surfaced common complaints in delivery, quality, and service |
| Experiment Lab (Flagship) | A/B test design and analysis | power/MDE, CUPED, SRM checks, sequential-safe inference | Synthetic + public A/B-ready sources | [yyzquwu/experiment-lab](https://github.com/yyzquwu/experiment-lab) | Reproducible experiment reports with decision-ready outputs |
| Causal Inference: Job Training | Policy impact beyond randomized tests | propensity scores, matching, IPW, doubly robust methods | LaLonde job training data | [yyzquwu/causal-inference-jobs-training](https://github.com/yyzquwu/causal-inference-jobs-training) | Compared estimators and documented the assumptions behind them |
| Uplift Modeling: Criteo-style Targeting | Who to treat for incremental impact | T-learner, S-learner, transformed outcome, AUUC/Qini | Criteo-style uplift data workflow | [yyzquwu/uplift-modeling-criteo](https://github.com/yyzquwu/uplift-modeling-criteo) | Turned uplift scores into a top-k targeting policy |

## Quick Start

If you want the shortest path through the repo:

1. Start with the public repos for experimentation, causal inference, and uplift modeling.
2. Open the Olist projects here for SQL, product analytics, and NLP work.
3. Read the markdown report first, then dig into notebooks and scripts if you want the implementation details.

## Notes

- Real API tokens are not stored in this repository.
- Use `.env.example` as a template for local secrets.
