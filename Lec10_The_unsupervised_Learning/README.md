## The Unsupervised Learning

---
### **Concept**
#### - Clustering

#### - Dimensionality Reduction
Principal Component Analysis is used in exploratory data analysis and for multidimensionality reduction. The purpose is to <ins>remove the redundant and highly-correlated data</ins>, and to <ins>keep the most significnat data features</ins> for analysis.

**Process**

Data of $m$ varaibles and $n$ observations
1. Standardize the data 
    * Center : $x-mean$
    * Scale : $z = \frac{x - \text{mean}}{\text{standard devation}}$
2. Compute the Covariance or Correlation Matrix
    * Centered data: Covariance matrix $S$
    * Scaled data: Correlation matrix $S$
```math
S = \frac{1}{n-1}AA^T
```
3. Find the eigenvalues and the orthonormal eigenvectors of $S$

    The eigenvalues $\sigma_{i}^{2}$ is equivalent to the **Singular Value Decomposition** of the shifted training set matrix $A$
```math
A = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^{T}
```
4. Find the  principal components and Reduce the dimension of the data 

    To arrange the eigenvalues in <ins>decreasing</ins> order.
    * The first principal component $PC_1$: the direction of the 1st eigenvector. The second principal component $PC_2$: the direction of the 2nd eigenvector, etc.
    * *Loading scores*: The entries of each $PC_i$

    To project data points onto the selected principal components. 
    * To project the data contained in $A$ onto the first two principle component axis, compute $A [PC_1 PC_2]$.

The Total Variance
```math
T = \text{trace}(S) = \frac{\sigma_{1}^{2} + \dots + \sigma_{m}^{2}}{n-1}
```
```math
\frac{\sigma_{i}^{2}/(n-1)}{T} = \frac{\sigma_{i}^{2}}{\sigma_{1}^{2} + \dots + \sigma_{m}^{2}}
```
---
### **Implementation**

#### **Dataset Description**
In the impletation the **Fruit** dataset being used.
- **Fruit** : 7 columns 
    - Factor parameters: fruit_name / fruit_label / fruit_subtype
    - Numeric parameters: mass / width / height / color_score

Target: Using bragging to classify fruit apple and orange. 