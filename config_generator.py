import json

items = {
    '6800xt': {'min': 600, 'max': 900, 'asins': ["B08MVC76SR","B08N6ZLX9B","B08NS4W2ZY","B08NWHKGS9","B08NS4W2ZY","B08NXXT7WN","B08NXVNMPQ","B08NXYNLMR","B08NX14LV1"]},
    'ps5': {'min': 400, 'max': 500, 'asins': ["B08FC5L3RG","B08FC6MR62"]},
    '3070': {'min': 400, 'max': 600, 'asins': ["B08L8LG4M3","B08L8HPKR6","B08L8JNTXQ","B08L8KC1J7","B08L8L71SM","B08L8L9TCZ","B08LW46GH2","B08M13DXSZ","B08N8KXJCN","B08KY266MG","B08KXZV626","B08KY322TH","B08KWPDXJZ","B08KWLMZV4","B08KWN2LZG","B08HBJB7YD","B08HBF5L3K","B08LF32LJ6","B08LF1CWT2"]},
    '3080': {'min': 400, 'max': 900, 'asins': ["B08HH5WF97","B08HHDP9DW","B08J6F174Z","B08HR6FMF3","B08HR55YB5","B08HR4RJ3Q","B08HR3Y5GQ","B08HR3DPGW","B08HJS2JLJ","B08HJTH61J","B08KJ3VKLQ","B08HR7SV3M","B08HR5SXPS","B08HBTJMLJ","B08HBR7QBM","B08HJNKT3P","B08HVV2P4Z"]},
    '3090': {'min': 500, 'max': 900, 'asins': ["B08HJGNJ81","B08HJLLF7G","B08J6GMWCQ","B08HJRF2CN","B08HJPDJTY","B08KTYZXR9","B083GTG25Q","B08HRBW6VB","B08HR9D2JS","B08HBQWBHH","B08HBVX53D","B08HJQ182D"]},
}

websites = (
    'smile.amazon.de',
    'amazon.fr',
    'amazon.co.uk',
    'amazon.nl',
    'amazon.es',
    'amazon.it',
)

out = {
    "asin_groups": 1,
}
for item, values in items.items():
    current = out["asin_groups"]

    out[f"asin_list_{current}"] = values["asins"]
    out[f"reserve_min_{current}"] = values["min"]
    out[f"reserve_max_{current}"] = values["max"]

    out["asin_groups"] += 1

cmds = []
for website in websites:
    website_slug = website.replace('.', '_')
    cmds.append('AUTOBUY_CONFIG_PATH=config/g_' + website_slug + ' python3 app.py amazon --headless &')

    out['amazon_website'] = website
    with open('config/g_' + website_slug, 'w') as f:
        f.write(json.dumps(out, indent=2))

    with open('cmds', 'w') as f:
        f.write('\n'.join(cmds))
