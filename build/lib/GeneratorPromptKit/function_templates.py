topic_generation_function_template = [
    {
        "name": "topic_generator",
        "description": "You are an AI assistant whose objective is to employ all its world knowledge to generate a list of topics, given a specific domain or direction.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic_array": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "topic": {
                                "description": "One of the diverse set of topics under the given domain.",
                                "type": "string",
                                "enum": []
                            },
                        },
                        "required": ["topic"],
                    },
                    "description": "An array of topics.",
                    "minItems": 0,
                    "maxItems": 0,
                }
            },
            "required": ["topic_array"]
        }
    }
]

question_generation_function_template = [
    {
        "name": "subtopic_and_question_generator",
        "description": "You are an expert assistant whose objective is to generate subtopics based on a given topic within a domain. Following which you've to generate a expert question based on a subtopic selected. Essentially you generate subtopics and focused questions.",
        "parameters": {
            "type": "object",
            "properties": {
                "subtopic_array": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "subtopic": {
                                "description": "One of the diverse set of topics under the given domain.",
                                "type": "string",
                                "enum": []
                            },
                        },
                        "required": ["subtopic"],
                    },
                    "description": "An array of subtopics.",
                    "minItems": 0,
                    "maxItems": 0,
                },
                "selected_subtopic": {
                    "type": "string",
                    "description": "From the generated list of subtopics, the particular/selected subtopic"
                },
                "question": {
                    "type": "string",
                    "description": "From the selected subtopic an expert question."
                }
            },
            "required": ["subtopic_array", "selected_subtopic", "question"]
        }
    }
]

question_and_answer_generation_function_template = [
    {
        "name": "subtopic_question_and_expert_answer_generator",
        "description": "You are an expert assistant whose objective is to generate subtopics based on a given topic within a domain. Following which you've to generate a expert question based on a subtopic selected and also an expert answer. Essentially you generate subtopics, focused questions, and expert answers.",
        "parameters": {
            "type": "object",
            "properties": {
                "subtopic_array": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "subtopic": {
                                "description": "One of the diverse set of topics under the given domain.",
                                "type": "string",
                                "enum": []
                            },
                        },
                        "required": ["subtopic"],
                    },
                    "description": "An array of subtopics.",
                    "minItems": 0,
                    "maxItems": 0,
                },
                "selected_subtopic": {
                    "type": "string",
                    "description": "From the generated list of subtopics, the particular/selected subtopic"
                },
                "question": {
                    "type": "string",
                    "description": "From the selected subtopic an expert question."
                },
                "answer": {
                    "type": "string",
                    "description": "For the given question an expert answer."
                }
            },
            "required": ["subtopic_array", "selected_subtopic", "question", "answer"]
        }
    }
]