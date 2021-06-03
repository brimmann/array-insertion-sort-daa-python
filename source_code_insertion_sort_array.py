import matplotlib.pyplot as plt #This library was imported for plotting graph for growth function


def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
arr = [5, 10, 4, 54, 81]
print("Given array:")
print(arr)
insertion_sort(arr) 
print("Sorted array:") 
print(arr) 


#Growth Function of Max Element for Worst Case Scenario is T(n) = n^2

def worst_case_fun(n):
    return n*n

#Calculating domain and range of the function.

fun_range = []

for i in range(0, 10):
     fun_range.append(i)

fun_domain = []
for value in fun_range:
     fun_domain.append(worst_case_fun(value))

print(fun_domain)

#Plotting graph for the given range and domain.

plt.plot(fun_range, fun_domain)
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("INSERTION SORT ALGORITH TIME COMPLEXITY GRAPH")
plt.text(2, 40, "By Mohammad Rashid 3927")
plt.show()
