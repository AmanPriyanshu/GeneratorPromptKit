import os
from openai import OpenAI
from tqdm import tqdm
from .prompts import create_topic_extraction_prompt, create_subtopic_and_question_extraction_prompt
from .llm_integration import send_query2gpt as send_query_to_llm
from .function_templates import topic_generation_function_template, question_and_answer_generation_function_template, question_generation_function_template
from .utils import GPKDataset
import random

class GeneratorPromptKit:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm_model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=self.api_key.strip())
        self.topic_generation_function_template = topic_generation_function_template[0]
        self.question_and_answer_generation_function_template = question_and_answer_generation_function_template[0]
        self.question_generation_function_template = question_generation_function_template[0]

    def reconfigure_function_templates(self, num_topics, num_subtopics):
        self.topic_generation_function_template["parameters"]["properties"]["topic_array"]["minItems"] = num_topics
        self.topic_generation_function_template["parameters"]["properties"]["topic_array"]["maxItems"] = num_topics
        self.question_and_answer_generation_function_template["parameters"]["properties"]["subtopic_array"]["minItems"] = num_subtopics
        self.question_and_answer_generation_function_template["parameters"]["properties"]["subtopic_array"]["maxItems"] = num_subtopics
        self.question_generation_function_template["parameters"]["properties"]["subtopic_array"]["minItems"] = num_subtopics
        self.question_generation_function_template["parameters"]["properties"]["subtopic_array"]["maxItems"] = num_subtopics

    def generate_dataset(self, input_domain, num_topics, num_subtopics, num_datapoints, use_subtopic_index=False, subtopic_index=None, generate_answers=True):
        num_questions = num_datapoints
        self.reconfigure_function_templates(num_topics, num_subtopics)
        topics = self._extract_topics(input_domain, num_topics)
        dataset = []
        question_per_topic = num_questions//num_topics + 1
        bar = tqdm(range(question_per_topic*len(topics)), desc="Generating Dataset")
        for topic_index, topic in enumerate(topics):
            for question_id in range(question_per_topic):
                prompt, prefix_prompt, prefix_response = create_subtopic_and_question_extraction_prompt(input_domain, num_topics, topic, topics, topic_index, num_subtopics, use_subtopic_index=use_subtopic_index, subtopic_index=subtopic_index)
                messages = [{"role": "system", "content": "You're a helpful AI"}, {"role": "user", "content": prefix_prompt}, {"role": "assistant", "content": prefix_response}, {"role": "user", "content": prompt}]
                if generate_answers:
                    response = send_query_to_llm(self.client, self.llm_model, messages, function_template=self.question_and_answer_generation_function_template)
                    to_record = {"topic": topic, "subtopic": response["selected_subtopic"], "question": response["question"], "answer": response["answer"]}
                else:
                    response = send_query_to_llm(self.client, self.llm_model, messages, function_template=self.question_generation_function_template)
                    to_record = {"topic": topic, "subtopic": response["selected_subtopic"], "question": response["question"]}
                dataset.append(to_record)
                bar.update()
        bar.close()
        random.shuffle(dataset)
        return GPKDataset(dataset)

    def _extract_topics(self, input_domain, num_topics):
        prompt = create_topic_extraction_prompt(input_domain)
        response = send_query_to_llm(self.client, self.llm_model, [{"role": "system", "content": "You're a Topic Generator."}, {"role": "user", "content": prompt}], topic_generation_function_template[0])["topic_array"]
        topics = [t["topic"] for t in response]
        return topics[:num_topics]