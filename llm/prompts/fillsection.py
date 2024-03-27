

_ASSISTANT_DESC = "You are an helpful assistant who generate section in a SOP document using description of sop, section structure, and writing style of example provided document chunk"
_VARIABLE_DESC = """
"""
FILLSECTION_PROMPT = f"""{_ASSISTANT_DESC}""" + \
"""refer the following document chunk writing style, 'example_from_knowledge' - "{example_from_knowledge}".
   And the section template of SOP document, 'section_template' - "{section_template}".
   For the sop description 'sop_description' - "{sop_description}"
   Instruction : 
        if 'example_from_knowledge' is relevant to the 'sop_description' use the content from 'example_from_knowledge' too.
section HTML:
"""
# sop_description, section structure, example_from_knowledge







