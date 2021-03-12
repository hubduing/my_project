optimal = int(input())
hours = int(input())
minutes = int(input())

print((hours * 60 + minutes + optimal) // 60)
print((hours * 60 + minutes + optimal) % 60)
