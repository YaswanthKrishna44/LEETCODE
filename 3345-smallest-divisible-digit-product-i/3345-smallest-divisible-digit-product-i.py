class Solution:

  def smallestNumber(self, n: int, t: int) -> int:
    x = n
    while True:
      # Calculate the product of digits of x
      product = 1
      temp = x
      while temp > 0:
        product *= temp % 10
        temp //= 10

      # Check if product is divisible by t
      if product % t == 0:
        return x

      x += 1
        