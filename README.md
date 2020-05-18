# %CUSTOM_PLUGIN_SERVICE_NAME%

[![pipeline status][pipeline]][git-link]
[![coverage report][coverage]][git-link]

## Summary

Welcome to Python Hello World based on [https://www.tornadoweb.org]()

## Build

```bash
pip install --no-cache-dir -r requirements.txt
```

## Test

```bash
curl localhost:3000/fib/40
curl localhost:3000/cruds/cars/
curl localhost:3000/cruds/cars/ -d '{ "model": "Panda", "color": "REd" }' -H'content-type: application/json'
curl localhost:3000/log/dfs
curl localhost:3000/logs/dfs -H'miauser: aaa"
curl localhost:3000/logs/dfs -H'miauser: aaa' -H'miagroups: www'
```

-------------------------------------------

[pipeline]: https://git.tools.mia-platform.eu/hackathons/custom-plugin-challenge/giulio-p/badges/master/pipeline.svg
[coverage]: https://git.tools.mia-platform.eu/hackathons/custom-plugin-challenge/giulio-p/badges/master/coverage.svg
[git-link]: https://git.tools.mia-platform.eu/hackathons/custom-plugin-challenge/giulio-p/commits/master
[merge-request]: https://git.tools.mia-platform.eu/hackathons/custom-plugin-challenge/giulio-p/merge_requests
