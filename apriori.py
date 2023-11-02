from efficient_apriori import apriori

num = int(input("Enter the number of transactions = "))
arr = []
print("Enter the transactions:")
for _ in range(num):
    transaction = list(map(int, input().split()))
    arr.append(transaction)

min_support = float(input("Enter the minimum support = "))
min_confidence = float(input("Enter the minimum confidence = "))

itemsets, rules = apriori(arr, min_support=min_support, min_confidence=min_confidence)  #calling apriori function

print("\nFrequent itemsets:")
for itemset in itemsets:
    print(itemset)   

print("\nAssociation rules :")
for rule in rules:
    print(f"{rule.lhs} -> {rule.rhs} | Confidence: {rule.confidence}")
