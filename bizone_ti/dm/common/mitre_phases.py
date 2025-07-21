import enum


class MitrePhases(enum.Enum):
    discovery = "discovery"
    resource_development = "resource development"
    persistence = "persistence"
    privilege_escalation = "privilege escalation"
    lateral_movement = "lateral movement"
    execution = "execution"
    defense_evasion = "defense evasion"
    collection = "collection"
    command_and_control = "command and control"
    impact = "impact"
    credential_access = "credential access"
    initial_access = "initial access"
    exfiltration = "exfiltration"
    reconnaissance = "reconnaissance"
