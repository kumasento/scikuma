#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt

def find_last_diff_data(xs, last_lower=-128, epsilon=1e-6):
  rs = [xs[-1]]
  for x in reversed(xs[last_lower:]):
    is_all_diff = True
    # check whether x is different to all data in r
    for r in rs:
      if abs(r-x) < epsilon: # found same
        is_all_diff = False
    if is_all_diff:
      rs.append(x)
  return np.array(rs)
        

if __name__ == '__main__':
  print 'Logistic map: '
  num_mu_stride = 0.005
  mu_upper = 4.0
  mu_lower = 0.0
  mu_list = np.arange(mu_lower, mu_upper, num_mu_stride)
  num_mu = len(mu_list)

  num_iter = 1000
  epsilon = 1e-3
  max_period = 128

  print 'Collecting data points ...'
  xs_list = np.zeros((num_mu, num_iter+1), dtype=float)
  print xs_list.shape
  for idx, mu in enumerate(mu_list):
    xs_list[idx][0] = random.random() # random start point
    for i in xrange(1, num_iter+1):
      # Logistic map calculation
      xs_list[idx][i] = mu * xs_list[idx][i-1] * (1 - xs_list[idx][i-1])
      if xs_list[idx][i] < epsilon:
         xs_list[idx][i] = 0.0 # clean

  print 'Calculating lim for each series ...'
  print 'Here we assume each series are converged:'
  plot_xs = []
  plot_ys = []
  for idx, xs in enumerate(xs_list):
    for x in find_last_diff_data(xs, -max_period, epsilon):
      plot_xs.append(mu_list[idx])
      plot_ys.append(x)
  plt.plot(plot_xs, plot_ys, 'ko', markersize=2)
  plt.show()
