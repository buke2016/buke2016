class Autocomplete:
    def __init__(self, suggestions):
        # Initialize with a list of suggestions, each as a tuple (string, weight).
        self.suggestions = sorted(suggestions)  # Preprocess by sorting alphabetically.

    def binary_search(self, query):
        # Binary search to find all suggestions that start with the query string.
        left, right = 0, len(self.suggestions)
        results = []

        while left < right:
            mid = (left + right) // 2
            suggestion, weight = self.suggestions[mid]

            if suggestion.startswith(query):
                # If the suggestion starts with the query, add it to results.
                results.append((suggestion, weight))

            if suggestion < query:
                left = mid + 1
            else:
                right = mid

        return results

    def autocomplete(self, query):
        # Process an autocomplete query and return suggestions sorted by weight.
        matching_suggestions = self.binary_search(query)
        
        # Sort matching suggestions by weight in descending order.
        matching_suggestions.sort(key=lambda x: x[1], reverse=True)
        
        return matching_suggestions

# Example usage:
suggestions = [("apple", 5), ("banana", 3), ("cherry", 7), ("date", 2), ("elderberry", 6)]
autocomplete_system = Autocomplete(suggestions)

query = "b"
results = autocomplete_system.autocomplete(query)
print(results)  # Output: [('banana', 3)]
