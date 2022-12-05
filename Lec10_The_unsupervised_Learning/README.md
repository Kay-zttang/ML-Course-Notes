## The Unsupervised Learning

---
### **Concept**
#### - Clustering

#### - Dimensionality Reduction
Principal Component Analysis is used in exploratory data analysis and for multidimensionality reduction. The purpose is to <ins>remove the redundant and highly-correlated data</ins>, and to <ins>keep the most significnat data features</ins> for analysis.

**Process**
Data of $m$ varaibles and $n$ observations
1. Standardize the data 
    * Center :$$ x-mean $$
    * Scale :$$ z = \frac{x - \text{mean}}{\text{standard devation}} $$
2. Compute the Covariance or Correlation Matrix
    * Centered data: Covariance matrix $S$
    * Scaled data: Correlation matrix $S$
```math
S = \frac{1}{n-1}AA^T
```
3. 
---
### **Implementation**

#### **Dataset Description**
In the impletation the **Fruit** dataset being used.
- **Fruit** : 7 columns 
    - Factor parameters: fruit_name / fruit_label / fruit_subtype
    - Numeric parameters: mass / width / height / color_score

Target: Using bragging to classify fruit apple and orange. 