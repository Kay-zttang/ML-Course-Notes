## The Single Neuron Model
A custom framwork and same stochastic gradient descent rule for the models listed below:
- The Perceptron Single Neuron Model
- The Linear Regression Single Neuron Model
- The Logistic Regression Single Neuron Model
---
### **Concept**

#### **- Logistic Regression Single Neuron Model**
Recall lec3 and lec4, but the activation function set to be the **Sigmoid Activation Function** in order to predict the class probability.

<p align="center" width="100%">
    <img align="center" src="Img/the_single_neuron_logistic_regression_model.jpg" width="600" />
</p>

#### **- Neuron Cost Function and Model Update Rule**
The cost function here we choose the **binary cross entropy loss function**.

<p align="center" width="100%">
    <img align="center" src="Img/binary_cross_entropy_loss_function.jpg" width="600" />
</p>
 Since the gradient of the Binary Cross Entropy Loss Function matches the ones in previous single neuron model, we may implement stochastic gradient descent the same way as the model's update rule.
<p align="center" width="100%">
    <img align="center" src="Img/gradient_binary_cross.jpg" width="600" />
</p>


---

### **Implementation**

#### **Dataset Description**
In the impletation the **candidates_data** dataset being used.
- **Candidates_data** : 4 columns 
    - Binary parameters: 'admitted' (0 or 1)
    - Integer parameters: 'work_experience' (Rate from 1 to 6)
    - Numeric parameters: 'gmat' / 'gpa' 

Target: Using different single neuron model to classify admitted or not using numeric parameters "gmat" and "gpa".