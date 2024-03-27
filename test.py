from llm.openaiLLM import section_fill

sop_description = "sop for finance filing"
section_template = """
Section 3: Implementation
Subsections detailing the steps or procedures to be followed, including:

Specific conditions or requirements for different scenarios.
Detailed instructions for using equipment or materials (e.g., transport cases, gel packs).
Considerations for indoor vs. outdoor transport, time limits, and temperature-specific guidelines.
"""

example_from_knowledge = """
1. Sequence of Job Steps
Break down the task or operation into the basic steps to complete the work task and/or
operate the item of plant/equipment. For example, what is done first, what is done next and
so on.
Record each step of the task in the order of normal sequence, making sure you describe
what is done, not how it is done. As a working guide, the task description should be
contained within approximately 10 broad steps. This of course may vary depending on the
complexity and the hazardous nature of the job.
2. Potential Hazards/Risks
For each step in the work task, list the potential hazards/risks that are reasonably
foreseeable.
The following should be explored in relation to the steps, and the person(s) doing the task -
Can they:
• be struck by or contacted by anything
• strike against or contact anything
• be caught in, on, or under or between anything
• fall from height or be exposed to falling objects
• manual handling
• be exposed to welding rays, fumes, light, electricity or other forms of energy
• be exposed to stored energy
• be exposed to hazardous chemicals etc.
"""



test_delimiiter = "$$$"

test_layout = f"""
Title Page
Title: [Title of the SOP]
{test_delimiiter}
Subtitle: [Subtitle or additional details if necessary]
Logo or Image: [Institution's logo or relevant image]
Contact Information: [Institution Name, Address, Contact Details]
{test_delimiiter}
Document Header
STANDARD OPERATIONAL PROCEDURE (SOP)
{test_delimiiter}
Topic: [Specific topic of the SOP, e.g., Transport of Medications with Temperature and Humidity Monitoring]
{test_delimiiter}
Section 1: Purpose
Brief paragraph detailing the purpose of the SOP, focusing on the main goal or objective.
{test_delimiiter}
Section 2: Definitions
A list of terms and definitions relevant to the SOP, each with a brief explanation. This section can include items like key materials, devices, roles, or concepts specific to the topic.
{test_delimiiter}
Section 3: Implementation
Subsections detailing the steps or procedures to be followed, including:
Specific conditions or requirements for different scenarios.
Detailed instructions for using equipment or materials (e.g., transport cases, gel packs).
Considerations for indoor vs. outdoor transport, time limits, and temperature-specific guidelines.
{test_delimiiter}
Section 4: Responsibilities
Subsections outlining the responsibilities of different roles involved in the process, such as:
Personnel preparing for transport.
Transporters.
Receiving staff or destination responsibilities.
{test_delimiiter}
Section 5: Additional Guidelines
Any specific packing instructions or considerations for the transport of materials.
Instructions for completing and handling forms or documentation related to the process.
{test_delimiiter}
Section 6: Contact Information
Detailed contact information for relevant departments or personnel, including phone numbers and email addresses.
Appendix or Attachments
Any additional forms, checklists, or templates referenced in the SOP.
Optional: A Q&A section addressing common questions or scenarios related to the SOP.
{test_delimiiter}
Footer
Copyright and disclaimer information.
Contact details for further information or support.
"""

# resp = section_fill(sop_description, section_template, example_from_knowledge)

from vectordb.elastic import index_file
# resp = index_file("./data/new4_sop-ids-transport-temp-humidity-monitoring.pdf")
# resp = index_file("./data/Standard-Operating-Procedures-for-Pharmaceutical-Care-Delivery-in-Health-Facilities.pdf")
from document_generator.generator import fill_layout

fill_layout("sop for medicine management", test_layout, test_delimiiter)