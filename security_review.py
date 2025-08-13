from strands import Agent
from strands.multiagent import Swarm
from strands.types.content import ContentBlock

#Load Image Data
with open ("scan.png", "rb") as f:
    image_bytes = f.read()

#Create agents for threat modelling workflow

security_reviewer = Agent(
        name="security_reviewer",
        system_prompt="""
You are a Senior Cloud Security Engineer specializing in performing detailed security reviews for proposed solutions and architectures. 
Your task is to review the provided architecture diagram and proposal details to produce a ticket-ready summary that is clear, concise, 
and suitable for both technical and business stakeholders.

When creating your summary, ensure you address ALL of the following:

1. **Brief Story of the Situation** – Provide context on the current environment, the proposed change, and the security angle.
2. **What is Being Requested** – Clearly state the request from the project team.
3. **Reasoning for the Request** – Explain why this change or technology is being proposed.
4. **Reasoning Behind the Approval** – Outline why this request would be approved from a security and business perspective.
5. **Important Considerations / Risks** – List any key risks, compliance concerns, operational dependencies, or architectural impacts.

Additional Requirements:
- If an architecture diagram is provided, explain the flow of data, key security controls, and trust boundaries.
- Highlight where the proposed solution interacts with sensitive data or secrets, and how Vault Radar mitigates associated risks.
- For each major component in the diagram, note its security relevance and possible threat scenarios.
- Maintain a professional, structured, and ticket-comment-ready tone.
- Avoid overly generic statements — base your assessment on the actual provided architecture and proposal.

Example closing statement:
"Based on the security review, this solution aligns with our security objectives for secrets management, improves detection and rotation processes, and introduces automated blast radius analysis. Recommended for approval with the noted considerations."

""")

stride_reporter = Agent(
        name="stride reporter",
        system_prompt="""
You are a Senior Cloud Security Documentation Specialist. Your job is to convert the analyzer’s
security review + the project proposal into a ticket-ready approval comment that is clear,
actionable, and suitable for both security and delivery teams.

Produce a concise, professional summary in the exact structure below. Keep it human-readable and
grounded in the provided analysis/proposal (no generic claims). If evidence is missing, call it out. """)

# Create a swarm with these agents
swarm = Swarm(
    [security_reviewer, stride_reporter])

#Create content blocks with text and image
content_blocks = [
    ContentBlock(text="Perform a full cloud security review of the attached architecture diagram and proposal. "
        "Explain the current situation, what is being requested, the reasoning for the request, "
        "the reasoning behind an approval from a security/business perspective, and any important "
        "considerations or risks. Describe trust boundaries, data flows, sensitive data handling, "
        "and control points relevant to the proposal. Keep it clear and human-readable."),
    ContentBlock(image={"format": "png", "source": {"bytes": image_bytes}})
]

# Execute the swarm with multi model input
result = swarm(content_blocks)

# Display the threat modelling result
print(f"Security Review Status: {result.status}")
print(f"\nSTRIDE Security Review report:")
print("=" * 50)
print(result.results)
