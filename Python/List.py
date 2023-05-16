gym = ["Biceps","Triceps","Chest","Shoulders","Back","Legs"]
print(gym[2])
nums = [1,10,20,5,2,9,3,6]
#print(nums.sort())
#print(nums.reverse())
print(nums[::])
print(nums[::-1]) #reverse
print(len(nums))
print(max(nums))
print(min(nums))
nums.append(7)
print(nums)
nums.insert(1,2)
nums.remove(9) #Removes number 9
nums.pop()
#TUPLE - IMMUTABLE
num1 = (1,3,8,2,4,1)
print(num1)
#num1[2]=3  INVALID
#Swapping 2 numbers
a=3
b=5
a,b = b,a
print(a)