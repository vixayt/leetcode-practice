class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        current, result = '', []
        for char in searchWord:
            current += char
            i = bisect.bisect_left(products, current)
            result.append([product for product in products[i: i+3] if product.startswith(current)])
        return result
