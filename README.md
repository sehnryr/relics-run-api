# Relics.run API

This is an unofficial API for the [Relics.run](https://relics.run/) website.

The API is currently in development and is subject to change.
Through the API, you can access the same data that is available on the website.
This API only facilitates the retrieval of data through functions.

## Usage

To get the index, you can use the following code:
```python
import relics_run_api as r_api

# Get the index of relics.run
index = r_api.get_index()

# Get the list of unvaulted relics (for example)
unvaulted = index["non_vaulted"]

print(unvaulted) # ['Axi G10', 'Lith S15', 'Neo S17', ...]
```

Relics.run has a few endpoints that can be accessed through this API.

`https://relics.run/index/`
- `get_index()` - Get the index
- `get_index_price_data()` - Get the price data of the index
- `get_index_sub_type_data()` - Get the sub type data of the index

`https://relics.run/export/`
- :warning: Currently not implemented (and not planned)

`https://relics.run/history/`
- `get_history_dates()` - Get the available dates for the history
- `get_history(date: date)` - Get the history for a specific date

`https://relics.run/market_data/`
- `get_market_data_item_ids()` - Get the available item ids for the market data
- `get_market_data_item_info()` - Get the list of item info for which there is data
- `get_market_data_items()` - Get the market data for all items

`https://relics.run/output/`
- `get_output_type_dict()` - Get the list of types from relics.run
- `get_output_wfm_items_categorized()` - Get a list of items from the warframe market, categorized by type

Additionally, there are some utility functions and constants available:
- `RELIC_RARITY` - A dictionary containing the drop chances for each rarity of a relic

## Credits

- [Relics.run](https://relics.run/) for providing the data
- TheLostGuthix for the help with the API
