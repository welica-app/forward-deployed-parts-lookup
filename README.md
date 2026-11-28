# Repair a parts lookup

This is a small shop app that shows how many of each part the shop can sell, and it shows the wrong number for some parts. Your job is to find the fault, repair it, and add a check. The check must fail on the app as you downloaded it, and pass once your repair is in. Then it will catch the fault if it ever comes back.

## The rule

Each stock record holds the part's name and two counts. `on_hand` is how many are on the shelf. `reserved` is how many of those are already set aside for orders. The number available to sell is `on_hand` minus `reserved`. The counts are correct and are whole numbers. A result of zero means the shop has none to sell. For a part code the shop does not stock, the app shows `Part not found.`

The fault was reported like this: the app showed 18 hex bolts (`BOLT-08`) available, but 6 were already set aside, so only 12 could be sold.

## The files

- `shop_app.py`: the shop app you run in the terminal. Its function `lookup_part(part_code)` asks for a part's stock record. It gives back the part's name and the number available, or `None` for an unknown part. The app then shows the result.
- `stock_client.py`: sends the request to the stock service, through `fetch_stock(part_code)`.
- `stock_api.py`: a small stock service that runs on your own computer, at `127.0.0.1:8765`. The app asks it for one part with the request `GET /stock?part=PART_CODE`. The service sends back that part's record: its name and its two counts. The record is written in JSON, a common format that programs use to send data to each other. For a part the shop does not stock, the service sends back the code 404, which means "not found", and the message `{"error": "part_not_found"}`.
- `stock_replies.json`: the three invented stock records the service sends back.
- `checks.py`: simple checks that test the lookup. They are run from the function `run_checks()`. Each check looks up one part, then uses `assert` to state what the result must be. Python checks the statement in an `assert` line, and continues when the statement is true. When its statement is false, it stops with an error, so the check fails. The existing checks test a part with nothing set aside, and an unknown part. Add your own check in `run_checks()`, written the same way.

## How to start

You need Python 3. Nothing else needs installing.

1. Download these files and unzip the folder, or clone the repository if you use Git.
2. Open a terminal in the folder that holds `stock_api.py`. Start the stock service and leave it running:

   ```sh
   python3 -B stock_api.py
   ```

   It prints `Stock API: http://127.0.0.1:8765`.
3. Open a second terminal in the same folder. Look up each part:

   ```sh
   python3 -B shop_app.py BOLT-08
   python3 -B shop_app.py CLIP-12
   python3 -B shop_app.py CAP-04
   python3 -B shop_app.py UNKNOWN
   ```

4. Run the checks:

   ```sh
   python3 -B checks.py
   ```

   On the starter as it is, this prints `Checks passed.`
5. To see a record the service sends, open `http://127.0.0.1:8765/stock?part=BOLT-08` in a web browser while the service is running. To print all the saved records, even with the service stopped, run:

   ```sh
   python3 -B -m json.tool stock_replies.json
   ```

6. When you have finished, press Ctrl+C in the first terminal to stop the service.

If the app prints `Stock API unavailable.`, the app could not get usable stock data from the stock service. First check that the service is still running in the first terminal. If it is not, start it again, as in step 2.

## What to hand in

The code you changed, `checks.py` with your new checks, and a short note: what was wrong, how you found it, what you changed, and how you checked it. End the note with two plain lines for the counter staff: what the number on the screen now means, and what to do if the app shows `Stock API unavailable.`
