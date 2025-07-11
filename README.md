# Senzing ChatGPT Plugin Demo

## :no_entry: Deprecated

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

A demo of Senzing Conversational AI for Entity Resolution announced in this [blog post]!

https://github.com/senzing-garage/senzing-with-chatgpt-plugin/assets/23748/af382f96-8657-4640-ac44-0fdcaacabe12

## Features

- Show examples of entities with either matches, possible matches, or relationships.
- Show details about an entity.
- Show step-by-step details of how an entity was resolved.
- Search for entities by entity attributes.

## Prerequisite

- [ChatGPT Plugins Developer Early Access]

## Quickstart

1. Open the project in a VS Code [DevContainer].
2. In the remote container terminal, start the server: `make run`
3. In ChatGPT, select `GPT-4` > `Plugins (Beta)`
4. Go to the `Plugin store`
5. Select `Develop your own plugin` (on the bottom bar)
6. Enter your website domain: `localhost:8080`

## Data

The included SQLite db is already preloaded with the [truth-sets data].

If you want to use your own data, you can either:

- Follow the [Quickstart for Docker] guide.
- Modify `SENZING_ENGINE_CONFIGURATION_JSON` in [devcontainer.env].

[blog post]: https://senzing.com/first-conversational-ai-for-entity-resolution/
[ChatGPT Plugins Developer Early Access]: https://openai.com/waitlist/plugins
[devcontainer.env]: https://github.com/kakugawa/senzing-entity-resolution-plugin/blob/main/.devcontainer/devcontainer.env
[DevContainer]: https://code.visualstudio.com/docs/devcontainers/tutorial
[Quickstart for Docker]: https://senzing.zendesk.com/hc/en-us/articles/12938524464403-Quickstart-For-Docker
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
[truth-sets data]: https://github.com/senzing-garage/truth-sets
