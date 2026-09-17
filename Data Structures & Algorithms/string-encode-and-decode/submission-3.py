class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            for c in s:
                result = result + c
            result = result + "™"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current = ""
        for c in s:
            if c != "™":
                current = current + c
            else:
                result.append(current)
                current = ""
            
        return result

