# References

Two files drive this skill:

## `profile.md` (required after first run)

The user's static configuration: sources, categories, industry, role, format preferences. Created during first-run setup. See `profile-template.md` for the structure.

## `exclusions.md` (optional)

Topics or keywords to always filter out. Created when the user repeatedly flags noise. Format: one keyword or topic per line.

Example:

```
celebrity news
crypto rugpulls
opinion columns
sports
```

The skill reads this file on every run and drops any story whose title or summary contains a listed keyword.
