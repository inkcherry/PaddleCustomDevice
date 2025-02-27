# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function

import numpy as np
import unittest

from op_test import OpTest
import paddle

paddle.enable_static()
SEED = 2022


def accuracy_wrapper(infer, indices, label):
    return paddle._C_ops.accuracy(infer, indices, label)


class TestAccuracy(OpTest):
    def setUp(self):
        self.op_type = "accuracy"
        self.python_api = accuracy_wrapper
        self.set_sdaa()
        self.init_dtype()
        np.random.seed(SEED)
        n = 8192
        infer = np.random.random((n, 1)).astype(self.dtype)
        indices = np.random.randint(0, 2, (n, 1)).astype("int64")
        label = np.random.randint(0, 2, (n, 1)).astype("int64")
        self.inputs = {"Out": infer, "Indices": indices, "Label": label}
        num_correct = 0
        for rowid in range(n):
            for ele in indices[rowid]:
                if ele == label[rowid]:
                    num_correct += 1
                    break
        self.outputs = {
            "Accuracy": np.array(num_correct / float(n)).astype(self.dtype),
            "Correct": np.array(num_correct).astype("int32"),
            "Total": np.array(n).astype("int32"),
        }

    def set_sdaa(self):
        self.__class__.use_custom_device = True
        self.place = paddle.CustomPlace("sdaa", 0)

    def init_dtype(self):
        self.dtype = np.float32

    def test_check_output(self):
        self.check_output_with_place(self.place)


class TestAccuracy2(TestAccuracy):
    def setUp(self):
        self.op_type = "accuracy"
        self.python_api = accuracy_wrapper
        self.set_sdaa()
        self.init_dtype()
        np.random.seed(SEED)
        n = 8192
        infer = np.random.random((n, 100)).astype(self.dtype)
        indices = np.random.randint(0, 1000, (n, 100)).astype("int64")
        label = np.random.randint(0, 1000, (n, 1)).astype("int64")
        self.inputs = {"Out": infer, "Indices": indices, "Label": label}
        num_correct = 0
        for rowid in range(n):
            for ele in indices[rowid]:
                if ele == label[rowid]:
                    num_correct += 1
                    break
        self.outputs = {
            "Accuracy": np.array(num_correct / float(n)).astype(self.dtype),
            "Correct": np.array(num_correct).astype("int32"),
            "Total": np.array(n).astype("int32"),
        }


class TestAccuracyType(TestAccuracy):
    def setUp(self):
        self.op_type = "accuracy"
        self.python_api = accuracy_wrapper
        self.set_sdaa()
        self.init_dtype()
        np.random.seed(SEED)
        n = 8192
        infer = np.random.random((n, 100)).astype(self.dtype)
        indices = np.random.randint(0, 1000, (n, 100)).astype("int64")
        label = np.random.randint(0, 1000, (n, 1)).astype("int32")
        self.inputs = {"Out": infer, "Indices": indices, "Label": label}
        num_correct = 0
        for rowid in range(n):
            for ele in indices[rowid]:
                if ele == label[rowid]:
                    num_correct += 1
                    break
        self.outputs = {
            "Accuracy": np.array(num_correct / float(n)).astype(self.dtype),
            "Correct": np.array(num_correct).astype("int32"),
            "Total": np.array(n).astype("int32"),
        }


class TestAccuracyType2(TestAccuracy):
    def setUp(self):
        self.op_type = "accuracy"
        self.python_api = accuracy_wrapper
        self.set_sdaa()
        self.init_dtype()
        np.random.seed(SEED)
        n = 8192
        infer = np.random.random((n, 100)).astype(self.dtype)
        indices = np.random.randint(0, 1000, (n, 100)).astype("int32")
        label = np.random.randint(0, 1000, (n, 1)).astype("int64")
        self.inputs = {"Out": infer, "Indices": indices, "Label": label}
        num_correct = 0
        for rowid in range(n):
            for ele in indices[rowid]:
                if ele == label[rowid]:
                    num_correct += 1
                    break
        self.outputs = {
            "Accuracy": np.array(num_correct / float(n)).astype(self.dtype),
            "Correct": np.array(num_correct).astype("int32"),
            "Total": np.array(n).astype("int32"),
        }


if __name__ == "__main__":
    unittest.main()
