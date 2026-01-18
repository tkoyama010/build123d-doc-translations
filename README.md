# build123d official documentation translations

[![build123d](https://img.shields.io/badge/%F0%9F%94%A7-build123d-white)](https://build123d.readthedocs.io)
![All Contributors](https://img.shields.io/github/all-contributors/tkoyama010/build123d-doc-translations?color=ee8449)

[build123d official documentation translations](https://github.com/tkoyama010/build123d-doc-translations) is a project to provide build123d official documentation, hosted on
the Read The Docs platform, in multiple languages.

> [!NOTE]
> The current procedure is a bit tricky because Read The Docs
> doesn't have a way to specify options for `sphinx-build` command.
> We use the `post_create_environment` job to copy the `locales` directory
> to `build123d/docs` and Sphinx will automatically find the translations.
> If there is a better way, open an issue.

## How the translated documentation projects are setup on RTD

Instructions:
https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

- There is a RTD project for each language.
- Each project needs the correct **Language** setting on the
  **Settings** page.
- The parent project needs connections created to each translated
  project on the **Translations Settings** page.

| Language                 | Build Status                                                                                                                                                | RTD Project                                                                                                                   | Transifex                                                                                                                              |
| :----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| English (parent project) | [![Documentation Status](https://readthedocs.org/projects/build123d/badge/?version=latest)](https://build123d.readthedocs.io/en/latest/?badge=latest)       | [![readthedocs.org](https://img.shields.io/badge/readthedocs-en-ff7964.svg?)](https://readthedocs.org/projects/build123d/)    |                                                                                                                                        |
| 日本語                   | [![Documentation Status](https://readthedocs.org/projects/build123d-ja/badge/?version=latest)](https://build123d-ja.readthedocs.io/ja/latest/?badge=latest) | [![readthedocs.org](https://img.shields.io/badge/readthedocs-ja-ff7964.svg?)](https://readthedocs.org/projects/build123d-ja/) | [![Transifex](https://img.shields.io/badge/Transifex-ja-blue.svg?)](https://app.transifex.com/tkoyama010/build123d-doc/translate/#/ja) |

## How to add a new language translation

1.  Add new language to `locales/update.sh`:

```diff
-   rm -R -f ja
-   tx pull --silent -f -l ja
+   rm -R -f ja pt_BR
+   tx pull --silent -f -l ja,pt_BR
```

2.  Update po files:

```
sh ./locales/update.sh
```

3.  Commit them

4.  Add new project on Read The Docs. For example, for `pt_BR`:

    https://readthedocs.org/projects/build123d-pt-br/

> [!NOTE]
> If a RTD project name for a translation is already taken,
> create a unique project name instead. For example, when `build123d-ru`
> was taken, `build123d-doc-ru` was used instead.

5.  Add new translation project to parent project:

    https://readthedocs.org/dashboard/build123d/translations/

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkoyama010"><img src="https://avatars.githubusercontent.com/u/7513610?v=4?s=100" width="100px;" alt="Tetsuo Koyama"/><br /><sub><b>Tetsuo Koyama</b></sub></a><br /><a href="#ideas-tkoyama010" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-tkoyama010" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
