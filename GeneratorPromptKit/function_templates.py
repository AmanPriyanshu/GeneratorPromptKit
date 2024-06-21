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