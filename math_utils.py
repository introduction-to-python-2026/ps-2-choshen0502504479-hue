def find_max_number(num1, num2, num3):
    # return the max number 
    if num1 > num2 :
      if num1 > num3 :
        return num1
      else :
        return num3
    else :
      if num2 > num3 :
        return num2
      else :
        return num3

def find_mean(num1, num2, num3):
    # return the mean
    mean = (num1 + num2 + num3) /3
    return mean
    print("the mean is", mean)

def find_mean_std(num1, num2, num3):
    # return the mean std and mean
    mean = find_mean(num1, num2, num3)
    std = (((num1 - mean)**2 + (num2 - mean)**2 + (num3 - mean)**2)/3)**0.5
    return mean, std
    print("The mean is", mean)
    print("The standard deviation is", std)

