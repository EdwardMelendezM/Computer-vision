import numpy as np

npArray = np.zeros((5, 6))
print(npArray)
print(npArray.dtype)
print(npArray.shape)
print(f"Number of row in array is {npArray.shape[0]}")
print(f"Number of columns in array is {npArray.shape[1]}")
print("---")
arrayx = np.zeros((5, 6), dtype=np.uint8)
print(arrayx)
print(arrayx.dtype)

arrayone = np.ones((5, 6), dtype=np.uint8)
print(arrayone)

print("---")
arrayRandom = np.random.rand(5, 6)
print(arrayRandom)
print("----")
npArray = np.array([[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30]],
                   dtype=np.uint8)
print(npArray)
