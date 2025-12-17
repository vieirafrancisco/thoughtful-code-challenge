from enums import PackageType, Stack


def sort(width: float, height: float, length: float, mass: float) -> str:
    package_type = PackageType.NONE
    volume = width * height * length

    if width >= 150 or height >= 150 or length >= 150 or volume >= 1_000_000:
        package_type = PackageType.BULKY
    
    if mass >= 20:
        if package_type == PackageType.BULKY:
            package_type = PackageType.BOTH
        else:
            package_type = PackageType.HEAVY

    if package_type == PackageType.BULKY or package_type == PackageType.HEAVY:
        return Stack.SPECIAL.value

    if package_type == PackageType.BOTH:
        return Stack.REJECTED.value
    
    return Stack.STANDARD.value

if __name__ == "__main__":
    print(sort(10, 150, 10, 21))
