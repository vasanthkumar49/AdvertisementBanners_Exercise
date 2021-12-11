# AdvertisementBanners - Coding Exercise - @author - Vasanthakumar Chidanandagari

## Business Model

Advertisement banners are displayed to users in a mobile application (`app_id`)
in a country (`country code`) from an advertiser (`advertiser_id`). When this
happens, an `impression` event is recorded and stored. Optionally, if the user
clicks on the banner, a `click` event is recorded.

## Implemented solutions

### Reading events stored in JSON files - clicks.json, impressions.json input file 

### Calculate metrics for some dimensions Output to a JSON file using the following format:

```json
[
  {
    "app_id": 1,
    "country_code": "US",
    "impressions": 102,
    "clicks": 12,
    "revenue": 10.2
  },
  ...
]
```

### Making a recommendation for the top 5 advertiser_ids to display for each app and country combination.

Output fields:

- `app_id`
- `country_code`
- `recomended_advertiser_ids` (list of top 5 advertiser ids with the highest revenue per impression rate in this application and country).

Output JSON file using the following format:

```json
[
  {
    "app_id": 1,
    "country_code": "US",
    "recommended_advertiser_ids": [32, 12, 45, 4, 1]
  }
]
```
### Writing the output to a JSON file using the given format - (Sample files - metrics.json, top5_advertiser.json)

## Deployment & Execution steps

- Deploy provided following files into speific path in a server or system
	AdvertisementBanners.py -> Application to process input data
	clicks.json             -> Input file
	impressions.json        -> Input file
	
- Provide input files path and output files path in the respective lines

- Run command in the cmd or console to run the application
  
  python AdvertisementBanners.py
  
- Check and validate generated output files 

	
