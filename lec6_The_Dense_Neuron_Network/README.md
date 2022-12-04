## The Dense Neuron Model

---
### **Concept**
#### **- The Neuron Networks**
* **Structure**:

    1 Input Layer + 1 sequence of Hidden Layer (multiple single nuerons) + 1 Output Layer
* Computational; highly composite
* Problem of latent **overfitting**
* **Work Flow**: (Iterate until arriving at an Output Value)

    Input Signal (feature measure) scaled by $\to$ 1st layer weights
    
    pass into $\to$ an activation function foward into $\to$ next layer
* **Learning Process**: (Same as Single Neuron Model)

     By minimizing the <ins>Cost Function</ins> by adjusting the <ins>Weights and Bias</ins> with some variant of <ins>Gradient Descent</ins>.

<p align="center" width="100%">
    <img align="center" src="Img/the_neuron_network.jpg" width="600" />
</p>

#### **- Neuron Cost Function and Model Update Rule**
Implement stochastic gradient descent as well in each phase.

For each $i = 1, ..., N$:
1. Feedfoward $\mathbf{x}^{(i)}$ into the network 
2. Compute $\delta^{L} = \nabla_aC\otimes \sigma'(\mathbf{z}^{L})$
3. For $\ell = L, L-1, \dots, 1$:
    1. Compute $\delta^{\ell} = \big ( (\mathbf{w}^{\ell + 1})^{T} \delta^{\ell + 1} \Big )\otimes \sigma'(\mathbf{z}^{\ell})$
    2. Update $w$ and $b$ via the update rule:
```math
w^{\ell} \leftarrow w^{\ell} - \alpha \delta^{\ell}(\mathbf{a}^{\ell-1})^{T}
```
```math
b^{\ell} \leftarrow b^{\ell} - \alpha \delta^{\ell}
```


---

### **Implementation**

#### **Dataset Description**