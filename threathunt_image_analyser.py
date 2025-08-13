from strands import Agent
from strands.multiagent import Swarm
from strands.types.content import ContentBlock

#Load Image Data
with open ("arch.png", "rb") as f:
    image_bytes = f.read()

#Create agents for threat modelling workflow

threat_analyzer = Agent(
        name="threat_analyzer",
        system_prompt="You are a Cybersecuirty expert specializing in  threat modelling. Analyze system architecture diagrams to identify potential security threats using the STRIDE framework(Spoofing, Tampering, Repudiation, Informaton Disclosure, Denial of servive, Elevaton of Privilege). Focus on data flows, trust boundaries and system components")

stride_reporter = Agent(
        name="stride reporter",
        system_prompt="You are security documentation specialist. Create a brief threat modelling reports organized by STRIDE categories. For each threat category, provide specific vulnerabilities, attack vectors, impact assesment and mitigation recommendatons. Structire the report professionally with clear setion for each STRIDE component")

# Create a swarm with these agents
swarm = Swarm(
    [threat_analyzer, stride_reporter])

#Create content blocks with text and image
content_blocks = [
    ContentBlock(text="perform a comprehensive threat modelling analysis of this system architecture diagrams to identify potential security threats using the STRIDE framework. Identify security vulnerabilities, attack vectors and provide detailed mitigation strategy"),
    ContentBlock(image={"format": "png", "source": {"bytes": image_bytes}})
]

# Execute the swarm with multi model input
result = swarm(content_blocks)

# Display the threat modelling result
print(f"Threat analysis Status: {result.status}")
print(f"\nSTRIDE threat Modelling report:")
print("=" * 50)
print(result.results)
