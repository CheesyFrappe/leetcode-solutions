"""
    1108 - Defanging an IP Address - Easy
    https://leetcode.com/problems/defanging-an-ip-address/
    Topics: String

    Runtime complexity: O(1)
    Spacetime complexity: O(1)
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')