# Given an integer n, count the total number of digit 1 appearing in all non-negative integers 
# less than or equal to n.
# TC: O(nlogn)
# SC: O(1) as we are not using any extra space


def countDigitOne(n):
    cnt = 0
    for i in range(1, n+1):
        # typecasting integer to string
        st = str(i)

        # counting 1's with count function
        cnt += st.count("1")
    
    return cnt

# n = 0
n = 13
print(countDigitOne(n))


##### OR  ##############


# function to count the
# frequency of 1.


# TC : O(logn)
def countDigitOne(n):
	cnt = 0
	i = 1
	while(i <= n):
		divider = i * 10
		cnt += (int(n / divider) * i + min(max(n % divider -i + 1, 0), i))
		i *= 10
	
	return cnt

# Driver Code
n = 13
print(countDigitOne(n))
