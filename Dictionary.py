food = {"Person1 ":"Rice","Person2":"Dal","Person3":"Roti","Person4":{"Morning":"Fruits","Afternoon":"rice","Night":"Maggi"}}
print(food)
print(food["Person4"])
food["Person5"]="Burger"
print(food)
food1 = food.copy()  # Copy is used for creating a duplicate of food so that "Food" dictionary won't be changed when
# we make changes in food1
del food1["Person2"]
print(food1)
print(food.get("Person2"))
food.update({"Pramod":"Healthy Food"})
print(food)
print(food.keys())
print(food.items())
