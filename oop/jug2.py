class Container:

    name: str = ""
    volume: int = 0
    current_volume: int = 0
    pour_out: int = 0

    def pour_out_liquid(self) -> int:
        if self.current_volume - self.pour_out >= 0:
            self.current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.name} пуст")
            return 0

    def pour_liquid(self, volume: int) -> None:
        if self.current_volume + volume <= self.volume:
            self.current_volume += volume
        else:
            print(f"В {self.name} не хватит места")

    def info(self):
        print(f"{self.name} = {self.current_volume}")


class Jug(Container):
    name: str = "Jug"
    volume: int = 1000
    current_volume: int = 600
    pour_out: int = 100


class Glass(Container):
    name: str = "Glass"
    volume: int = 300
    current_volume: int = 0
    pour_out: int = 50


def main() -> None:
    jug = Jug()
    glass = Glass()
    i = 0
    while i < 15:
        jug.info()
        glass.info()
        glass.pour_liquid(jug.pour_out_liquid())
        i += 1


if __name__ == "__main__":
    main()
