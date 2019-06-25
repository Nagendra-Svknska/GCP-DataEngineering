normal_set = set(["a", "b", "c"])
normal_set2=set(["1","2","c"])
n1=normal_set&normal_set2
print(n1)
n=normal_set|normal_set2
print(n)
# Adding an element to normal set is fine
normal_set.add("d")

print("Normal Set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("Frozen Set")
print(frozen_set)
