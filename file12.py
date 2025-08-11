import re
import textwrap

# Long block of text (sample article or story)
long_text = """
    In a distant future where humanity has colonized the stars, the remnants of Earth’s culture are preserved in digital libraries scattered across the galaxy. 
    These libraries are not just collections of knowledge, but monuments to what once was, maintained by caretakers who have never set foot on the planet they are sworn to remember. 
    Among these caretakers is Aria, a young woman born on a space station orbiting a dead world. Her only connection to Earth is through the words and images stored in the archives: 
    poems written under blue skies, songs sung in rain, films capturing the laughter of children running through fields of green. One day, Aria discovers a corrupted file 
    marked “Project Eden.” Within it lies a fragment of a map, cryptic coordinates, and a phrase in an ancient language: “Terra resurgens.” Earth reborn.

    Driven by curiosity and a longing she can’t explain, Aria embarks on a journey across sectors, piecing together fragments left behind by a civilization that lost hope. 
    Along the way, she meets others who have found similar clues—scholars, adventurers, even pirates—each with their own vision of what Earth was and what it could be. 
    As they converge on the final destination, truths are unearthed: Earth was never fully dead, only forgotten and hidden. Now, the descendants of those who once fled its 
    dying ecosystems must decide whether to return and rebuild or let the planet rest as a memory. “Terra resurgens.” Earth reborn. And with it, humanity’s second chance.
"""

# Function to analyze text
def analyze_text(text):
    words = text.split()
    word_count = len(words)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip() != ''])
    average_word_length = sum(len(word) for word in words) / word_count
    average_sentence_length = word_count / sentence_count
    reading_level = 0.39 * average_sentence_length + 11.8 * average_word_length - 15.59  # Flesch–Kincaid style estimate

    print("Text Analysis Report")
    print("-" * 40)
    print(f"Total Words: {word_count}")
    print(f"Total Sentences: {sentence_count}")
    print(f"Average Word Length: {average_word_length:.2f}")
    print(f"Average Sentence Length: {average_sentence_length:.2f} words")
    print(f"Estimated Reading Level (Grade): {reading_level:.2f}")
    print("-" * 40)
    print("\nWrapped Text Preview:\n")
    print(textwrap.fill(text.strip(), width=80))

# Run the analysis
analyze_text(long_text)

