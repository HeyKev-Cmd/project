from .layers import *
from .fast_layers import *
def affine_bn_relu_drop_forward(x, w, b, gamma, beta, bn_params, dropout_params):
  """
  Convenience layer that combines affine transform, batch normalization, ReLU and drop-out
  Inputs:
  - x: Input to the affine layer
  - w, b: Weights for the affine layer
  - gamma, beta: Weights for the normalization layer
  - dropout_params: A dictionary with the following keys:
    - p: Dropout parameter. We drop each neuron output with probability p.
    - mode: 'test' or 'train'. If the mode is train, then perform dropout;
      if the mode is test, then just return the input.
    - seed: Seed for the random number generator. Passing seed makes this
      function deterministic, which is needed for gradient checking but not in
      real networks.
  Returns a tuple of:
  - out: Output from the drop out layer
  - cache: Object to give to the backward pass
  """
  a, (fc_cache, bn_cache, relu_cache) = affine_bn_relu_forward(x, w, b, gamma, beta, bn_params)
  out, dropout_cache = dropout_forward(a, dropout_params)
  cache = (fc_cache, bn_cache, relu_cache, dropout_cache)
  return out, cache

def affine_bn_relu_drop_backward(dout, cache):
  """
  Backwardpass for the affine-batchnorm-ReLU-dropout convenience layer
  """
  fc_cache, bn_cache, relu_cache, dropout_cache = cache
  da = dropout_backward(dout, dropout_cache)
  dx, dw, db, dgamma, dbeta = affine_bn_relu_backward(da, (fc_cache, bn_cache, relu_cache))
  return dx, dw, db, dgamma, dbeta
def affine_bn_relu_forward(x, w, b, gamma, beta, bn_params):
  """
  Convenience layer that combines affine transform, batch normalization and ReLU
  Inputs:
  - x: Input to the affine layer
  - w, b: Weights for the affine layer
  - gamma, beta: Weights for the normalization layer
  Returns a tuple of:
  - out: Output from the ReLU
  - cache: Object to give to the backward pass
  """
  a1, fc_cache = affine_forward(x, w, b)
  a2, bn_cache = batchnorm_forward(a1, gamma, beta, bn_params)
  out, relu_cache = relu_forward(a2)
  cache = (fc_cache, bn_cache, relu_cache)
  return out, cache

def affine_bn_relu_backward(dout, cache):
  """
  Backwardpass for the affine-norm-ReLU convenience layer
  """
  fc_cache, bn_cache, relu_cache = cache
  da2 = relu_backward(dout, relu_cache)
  da1, dgamma, dbeta = batchnorm_backward(da2, bn_cache)
  dx, dw, db = affine_backward(da1, fc_cache)
  return dx, dw, db, dgamma, dbeta


def affine_relu_forward(x, w, b):
    """Convenience layer that performs an affine transform followed by a ReLU.

    Inputs:
    - x: Input to the affine layer
    - w, b: Weights for the affine layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    a, fc_cache = affine_forward(x, w, b)
    out, relu_cache = relu_forward(a)
    cache = (fc_cache, relu_cache)
    return out, cache

def affine_relu_backward(dout, cache):
    """Backward pass for the affine-relu convenience layer.
    """
    fc_cache, relu_cache = cache
    da = relu_backward(dout, relu_cache)
    dx, dw, db = affine_backward(da, fc_cache)
    return dx, dw, db
def affine_relu_dropout_forward(x, w, b, dropout_params):
  """
  Convenience layer that combines affine transform, ReLU and drop-out
  Inputs:
  - x: Input to the affine layer
  - w, b: Weights for the affine layer
  - dropout_params: A dictionary with the following keys:
    - p: Dropout parameter. We drop each neuron output with probability p.
    - mode: 'test' or 'train'. If the mode is train, then perform dropout;
      if the mode is test, then just return the input.
    - seed: Seed for the random number generator. Passing seed makes this
      function deterministic, which is needed for gradient checking but not in
      real networks.
  Returns a tuple of:
  - out: Output from the drop out layer
  - cache: Object to give to the backward pass
  """
  a, (fc_cache, relu_cache) = affine_relu_forward(x, w, b)
  out, dropout_cache = dropout_forward(a, dropout_params)
  cache = (fc_cache, relu_cache, dropout_cache)
  return out, cache

def affine_relu_dropout_backward(dout, cache):
  """
  Backwardpass for the affine-ReLU-dropout convenience layer
  """
  fc_cache, relu_cache, dropout_cache = cache
  da = dropout_backward(dout, dropout_cache)
  dx, dw, db = affine_relu_backward(da, (fc_cache, relu_cache))
  return dx, dw, db
# *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

pass

# *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

def conv_relu_forward(x, w, b, conv_param):
    """A convenience layer that performs a convolution followed by a ReLU.

    Inputs:
    - x: Input to the convolutional layer
    - w, b, conv_param: Weights and parameters for the convolutional layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    a, conv_cache = conv_forward_fast(x, w, b, conv_param)
    out, relu_cache = relu_forward(a)
    cache = (conv_cache, relu_cache)
    return out, cache


def conv_relu_backward(dout, cache):
    """Backward pass for the conv-relu convenience layer.
    """
    conv_cache, relu_cache = cache
    da = relu_backward(dout, relu_cache)
    dx, dw, db = conv_backward_fast(da, conv_cache)
    return dx, dw, db


def conv_bn_relu_forward(x, w, b, gamma, beta, conv_param, bn_param):
    """Convenience layer that performs a convolution, a batch normalization, and a ReLU.

    Inputs:
    - x: Input to the convolutional layer
    - w, b, conv_param: Weights and parameters for the convolutional layer
    - pool_param: Parameters for the pooling layer
    - gamma, beta: Arrays of shape (D2,) and (D2,) giving scale and shift
      parameters for batch normalization.
    - bn_param: Dictionary of parameters for batch normalization.

    Returns a tuple of:
    - out: Output from the pooling layer
    - cache: Object to give to the backward pass
    """
    a, conv_cache = conv_forward_fast(x, w, b, conv_param)
    an, bn_cache = spatial_batchnorm_forward(a, gamma, beta, bn_param)
    out, relu_cache = relu_forward(an)
    cache = (conv_cache, bn_cache, relu_cache)
    return out, cache


def conv_bn_relu_backward(dout, cache):
    """Backward pass for the conv-bn-relu convenience layer.
    """
    conv_cache, bn_cache, relu_cache = cache
    dan = relu_backward(dout, relu_cache)
    da, dgamma, dbeta = spatial_batchnorm_backward(dan, bn_cache)
    dx, dw, db = conv_backward_fast(da, conv_cache)
    return dx, dw, db, dgamma, dbeta


def conv_relu_pool_forward(x, w, b, conv_param, pool_param):
    """Convenience layer that performs a convolution, a ReLU, and a pool.

    Inputs:
    - x: Input to the convolutional layer
    - w, b, conv_param: Weights and parameters for the convolutional layer
    - pool_param: Parameters for the pooling layer

    Returns a tuple of:
    - out: Output from the pooling layer
    - cache: Object to give to the backward pass
    """
    a, conv_cache = conv_forward_fast(x, w, b, conv_param)
    s, relu_cache = relu_forward(a)
    out, pool_cache = max_pool_forward_fast(s, pool_param)
    cache = (conv_cache, relu_cache, pool_cache)
    return out, cache


def conv_relu_pool_backward(dout, cache):
    """Backward pass for the conv-relu-pool convenience layer.
    """
    conv_cache, relu_cache, pool_cache = cache
    ds = max_pool_backward_fast(dout, pool_cache)
    da = relu_backward(ds, relu_cache)
    dx, dw, db = conv_backward_fast(da, conv_cache)
    return dx, dw, db
###############################################


def affine_bn_relu_forward(x, w, b, gamma, beta, bn_param):
  """
  Convenience layer that performs an affine transform, batch normalization,
  and ReLU.
  Inputs:
  - x: Array of shape (N, D1); input to the affine layer
  - w, b: Arrays of shape (D2, D2) and (D2,) giving the weight and bias for
    the affine transform.
  - gamma, beta: Arrays of shape (D2,) and (D2,) giving scale and shift
    parameters for batch normalization.
  - bn_param: Dictionary of parameters for batch normalization.
  Returns:
  - out: Output from ReLU, of shape (N, D2)
  - cache: Object to give to the backward pass.
  """
  a, fc_cache = affine_forward(x, w, b)
  a_bn, bn_cache = batchnorm_forward(a, gamma, beta, bn_param)
  out, relu_cache = relu_forward(a_bn)
  cache = (fc_cache, bn_cache, relu_cache)
  return out, cache


def affine_bn_relu_backward(dout, cache):
  """
  Backward pass for the affine-batchnorm-relu convenience layer.
  """
  fc_cache, bn_cache, relu_cache = cache
  da_bn = relu_backward(dout, relu_cache)
  da, dgamma, dbeta = batchnorm_backward(da_bn, bn_cache)
  dx, dw, db = affine_backward(da, fc_cache)
  return dx, dw, db, dgamma, dbeta  

