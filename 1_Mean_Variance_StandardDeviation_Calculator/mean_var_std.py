import numpy as np


def calculate(list):

  try:
    if len(list) == 9:
      Arr = np.array([[list[0], list[1], list[2]], [list[3], list[4], list[5]],
                      [list[6], list[7], list[8]]])

      a1 = Arr.mean(axis=0).tolist()
      a2 = Arr.mean(axis=1).tolist()
      a3 = Arr.mean()

      b1 = Arr.var(axis=0).tolist()
      b2 = Arr.var(axis=1).tolist()
      b3 = Arr.var()

      c1 = Arr.std(axis=0).tolist()
      c2 = Arr.std(axis=1).tolist()
      c3 = Arr.std()

      d1 = Arr.max(axis=0).tolist()
      d2 = Arr.max(axis=1).tolist()
      d3 = Arr.max().tolist()

      e1 = Arr.min(axis=0).tolist()
      e2 = Arr.min(axis=1).tolist()
      e3 = Arr.min().tolist()

      f1 = Arr.sum(axis=0).tolist()
      f2 = Arr.sum(axis=1).tolist()
      f3 = Arr.sum().tolist()

      calculations = {
        'mean': [a1, a2, a3],
        'variance': [b1, b2, b3],
        'standard deviation': [c1, c2, c3],
        'max': [d1, d2, d3],
        'min': [e1, e2, e3],
        'sum': [f1, f2, f3]
      }

  except:
    print("List must contain nine numbers.")

  return calculations
