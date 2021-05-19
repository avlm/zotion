WIP Python client for official Notion API (now in public beta)

```bash
$ pip install zotion
```

```python
>>> from zotion.client import Notion
>>> notion = Notion('YOUR_NOTION_API_KEY')
>>> database = notion.retrieve_database('YOUR_DATABASE_ID')
```

Database will be an [addict](https://github.com/mewwts/addict) object, so you can easily access info just doing this:

```python
>>> database.title[0].text.content
>>> 'My great database'
```

For now just internal integrations.

Feel free to contribute.

MIT license.
