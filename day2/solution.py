from dataclasses import dataclass
import re


@dataclass
class GameConfiguration:
    num_red: int
    num_green: int
    num_blue: int


def is_possible_compare_configs(
    first_config: GameConfiguration, other_config: GameConfiguration
) -> bool:
    return (
        first_config.num_red >= other_config.num_red
        and first_config.num_green >= other_config.num_green
        and first_config.num_blue >= other_config.num_blue
    )


def power_of_cubes(config: GameConfiguration) -> int:
    return config.num_red * config.num_blue * config.num_green


def sample_to_config(config_line: str) -> GameConfiguration:
    final_config = GameConfiguration(num_red=0, num_green=0, num_blue=0)
    numbers = config_line.split(",")
    for num_str in numbers:
        number = re.findall(r"\d+", num_str)[0]
        if "red" in num_str:
            final_config.num_red = int(number)
        elif "blue" in num_str:
            final_config.num_blue = int(number)
        elif "green" in num_str:
            final_config.num_green = int(number)
    return final_config


def is_possible(config: GameConfiguration, line: str) -> bool:
    samples = line.split(";")
    for s in samples:
        sample = sample_to_config(s)
        if not is_possible_compare_configs(config, sample):
            return False
    return True


def fewest_number_of_cubes(line: str) -> GameConfiguration:
    final_config = GameConfiguration(num_red=0, num_green=0, num_blue=0)
    samples = line.split(";")
    for s in samples:
        sample = sample_to_config(s)
        final_config.num_red = max(final_config.num_red, sample.num_red)
        final_config.num_blue = max(final_config.num_blue, sample.num_blue)
        final_config.num_green = max(final_config.num_green, sample.num_green)
    return final_config


def main():
    file_input = open("input.txt", "r")
    total_sum = 0
    power_sum = 0
    config = GameConfiguration(num_red=12, num_green=13, num_blue=14)
    for line in file_input:
        parse_line = line.split(":")
        game_id = int(parse_line[0][len("Game ") :])
        if is_possible(config, parse_line[1]):
            total_sum += game_id
        power_sum += power_of_cubes(fewest_number_of_cubes(parse_line[1]))
    print(f"Sum of possible games: {total_sum}")
    print(f"Power of cubes sum: {power_sum}")


if __name__ == "__main__":
    main()
