import random
from .support import randomness_boosters, grounding_phrase, indirect_question_generators

def create_topic_extraction_prompt(input_domain, num_topics=10):
    prompt = f"""
    Input Domain: {input_domain}

    Instructions:
    Extract a list of {num_topics} relevant topics from the given input domain.
    Ensure the topics are diverse and cover various aspects of the domain.
    """

    return prompt

def create_subtopic_and_question_extraction_prompt(input_domain, num_topics, topic, topic_list, topic_index, num_subtopics, use_subtopic_index=False, subtopic_index=None):
    topic_index += 1
    prefix_prompt = f"""
    Input Domain: {input_domain}

    Instructions:
    Extract a list of {num_topics} relevant topics from the given input domain. Ensure the topics are diverse and cover various aspects of the domain. 
    
    Then, extract the topic at Topic at Index - {topic_index}.
    """
    topics_string = "\n".join([str(i+1)+". "+t for i,t in enumerate(topic_list)])
    prefix_response = f"""
    List of Topics:
    {topics_string}

    Topic at Index - {topic_index}: {topic}
    """
    prompt = f"""
    Topic at Index - {topic_index}: {topic}

    Instructions:
    Generate a list of {num_subtopics} subtopics related to the given topic: {topic}.
    The subtopics should be specific and cover different facets of the main topic.
    """

    if use_subtopic_index:
        if subtopic_index is None:
            raise Exception("Please provide subtopic_index")
        subtopic_index += 1
        prompt += f"""
        Select the subtopic at index {subtopic_index} from the generated list.

        Instructions for Question Generation:
        {random.choice(indirect_question_generators)}
        {grounding_phrase}
        {random.choice(randomness_boosters)}
        """
    else:
        prompt += f"""
        Randomly sample a subtopic from the generated list.
        State the randomly selected subtopic.

        Now, Instructions for Question Generation:
        {random.choice(indirect_question_generators)}
        {random.choice(randomness_boosters)}
        {grounding_phrase}
        """

    return prompt, prefix_prompt, prefix_response