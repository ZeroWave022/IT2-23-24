class Pokemon:
    def __init__(self, raw_data) -> None:
        self.id: int = raw_data["id"]
        self.names: dict[str, str]  = raw_data["name"]
        self.types: list[str] = raw_data["type"]
        self.stats: dict[str, str] = raw_data["base"]

    def __str__(self) -> str:
        return f"""{self.names['english']}:
HP: {self.stats['HP']}
Attack: {self.stats['Attack']}
Defense: {self.stats['Defense']}
Special Attack: {self.stats['Sp. Attack']}
Special Defense: {self.stats['Sp. Defense']}
Speed: {self.stats['Speed']}"""
