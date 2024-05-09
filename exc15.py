nums = []
for i in range(6):
    num = int(input(f"DIGITE UM {i + 1} NUMERO: "))
    nums.append(num)
avg = sum(nums) / len(nums)
avg_up = []
avg_down = []
for num in nums:
    if num >= avg:
        avg_up.append(num)
    else:
        avg_down.append(num)
print(f"NUMEROS ABAIXO DA MEDIA: {avg_down}")
print(f"NUMEROS ACIMA DA MEDIA: {avg_up}")