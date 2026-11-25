import sys

from stock_client import fetch_stock


def lookup_part(part_code):
    stock = fetch_stock(part_code)
    if stock is None:
        return None

    available = stock["on_hand"]
    return {"name": stock["name"], "available": available}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 shop_app.py PART_CODE", file=sys.stderr)
        return 2

    part_code = sys.argv[1]
    try:
        part = lookup_part(part_code)
    except OSError:
        print("Stock API unavailable.", file=sys.stderr)
        return 1

    if part is None:
        print("Part not found.")
        return 0

    print(f'{part["name"]} ({part_code}) | Available: {part["available"]}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
