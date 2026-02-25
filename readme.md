# Ignition Event Streams Example Stack

This repository contains a containerized development environment featuring examples of the Event Streams module.

TLDR:
1. git clone <your-repo-url>
2. docker compose up -d

All database tables, kafka topics, etc. should prepopulate upon startup.

## 🔗 Connection Details

| Service | Access URL / Port | Credentials (Default) |
| :--- | :--- | :--- |
| **Ignition** | `http://localhost:8088` | admin / password |
| **pgAdmin** | `http://localhost:5050` | pgadmin4@pgadmin.org / admin |
| **Kafka UI** | `http://localhost:8080` | N/A |
| **Postgres** | `localhost:5432` | admin / password (DB: postgres) |
| **Kafka Broker** | `kafka:9092` | Internal Docker Network |

## 🏗 Architecture Overview

* **Ignition**: Industrial automation platform.
* **PostgreSQL**: Database to store event logs and tag data.
* **Kafka**: Distributed message broker for high-throughput event streaming. Used for a few handlers and sources in Event Streams
* **Kafka UI**: Web interface for managing topics and messages (**Port 8080**).
* **pgAdmin**: Web interface for database management (**Port 5050**).

## 🚀 Getting Started

### Prerequisites
* Docker and Docker Compose installed.
* The `.env` file (copied from `.env.example`).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd event-streams-examples
    ```

2.  **Configure Environment Variables:**
    ```bash
    cp .env.example .env
    # Edit .env to set passwords or license keys
    ```

3.  **Spin up the stack:**
    ```bash
    docker-compose up -d
    ```

## 📂 Project Structure & Git Strategy

This repo uses a targeted `.gitignore` to ensure only configuration and source code are tracked.

| Directory/File | Description |
| :--- | :--- |
| `ignition/projects` | **Tracked**: Ignition Views, Scripts, and Resources. |
| `ignition/config` | **Tracked**: Gateway config (excluding local runtime DBs). |
| `postgres-init/` | **Tracked**: SQL scripts to initialize the DB schema. |
| `**/logs/`, `**/db/` | **Ignored**: Runtime data and binary logs. |
| `.env` | **Ignored**: Local secrets and license keys. |

## 📊 Database Schema

The Postgres container automatically runs `/postgres-init/init.sql` on the first startup to create:
* `ex_event_streams_example_data`: Process and inventory logs.
* `ex_event_streams_tag_data`: Tag path, quality, and value history.

## 🛠 Maintenance

**Check logs for the event stream:**
```bash
docker logs -f ignition