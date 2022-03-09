beginning = int(input("Enter some number: "))
end = int(input("Enter bigger number: "))

cube_list = []

for i in range(beginning, end+1):
    cubed = i**3
    print(i, "cubed:", cubed)
    cube_list.append(cubed)
print("All cubes:", cube_list)

