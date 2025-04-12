import random

madlib_templates = [
    "Today I went to the {place} and saw a {adjective} {noun} {verb}ing happily.",
    "In the {adjective} world of {place}, a {noun} loved to {verb} every day.",
    "Once upon a time in {place}, a {adjective} {noun} decided to {verb}."
]

words_to_prompt = {
    "adjective": "Enter an adjective: ",
    "noun": "Enter a noun: ",
    "verb": "Enter a verb: ",
    "place": "Enter a place: "
}

def get_user_inputs(words):
    inputs = {}
    for key, prompt in words.items():
        word = input(prompt)
        inputs[key] = word
    return inputs

def generate_unique_story():
    template = random.choice(madlib_templates)
    user_inputs = get_user_inputs(words_to_prompt)
    story = template.format(**user_inputs)
    print("\nHere is your unique Mad Libs story:")
    print(story)

if __name__ == "__main__":
    generate_unique_story()
