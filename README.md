# charged

Obsidian vault and [Jekyll] campaign site published at <https://terra-campaigns.github.io/charged> using the [Just the Docs] theme and the [oude-mechanismen] engine.

## Setup

Run the idempotent environment setup script from the repository root:

```sh
./bin/setup
```

This configures `.githooks/`, ensures Ruby dependencies are installed (`bundle check || bundle install`), compiles the site and local Tier 1 catalogue cache (`.agents/context/catalog.json`), and runs `oude doctor`.

## Local Preview & Checks

```sh
bundle exec jekyll serve --trace
oude doctor
oude lint-wiki
```

Link, gallery, and last-modified metadata is extracted in-memory during build by the `oude-mechanismen` RubyGem (`data_extractor.rb`). Live caravan trade prices in `_data/trade.json` are synchronised separately by `.agents/scripts/sync_trade.py`.

## Licensing & Attribution

Licensed under the [MIT License]. Deployment workflows derive from GitHub's [starter workflows].

[Jekyll]: https://jekyllrb.com
[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[oude-mechanismen]: https://github.com/terra-campaigns/oude-mechanismen
[MIT License]: https://en.wikipedia.org/wiki/MIT_License
[starter workflows]: https://github.com/actions/starter-workflows/blob/main/pages/jekyll.yml
