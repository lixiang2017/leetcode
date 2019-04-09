class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

if __name__ == "__main__":
    str = "Hello"
    assert Solution().toLowerCase(str) == "hello"

    str = "here"
    assert Solution().toLowerCase(str) == "here"

    str = "LOVELY"
    assert Solution().toLowerCase(str) == "lovely"