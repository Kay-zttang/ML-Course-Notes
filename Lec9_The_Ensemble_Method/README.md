## The Ensemble Method

---
### **Concept**
#### The Bagging
The **B**ootstrap **Agg**regation.

A given set of machine learning model is trained respectively on random samples of training data sets (with replacement). Then to combine the predictions of these models and use as a single prediction.
- Regression: <ins>Average</ins> of predictions
- Classification: <ins>Majority</ins> Vote of predictions

Purpose: To reduce the error and variance of models by aggregation.

#### The Random Forest 

---
### **Implementation**

#### **Dataset Description**
In the impletation the **Titanic** dataset being used.
- **Titanic** : 12 columns (Using 7 columns as features)
    - Predicted label: survived (0 or 1)
    - Predict features: Pclass / Sex / Age / SibSp / Parch / Fare
    - Pre-processing the data for data type, NaN value and etc.

Target: Using predict features to predict survived or dead.