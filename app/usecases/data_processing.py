from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
    agent_data (AgentData): Agent data that contains accelerometer, GPS, and timestamp.
    Returns:
    processed_data (ProcessedAgentData): Processed data containing the classified state of
    the road surface and agent data.
    """
    road_state = "good"
    if agent_data.accelerometer.y > 100:
        road_state = "has hills"
    elif agent_data.accelerometer.y < 0:
        road_state = "has pits"

    return ProcessedAgentData(road_state=road_state,
                              agent_data=agent_data)
        