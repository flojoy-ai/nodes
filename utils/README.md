# Utilities for nodes
---

These utilities are meant to make the process of writing nodes easy, and handle common patterns.

## Reconciling different DataContainer types

Nodes should try to accomodate any reasonable combination of inputs that a first-time Flojoy Studio user might try.

For example, the ADD node should make a best effort to do something reasonable when a matrix is added to a dataframe, or a 2 matrices of a different size are added.

For this reason, we've created the `Reconciler` class to handle the process of turning different data types into compatible, easily added objects. 

### An Example

Here's an example of the Reconciler in action from the ADD node. Just initialize the Reconciler and pass it pairs of primitives from within your DataContainers.

```python
def ADD(dc_inputs: list[DataContainer], params: dict) -> DataContainer:

	...
    
    dc_reconciler = Reconciler()
    cur_sum = dc_inputs[0]
    for operand_n in dc_inputs[1:]:
        # reconcile the types of the inputs before calling numpy
        reconciled_lhs, reconciled_rhs = dc_reconciler.reconcile(cur_sum.y, operand_n.y)
        cur_sum = np.add(reconciled_lhs, reconciled_rhs)

    return DataContainer(x=dc_inputs[0].x, y=cur_sum)
```

## Customizing your Reconcilers for different Node Categories

Have a different idea about how you want your DataContainers to be interoperable? Subclass `Reconciler` amd override the specific type pairs you're interested in.

For example, let's say we're writing image processing nodes, and we want special behavior when dealing with certain image-like DataContainers.


```python
class ImageProcessingReconciler(Reconciler):
    def __init__():
        super().__init__()


    # override only for the pair of types you're interested in! 
    def image__image(self, lhs, rhs):
    	# special handling for reconciling two different images
    	... 
    	return lhs, rhs

    def grayscale__image(self, lhs, rhs):
    	# special handling for reconciling a grayscale and an image
    	... 
    	return lhs, rhs

```
