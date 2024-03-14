nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

n = len(nums)

l = 0

r = 0
maxSlide = 0
currentSlide = 0
while r < n:
    if(nums[r] == 1):
        currentSlide += 1
        maxSlide = max(maxSlide, currentSlide)
    elif(k > 0):
        currentSlide += 1
        maxSlide = max(maxSlide, currentSlide)
        k -= 1
    else:
        currentSlide = 0
    r += 1
print(maxSlide)
