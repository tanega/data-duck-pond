# The Duck Pond

![Birds of New York(1910).Art by Louis Agassiz Fuertes](/assets/images/ducks.jpg)

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

## Introduction

A experimental **poor man's datalake** made with [Dagster](https://github.com/dagster-io/dagster) for data orchestration, [DuckDB](https://github.com/duckdb/duckdb) as an high-performance analytical database system, [Metabase](https://github.com/metabase/metabase) for data vizualisation and [MinIO](https://github.com/minio/minio) for persistent data storage.

Everything is shipped as **Docker containers** with [Traefik](https://github.com/traefik/traefik) as a reverse-proxy.

## Prerequisites

- Having **Docker ( v20.10 or latest)** installed on your system
- Active ** Python environment** (ideally _Python 3.9.8_ for consistency) with Poetry installed (for more information, see [Dagster Container README](/dagster/README.md))
- Install NPM and Node to run launch scripts; See [these instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

## Getting started locally

### **Build and run** containers

```bash
    # Build images
    npm run d:build
    # Start containers with detach daemon
    npm run d:up-d
    # Alternatively keep them attached
    npm run d:up
    # When you're done with, shut down...
    npm run d:down
    # ...remove volumes if needed
    npm run d:down:all
```

Alternatively, you can run Docker scripts directly

```bash
    # make scripts/docker.sh executable
    chmod u+x ./scripts/docker.sh
    # list all running composed containers
    ./scripts/docker.sh ps
    # build images
    ./scripts/docker.sh build
    # launch containers
    ./scripts/docker.sh up -d
    # remove containers and network
    ./scripts/docker.sh down
    # ...and so on!
```

### Take a look at the running services

- Dagster UI, **Dagit** is accessible at [http://orchestration.localhost](http://orchestration.localhost)
- **Metabase** with _DuckDB_ driver is accessible at [http://vizualization.localhost](http://vizualization.localhost)
- **MinIO dashboard** is accessible at [http://storage.localhost](http://storage.localhost)

## Contributing

Contributions guidelines will be posted soon!

## Credits

- **Cover image** from _Eaton, Elon Howard. Birds of New York. pt. 1 (1910)._ Art by Louis Agassiz Fuertes. Contributed in BHL from Eaton, Elon Howard. **Birds of New York. pt. 1 (1910)**. Art by Louis Agassiz Fuertes. Contributed in BHL from Gerstein Science Information Centre [(https://s.si.edu/2LlwjIL)](https://s.si.edu/2LlwjIL)
- Special thanks to [MileTwo](https://github.com/MileTwo) for his Docker multi stage build template for Dagster.
- Every building blocks of this repo are Open Source projects. **s/o to every contributors involved !**
