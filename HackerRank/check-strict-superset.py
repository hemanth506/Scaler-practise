# Some test cases failed

# A = set(map(int, input().split()))
# lenA = len(A)
# n = int(input())

A = set(['51', '28', '10', '61', '99', '31', '55', '7', '88', '48', '18', '80', '18', '36', '49', '21', '36', '1', '49', '53', '11', '78', '46', '87', '82', '28', '76', '50', '89', '31', '14', '81', '87', '39', '3', '69', '26', '18', '85', '18', '23', '43', '75', '5', '64', '47', '34', '19', '2', '54', '92', '45', '79', '80', '59', '16', '75', '80', '55', '24', '56', '74', '76', '31', '22', '74', '20', '93', '79', '81', '12', '57', '21', '79', '65', '32', '57', '37', '47', '84', '82', '28', '72', '15', '53', '50', '86', '58', '83', '88', '3', '44', '76', '63', '32', '14', '13', '38', '29', '70', '38', '4', '71', '15', '45', '4', '94', '24', '46', '6', '95', '48', '15', '82', '92', '62', '6', '67', '38', '20', '60', '78', '37', '84', '32', '39', '51', '88', '13', '99', '6', '3', '64', '37', '83', '68', '18', '51', '98', '37', '11', '48', '63', '97', '30', '90', '73', '44', '63', '25', '78', '12', '25', '91', '36', '38', '59', '12', '36', '51', '58', '61', '82', '91', '31', '41', '36', '99', '28', '50', '28', '64', '22', '56', '26', '39', '75', '53', '8', '41', '94', '86', '35', '69', '48', '17', '80', '32', '12', '29', '2', '33', '51', '79', '58', '74', '91', '46', '6', '54', '66', '0', '75', '60', '30', '95', '57', '36', '70', '32', '83', '1', '88', '27', '57', '2', '67', '28', '18', '51', '61', '16', '40', '79', '96', '78', '27', '72', '85', '45', '73', '12', '89', '31', '11', '24', '42', '94', '22', '84', '1', '67', '8', '62', '80', '77', '81', '58', '1', '6', '63', '30', '64', '37', '44', '60', '11', '14', '68', '28', '81', '86', '30', '17', '81', '14', '30', '44', '64', '89', '7', '94', '89', '13', '59', '88', '34', '42', '6', '51', '10', '19', '66', '91', '46', '22', '41', '34', '98', '4', '26', '90', '84', '90', '44', '90', '84', '13', '36', '6', '97', '21', '30', '52', '46', '15', '83', '89', '45', '83', '33', '11', '3', '18', '6', '82', '17', '23', '13', '91', '27', '39', '76', '11', '86', '12', '97', '64', '51', '48', '84', '35', '66', '15', '48', '32', '99', '11', '18', '93', '11', '85', '71', '63', '57', '76', '1', '80', '45', '19', '7', '39', '80', '70', '78', '3', '17', '51', '14', '99', '47', '83', '17', '82', '23', '59', '59', '41', '77', '22', '7', '35', '22', '98', '59', '90', '80', '72', '60', '67', '22', '75', '3', '99', '18', '81', '47', '48', '18', '98', '18', '37', '47', '65', '98', '86', '82', '5', '30', '87', '25', '17', '97', '60', '93', '33', '99', '89', '62', '98', '40', '27', '70', '57', '49', '93', '46', '11', '38', '94', '43', '75', '61', '75', '55', '45', '26', '9', '84', '89', '40', '87', '14', '61', '31', '99', '53', '6', '83', '55', '15', '95', '46', '8', '58', '73', '58', '57', '9', '7', '49', '21', '31', '88', '31', '32', '61', '30', '19', '69', '78', '33', '3', '0', '70', '73', '40', '91', '91', '96', '72', '79', '0', '41', '91', '51', '10', '80', '50', '77', '30', '38', '1', '85', '56', '90', '78', '36', '31', '0', '82', '12', '95', '28', '1', '65', '72', '75', '89', '54'])
lenA = len(A)
n = 20
class Solution:
    def solve(self, A, lenA, n):
        OnlyTrue = []
        for i in range(0, n):
            # otherSet = set(map(int, input().split()))
            otherSet = set(['81', '79', '97', '20', '68', '23', '19', '12', '53', '86', '26', '36', '4', '64', '10', '43', '12', '75', '98', '30', '12', '33', '27', '1', '32', '68', '64', '49', '99', '10', '16', '9', '7', '47', '23', '29', '30', '94', '57', '25', '38', '15', '57', '33', '79', '28', '45', '98', '20', '50', '34', '93', '6', '14', '9', '29', '56', '13', '44', '67', '5', '23', '32', '38', '78', '20', '55', '35', '25', '91', '64', '10', '47', '32', '97', '44', '85', '65', '87', '36', '91', '88', '78', '6', '48', '86', '67', '56', '44', '18', '98', '39', '10', '80', '47', '65', '49', '98', '63', '21'] )
            lenOtherSet = len(otherSet)
            if lenA > lenOtherSet:
                unionValue = otherSet.union(A)
                if lenOtherSet == unionValue:
                    OnlyTrue.append(True)
                else:
                    return False
            else:
                return False
                
        return OnlyTrue
                
                
sol = Solution()
print(sol.solve(A, lenA, n))