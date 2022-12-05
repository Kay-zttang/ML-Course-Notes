## The k-Nearest Neighbor Algorithm

---
### **Concept**
#### KNN 
Use the distance between points to identify the similarity of points. More specifically, using the Euclidean distance for measurment.
```math
d(p, q) = \sqrt{(p - q)^{T} (p - q)}
```

#### Process
1. Number of neighbors chosed: K
2. For each example in the data
    1. **Calculate the distance** between the query example and the current example from the data.
    2. Add the distance and the index of the example to an ordered collection
3. **Sort** the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances
4. **Pick the first K entries** from the sorted collection and get teh related labels
5. Case: 
    * regression: return the **mean** of the K labels
    * classification: return the **mode** of the K labels

---

### **Implementation**

#### **Dataset Description**
In the impletation the **Fruit** and **Audible** dataset being used.
- **Fruit** : 7 columns 
    - Factor parameters: fruit_name / fruit_label / fruit_subtype
    - Numeric parameters: mass / width / height / color_score

Target: Using numeric parameters to predict fruit name.

- **Audible** : 5 columns 
    - String parameters: Book name / Author
    - Numeric parameters: Rating / Number of Reviews / Price

Target: Using numeric parameters to recommend similiar audible books.