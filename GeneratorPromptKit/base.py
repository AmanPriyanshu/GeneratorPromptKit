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

    def generate_dataset(self, input_domain, num_topics, num_subtopics, num_questions):
        topics = self._extract_topics(input_domain, num_topics)
        dataset = []

        for topic in tqdm(topics, desc="Generating Dataset"):
            subtopics = self._extract_subtopics(topic, num_subtopics)
            for subtopic in subtopics:
                question, answer = self._generate_question_answer(topic, subtopic)
                dataset.append({"question": question, "answer": answer})

                if len(dataset) >= num_questions:
                    return dataset

        return dataset

    def _extract_topics(self, input_domain, num_topics):
        prompt = create_topic_extraction_prompt(input_domain)
        response = send_query_to_llm(self.client, self.llm_model, [{"role": "system", "content": "You're a Topic Generator."}, {"role": "user", "content": prompt}], topic_generation_function_template)
        print(response)
        return topics[:num_topics]

    def _extract_subtopics(self, topic, num_subtopics):
        prompt = create_subtopic_and_question_extraction_prompt(topic)
        response = send_query_to_llm(prompt, self.llm_model, self.api_key)
        subtopics = parse_llm_response(response)
        return subtopics[:num_subtopics]

    def _generate_question_answer(self, topic, subtopic):
        prompt = create_generator_prompt(topic, subtopic)
        response = send_query_to_llm(prompt, self.llm_model, self.api_key)
        question, answer = parse_llm_response(response)
        return question, answer