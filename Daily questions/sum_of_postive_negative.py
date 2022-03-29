# Q6. sum of all positive and negitive numbers separately from 1 array
def sum_of_array(lst):
  """
  :param lst: list of array
  :return: sum of postive number and sum of negative numbers separately
  """
  positive_sum = 0
  negative_sum = 0
  for num in lst:
    if num > 0:
      positive_sum += num
    else:
      negative_sum += num
  return positive_sum,negative_sum


if __name__ =="__main__":

  number = {1,2,-4,-1}
  print(sum_of_array(number))