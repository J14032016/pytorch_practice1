# -*- coding: utf-8 -*-
# @File  : Autograd tutorial.py
# @Author: Changhui Jiang
# @Date  :  2022/07/11 15:10


import torch

x = torch.ones(2,2,requires_grad= True)
print(x)