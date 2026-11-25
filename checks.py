from shop_app import lookup_part


def run_checks():
    part = lookup_part("CLIP-12")
    assert part["name"] == "Pipe clip"
    assert part["available"] == 9
    assert lookup_part("UNKNOWN") is None


if __name__ == "__main__":
    run_checks()
    print("Checks passed.")
