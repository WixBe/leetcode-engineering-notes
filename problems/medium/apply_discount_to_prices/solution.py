class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        modified_words = []

        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price = float(word[1:])
                discounted_price = price * (1 - discount/100)
                formatted_price = f"${discounted_price:.2f}"
                modified_words.append(formatted_price)
            else:
                modified_words.append(word)
        modified_sentence = ' '.join(modified_words)
        return modified_sentence