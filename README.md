# Do LLM Explanations of Credit Decisions Tell the Truth?

MSc Artificial Intelligence research project, National College of Ireland (2026).

## The question
Banks are starting to use large language models (LLMs) to explain loan decisions to customers.
But does the LLM give the model's **real** reasons, or reasons that just sound believable?

This project measures the **faithfulness** of LLM explanations by checking them against SHAP,
which shows the features that actually drove each credit decision.

## Approach
1. Train credit models: rule baseline, Logistic Regression, XGBoost, MLP
2. Use SHAP to get each applicant's top-3 real reasons (the "answer key")
3. Generate LLM explanations (Flan-T5, Llama 3.2) with and without SHAP in the prompt
4. Score faithfulness, hallucination rate and coverage, with statistical tests

## Data
South German Credit dataset (Grömping, 2019), UCI Machine Learning Repository, CC BY 4.0.
1,000 applicants, 20 features, 700 good / 300 bad credit.

## Progress
- [x] Data loading and checks (1,000 rows, 21 columns, no missing values)
- [x] Stratified 70/15/15 train/validation/test split (seed 42)
- [ ] Baseline models
- [ ] SHAP explanations
- [ ] LLM explanations and faithfulness evaluation

## How to run
```bash
pip install -r requirements.txt
python src/split_data.py
```