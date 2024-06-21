from GeneratorPromptKit import GeneratorPromptKit

with open("openai_api.key", "r") as f:
    key = f.read()

def main():
    gpk = GeneratorPromptKit(api_key=key)
    input_domain = "Computer Science"
    dataset = gpk.generate_dataset(input_domain, num_topics=10, num_subtopics=5, num_datapoints=100)
    dataset.save('computer_science_dataset.json')

if __name__=='__main__':
    main()