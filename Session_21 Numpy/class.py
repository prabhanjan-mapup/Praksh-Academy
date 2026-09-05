import numpy as np

'''
creating a numpy array : 
syntax : 
np.array(object)

'''
prices = np.array([10, 20, 30, 40, 50])
print("Pricees = ",prices) #[10,20,30,40,50]
print(type(prices))#<class numpy.ndarray>

py_list = [10,20,30,40,50]
print(py_list) #[10,20,30,40,50]
result=[]
for number in py_list:
    result.append(number+10)

print(result)#[20, 30, 40, 50, 60]

print("Numpy by adding 10 will be : ",prices+10)#vectorization

prices_with_decimals = np.array([10.32, 20.89, 30.16, 40.98, 50.43])
print(prices_with_deimals)

prices_no_dtype = np.array([10, 20, 30, 40, 50],dtype=float)
print(prices_no_dtype)#[10. 20. 30. 40. 50.]
print(type(prices_no_dtype))#<class 'numpy.ndarray'>
print(prices_no_dtype.dtype)

'''
2d - array 
1 2 3
4 5 6
[
    [1,2,3], - 0
    [4,5,6], - 1
    [7,8,9] - 2
] - numpy for matrix calculations

a[1][1]
'''
two_d = np.array([[1,2,3],[4,5,6]])
print(type(two_d))#<class 'numpy.ndarray'>

three_d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(two_d.size)#6

print(two_d[1][2])
#slicing is same as list 

print(two_d[:1,:2])
'''
1,2
4,5
7,8
'''

initial_array = np.zeros(4)#[0,0,0,0]
inital_one_arry = np.ones(5)

full_array= np.full((2,3),5)#[[5,5,5],[5,5,5]]

numbers = np.arange(0,100,2)

numbers_linspace(0,10,5)#[0,2.5,5,7.5,10]

two_d_copy = two_d.copy()
'''
a=[1,2,3,4]
b=[1,2,3,4]
c=[]
suppose a and b and c are lists 
for x in range(len(a)):
    c[x] = a[x]+b[x]

suppose and b are numpy array
a>25
a+b
a.round()
'''






