import math

def getVal(a,b,c,d):
    return (math.sqrt(a) + math.sqrt(b)) * (math.sqrt(c) - math.sqrt(d))

out = []
nums = []

mx = 0
mxVal = 0
for b in range(1, 100):
    for a in range(b+1, 100):
        for c in range(1, 100):
            for d in range(1, c):
                if len({a,b,c,d}) < 4:
                    continue
                val = getVal(a,b,c,d)
                if abs(val - round(val)) < 1e-6:
                    val = round(val)
                    out.append(val)
                    nums.append([a,b,c,d])
                    if val > mx:
                        mx = val
                        mxVal = [a,b,c,d]

print(out)
print(nums)
print(mx)
print(mxVal)