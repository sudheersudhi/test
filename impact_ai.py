
# Total no of class days = N-1
# suppose N=5
#
# No of class days = 4
#
# consider 1 as present and 0 as absent.
#
# different ways  to attend class in 4 days = 0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111
#
# here 0000 will be avoided.
#
# total ways of attending class = 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
# so total ways = 15

def totalWays(n):
    if n <= 4:
        total_ways = pow(2, n - 1)
        probability = (pow(2, n-1) - total_ways) / total_ways
        print(
            "The number of ways to attend classes over {x} days = {days}".format(
            x=n, days=total_ways))
        print('The probability that you will miss your graduation ceremony. = {p}'.format(p=probability))
    else:
        total_ways = pow(2, n - 1) - (2 * (n - 4) - 1)
        probability = (pow(2, n-1) - total_ways) / total_ways
        print(
            "The number of ways to attend classes over {x} days = {days}.".format(
            x=n, days=total_ways))
        print(
            'The probability that you will miss your graduation ceremony. = {p}'.format(
                p=probability))


n = 4
print(totalWays(n))
