from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

# Dataclass object representing initial pattern
@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    # Additional constructor to return Pattern object from specified pattern in TOML file
    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells = {tuple(cell) for cell in toml_data["alive_cells"]},
        )

# Return representation of single pattern by name
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf=8"))
    return Pattern.from_toml(name, toml_data=data[name])

# Return list of all pattern representations
def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]