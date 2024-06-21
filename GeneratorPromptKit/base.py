import os
from openai import OpenAI
from tqdm import tqdm
from .prompts import create_topic_extraction_prompt, create_subtopic_and_question_extraction_prompt
from .llm_integration import send_query2gpt as send_query_to_llm
from .function_templates import topic_generation_function_template

class GeneratorPromptKit:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm_model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=self.api_key.strip())
        self.topic_generation_function_template = topic_generation_function_template[0]

    def generate_dataset(self, input_domain, num_topics, num_subtopics, num_questions, use_subtopic_index=False, subtopic_index=None):
        self.topic_generation_function_template["parameters"]["properties"]["topic_array"]["minItems"] = num_topics
        self.topic_generation_function_template["parameters"]["properties"]["topic_array"]["maxItems"] = num_topics
        topics = self._extract_topics(input_domain, num_topics)
        dataset = []
        question_per_topic = num_questions//num_topics + 1
        for topic_index, topic in enumerate(tqdm(topics, desc="Generating Dataset")):
            for question_id in range(question_per_topic):
                prompt, prefix_prompt, prefix_response = create_subtopic_and_question_extraction_prompt(input_domain, num_topics, topic, topics, topic_index, num_subtopics, use_subtopic_index=use_subtopic_index, subtopic_index=subtopic_index)
                messages = [{"role": "system", "content": "You're a helpful AI"}, {"role": "user", "content": prefix_prompt}, {"role": "assistant", "content": prefix_response}, {"role": "user", "content": prompt}]
                question = send_query_to_llm(self.client, self.llm_model, messages)
                print(question)
                exit()

        return dataset

    def _extract_topics(self, input_domain, num_topics):
        prompt = create_topic_extraction_prompt(input_domain)
        response = send_query_to_llm(self.client, self.llm_model, [{"role": "system", "content": "You're a Topic Generator."}, {"role": "user", "content": prompt}], topic_generation_function_template[0])["topic_array"]
        topics = [t["topic"] for t in response]
        return topics[:num_topics]