# ----------------------------------------------------------------------------
# Copyright 2016 Nervana Systems Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
from __future__ import print_function

import geon.backends.dataloaderbackend
from geon.frontends.base import graph

from geon.frontends.base.graph import Model, with_graph_scope, with_environment, \
    get_current_environment
from geon.backends.graph.environment import bound_environment, Environment

from geon.op_graph.arrayaxes import Axis, Axes, AxisVar, NumericAxis,\
    AxisID, AxisIDTuple, set_batch_axes, get_batch_axes, set_phase_axes, get_phase_axes
from geon.op_graph.names import name_scope_list, with_name_scope, name_scope,  \
    next_name_scope
from geon.op_graph.op_graph import deriv, placeholder, Variable, Constant, linear_map_axes, \
    batch_axes, assign
from geon.op_graph.op_graph import sample_axes, batch_axes, linear_map_axes, RNG, doall, \
    AllReduce, placeholder, Constant, NumPyTensor, absolute, add, argmax, argmin, cos, divide, dot, \
    equal, not_equal, greater, less, greater_equal, less_equal, softmax, max, min, sum, assign, \
    tensor_size, Variable, Temporary, exp, log, safelog, maximum, minimum, multiply, negative, \
    onehot, power, reciprocal, sig, sin, sqrt, square, subtract, tanh, deriv, cross_entropy_multi, \
    cross_entropy_binary, ExpandDims

from geon.op_graph.op_graph import absolute, add, argmax, argmin, cos, divide, dot, equal, exp, log, max, \
    maximum, \
    mean, min, minimum, multiply, onehot, greater, greater_equal, less, less_equal, power
from geon.op_graph.op_graph import negative, not_equal, NumPyTensor, reciprocal, sig, sin, softmax, sqrt, square, subtract, \
    sum
from geon.op_graph.op_graph import tanh, safelog, cross_entropy_binary, cross_entropy_binary_inner, cross_entropy_multi
from geon.op_graph.op_graph import doall, RNG, NumPyTensor, Temporary, tensor_size, set_break

from geon.op_graph.op_graph import AllReduce

# import all available transformers
from geon.transformers.nptransform import NumPyTransformer

try:
    from geon.backends.graph.artransform import ArgonTransformer
except ImportError as e:
    if 'argon' in str(e):
        print("Argon backend and tensor are defined in argon package, which is not installed.")
    elif 'mpi4py' in str(e):
        print(
            "Argon backend currently depends on the package mpi4py, which is not installed."
        )
    else:
        raise


# TODO These are just here as placeholders
def add_fc_bias(self, inputs, bias):
    pass


def batched_dot(self, A, B, C, alpha=None, beta=None, relu=None):
    pass


def check_cafe_compat(self):
    pass


def clip(self, a, a_min, a_max, out=None):
    pass


def compound_dot(self, A, B, C, alpha=None, beta=None, relu=None):
    pass


def exp2(self, a, out=None):
    pass


def fabs(self, a, out=None):
    pass


def finite(self, a, out=None):
    pass


def gen_rng(self, seed=None):
    pass


def log2(self, a, out=None):
    pass


def make_binary_mask(self, out, keepthresh=None):
    pass


def output_dim(self, X, S, padding, strides, pooling=None):
    pass


def rng_get_state(self, state):
    pass


def rng_reset(self):
    pass


def rng_set_state(self, state):
    pass


def set_caffe_compat(self):
    pass


def sig2(self, a, out=None):
    pass


def std(self, a, axis=None, partial=None, out=None, keepdims=None):
    pass


def take(self, a, indices, axis, out=None):
    pass


def tanh2(self, a, out=None):
    pass


def true_divide(self, a, b, out=None):
    pass


def update_fc_bias(self, err, out):
    pass


def var(self, a, axis=None, partial=None, out=None, keepdims=None):
    pass