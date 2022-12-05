## The Ensemble Method

---
### **Concept**
#### - The Bagging
The **B**ootstrap **Agg**regation.

A given set of machine learning model is trained respectively on random samples of training data sets (with replacement). Then to combine the predictions of these models and use as a single prediction.
- Regression: <ins>Average</ins> of predictions
- Classification: <ins>Majority</ins> Vote of predictions

Purpose: To reduce the error and variance of models by aggregation.

#### - The Random Forest 

---
### **Implementation**

#### **Dataset Description**
In the impletation the **Fruit** dataset being used.
- **Fruit** : 7 columns 
    - Factor parameters: fruit_name / fruit_label / fruit_subtype
    - Numeric parameters: mass / width / height / color_score

Target: Using bragging to classify fruit apple and orange. 