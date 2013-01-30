# -*- coding: utf-8 -*-

example_null_json = """
    null
"""

example_null_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "null",
        "id": "#",
        "required": true
    }
"""

example_int_json = """
    1
"""

example_int_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "number",
        "id": "#",
        "required": true
    }
"""


example_json_1 = """
    {
        "item_1": "string_value_1",
        "item_2": 123,
        "item_3": [1, 2, 3],
        "item_4": true,
        "item_5": null,
        "item_6": { "key": "value"},
        "item_7": {
            "item_7.1": "string_value_1",
            "item_7.2": 123,
            "item_7.3": [1, 2, 3],
            "item_7.4": true,
            "item_7.5": null,
            "item_7.6": { "key": "value"}
        }
    }
"""

example_json_schema_1 = """
    {
        "type": "object",
        "$schema": "http://json-schema.org/draft-03/schema",
        "id": "#",
        "required": true,
        "properties": {
            "item_1": {
                "type": "string",
                "id": "item_1",
                "required": true
            },
            "item_2": {
                "type": "number",
                "id": "item_2",
                "required": true
            },
            "item_3": {
                "type": "array",
                "id": "item_3",
                "required": true,
                "items": {
                    "type": "number",
                    "id": "0",
                    "required": true
                }
            },
            "item_4": {
                "type": "boolean",
                "id": "item_4",
                "required": true
            },
            "item_5": {
                "type": "null",
                "id": "item_5",
                "required": true
            },
            "item_6": {
                "type": "object",
                "id": "item_6",
                "required": true,
                "properties": {
                    "key": {
                        "type": "string",
                        "id": "key",
                        "required": true
                    }
                }
            },
            "item_7": {
                "type": "object",
                "id": "item_7",
                "required": true,
                "properties": {
                    "item_7.1": {
                        "type": "string",
                        "id": "item_7.1",
                        "required": true
                    },
                    "item_7.2": {
                        "type": "number",
                        "id": "item_7.2",
                        "required": true
                    },
                    "item_7.3": {
                        "type": "array",
                        "id": "item_7.3",
                        "required": true,
                        "items": {
                            "type": "number",
                            "id": "0",
                            "required": true
                        }
                    },
                    "item_7.4": {
                        "type": "boolean",
                        "id": "item_7.4",
                        "required": true
                    },
                    "item_7.5": {
                        "type": "null",
                        "id": "item_7.5",
                        "required": true
                    },
                    "item_7.6": {
                        "type": "object",
                        "id": "item_7.6",
                        "required": true,
                        "properties": {
                            "key": {
                                "type": "string",
                                "id": "key",
                                "required": true
                            }
                        }
                    }
                }
            }
        }
    }
"""