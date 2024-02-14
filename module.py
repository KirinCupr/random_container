import random

def get_rand_array(n):
    elements = [i for i in range(1, n+1)]
    array = [0 for i in range(n)]

    for i in range(n):
        flag = True
        while (flag):
            rand_element = 1 + int(random.random() * 100) % (n**2+1)
            if (not(is_element_in_container(elements, rand_element))): continue
            array[i] = rand_element
            elements.remove(rand_element)
            flag = False
    return array    

def get_rand_matr(n):
    elements = [i for i in range(1, n**2+1)]
    matr = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            flag = True
            while (flag):
                rand_element = 1 + int(random.random() * 100) % (n**2+1)
                if (not(is_element_in_container(elements, rand_element))): continue
                matr[i][j] = rand_element
                elements.remove(rand_element)
                flag = False
    return matr


#--- assisting functions 

def is_element_in_container(arr, number):
    for i in arr:
        if (i == number): return True
    return False
