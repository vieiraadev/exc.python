def soma_recursiva(nums, n):
    if n == 0:
        return 0
    else:
        return nums[n-1] + soma_recursiva(nums, n-1)
nums = [1, 2, 3, 4, 5]
n = len(nums)
resultado = soma_recursiva(nums, n)
print("A soma dos elementos da lista é:", resultado)