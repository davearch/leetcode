class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["eat","tea","tan","ate","nat","bat"]
          ate,  bat,  eat,  tea,  tan,  nat
          
          {sortedWord: [word, word, word]}
          
          aet,  aet,  ant,  aet,  ant,  abt
          {aet}
        
        O(1)
        create hashmap of sortedWord to list of anagrams
        O(n*mlogm)
        for each word, compare the sorted version with a key in the map
        O(1)
        if the key exists, append the current word to it's list
        O(1)
        else, create new entry with word
        O(n)
        create an output array and loop through map appending each list
        O(1)
        return output array
        """
        sortedWordToListOfAnagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in sortedWordToListOfAnagrams:
                sortedWordToListOfAnagrams[sorted_word].append(word)
            else:
                sortedWordToListOfAnagrams[sorted_word] = [word]
        return sortedWordToListOfAnagrams.values()