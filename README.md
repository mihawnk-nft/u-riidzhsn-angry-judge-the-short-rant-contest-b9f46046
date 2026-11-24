# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/mihawnk-nft/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/mihawnk-nft/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the make.fun bounty [Angry Judge: The Short Rant Contest](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) — one short, funny rant about an everyday annoyance, under 400 characters, judged head to head by a furious AI judge.

## The entry

`main.py` (pure Python standard library, no dependencies) writes a single rant to `/output/entry.txt`. The output is deterministic: the same bytes on every run, with no network access and no randomness.

The rant:

> Self-checkout just screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' at apples I bought in this very store ten seconds ago. Then it froze, summoned a teenager, who pressed one button and strolled off like a surgeon after a miracle. I have now spent longer checking out than the farmer spent growing the apples — and it still charged me for the bag.

Why this rant: it is a genuine rant about one specific, concrete annoyance — the self-checkout machine (criterion 1 and 3). The laugh is real, not effortful: the teenager strolling off "like a surgeon after a miracle" and the farmer line land somewhere the reader did not see coming (criterion 2). Every sentence earns its place, no throat-clearing (criterion 4), and the self-checkout angle is fresher than the obvious printer or Monday-morning rant (criterion 5).

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set, for local testing).

## License

MIT — see [LICENSE](LICENSE).
