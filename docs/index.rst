======================
Cortosis Documentation
======================

Release v\ |version|

This project is sponsored by **Interstellio IO (PTY) LTD**.

**Planning Phase:** Under construction, first initial code/commit/placeholder.

This project is not ready to be used by any external projects.

**Follow this project to see when we push a functional minimal viable version.**

Overview
--------

Cortosis is a modern, high-performance Python framework for API, web, and background daemons (minions) development. It provides a consistent development pattern across these domains, ensuring a streamlined and scalable architecture.

Built on top of some of the best open-source projects, Cortosis is optimised for speed, flexibility, and reliability. It leverages:

* **Falcon Router** -- A blazing-fast request router known for its efficiency in API handling from the Falcon Web Framework.
* **Uvicorn** -- A lightweight and high-performance ASGI server powered by asyncio for handling concurrent requests efficiently.
* **Asyncio** & Modern Python -- Ensuring non-blocking, high-throughput performance.
* **Jinja2** -- A powerful and flexible templating engine, making it easy to render dynamic web content.

Cortosis is inspired by our internal technology stack at Interstellio IO, which powers some of our NebularStack frontends and backends. After years of refinement and learning from real-world deployments, Cortosis is being developed as an open-source framework, bringing these optimisations and architectural patterns to the broader developer community.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   contrib
   contact