# DALC - Fine-tuned Language Models

We make available two fine-tuned langauge models using DALC v2.0: one for offensive language and one for abusive language.

The models are available via HugginFace:

- Offensive language model: https://huggingface.co/GroNLP/bert_dutch_base_offensive_language
- Abusive langauge model: https://huggingface.co/GroNLP/bert_dutch_base_abusive_language

Both models have been obatined using the full training data per language phenomenon from DALC v2.0. The following hyperparameters have been used:

| Hyperparamters      | Value |
| ------------------- | ------|
| Learning rate       | 2e-5  |
| Training Epochs     | 5     |
| Optimzer            | AdamW |
| Max sequence length | 280   |
| Adam epsilon        | 1e-8  |
| Batch size          | 16    |
| Warmup steps        | 2     |


Citation (if available):

```
@inproceedings{caselli-derveen-2023,
    title = "Benchmarking Offensive and Abusive Language in Dutch Tweets",
    author = "Caselli, Tommaso and van der Veen, Hylke",
    booktitle = "Proceedings of the 7th Workshop on Online Abuse and Harms (WOAH)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "",
    doi = "",
    pages = "",
}
```








