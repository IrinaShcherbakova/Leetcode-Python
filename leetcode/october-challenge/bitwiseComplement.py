class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = self.int_to_binary(N)
        bin_str = ""
        for bit in binary:
            bin_str += ("1" if bit == 0 else "0")
        return int(bin_str, 2)
     
    
    def int_to_binary(self, number):
        binary = []
        if (number != 0):
            while (number >= 1):
                if (number % 2 == 0):
                    binary.append(0)
                    number = number/2
                else:
                    binary.append(1)
                    number = (number-1)/2

        else:
            binary.append(0)

        return binary[::-1]
