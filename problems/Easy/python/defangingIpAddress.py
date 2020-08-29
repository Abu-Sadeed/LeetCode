class Solution:
    def defangIPaddr(self, address: str) -> str:
        li = list(address.split("."))
        result = '[.]'.join(str(i) for i in li)
        return result