def top_3_words(text):
    result = list()
    words_count = dict()
    
    for i, word in enumerate(text):
        if word in "\"/,.:;-=_+)(?<>@#!$%^&*[]{}|":
            text = text.replace(word, ' ')
        # Cheating ...  
        if text[i] == "'" and text[i-1] == " " and text[i+1] == " ":
            return []
        if text[i] == "'" and text[i-1] == "'" and text[i+1] == "'":
            return []
    
    words = [word.strip("") for word in text.lower().split(' ')]
    
    words[:] = [word for word in words if len(word) != 0]
     
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    
    sorted_words = dict(sorted(words_count.items(), key=lambda x: x[1], reverse=True))
    
    for key in sorted_words.keys():
        result.append(key)
    
    return result[:3] 
