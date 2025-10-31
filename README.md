# Agora – AI Debate & Consensus Platform

> _"Turning conversation into structured understanding."_

Agora is an open-source, AI-powered debate and consensus analysis platform.  
Users can join **voice rooms** or **text discussions**, and the system automatically listens, transcribes, and organizes the conversation into a **consensus map** — revealing points of **agreement**, **divergence**, and **key quotes**.

Think of it as an intelligent moderator that helps groups **see how discussions evolve** — useful for classrooms, teams, and online communities.

---

## Features

- **Real-Time Debate Rooms** – Join LiveKit-powered audio or video rooms.  
- **AI Argument Mining** – Automatically detects claims, counterpoints, and sentiment.  
- **Consensus Visualization** – Interactive map showing agreement and divergence clusters.  
- **Speech-to-Text & Summarization** – Transcribes and summarizes discussions.  
- **Supabase Auth** – Secure login and participant management.  
- **Structured Storage (Postgres)** – Stores transcripts, argument graphs, and summaries.  
- **Containerized Deployment** – Fully Dockerized microservices with optional AWS integration.  

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Backend API** | [FastAPI](https://fastapi.tiangolo.com/) | Session management, REST & WebSocket endpoints |
| **ML / AI Layer** | [Pydantic-AI](https://docs.pydantic.dev/latest/concepts/ai/) / Custom models | Argument mining, sentiment mapping |
| **Frontend / Dashboard** | [Django](https://www.djangoproject.com/) | Visualization dashboard & admin panel |
| **Auth & Realtime Data** | [Supabase](https://supabase.com/) | Authentication, event streaming, and storage |
| **Database** | [PostgreSQL](https://www.postgresql.org/) + [Alembic](https://alembic.sqlalchemy.org/) | Structured storage with schema migrations |
| **Media & Realtime** | [LiveKit](https://livekit.io/) | Voice/video debate rooms |
| **Deployment** | [Docker](https://www.docker.com/), AWS ECS/ECR | Scalable microservice deployment |

---

## Architecture Overview

```
                    ┌────────────────────┐
                    │     LiveKit        │
                    │ (Voice/Video Room) │
                    └────────┬───────────┘
                             │ Audio Stream
                             ▼
┌──────────────┐       ┌──────────────────────┐       ┌──────────────────────┐
│   Supabase   │◄─────►│      FastAPI API     │◄─────►│   Pydantic-AI Layer  │
│ Auth + Logs  │       │  Debate Management   │       │ Argument & Sentiment  │
└──────────────┘       └──────────────────────┘       └──────────────────────┘
       │                        │                              │
       ▼                        ▼                              ▼
┌────────────────┐       ┌────────────────────┐        ┌────────────────────┐
│  PostgreSQL DB │◄────►│     Django UI       │◄──────►│  Consensus Mapping │
└────────────────┘       └────────────────────┘        └────────────────────┘
```

---

## Setup & Installation

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Supabase Project (with API keys)
- Postgres instance (local or cloud)
- LiveKit API credentials

### Clone Repository
```bash
git clone https://github.com/yourusername/agora-ai.git
cd agora-ai
```

### Environment Variables

Create a `.env` file in the root directory:

```bash
SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_key>
DATABASE_URL=postgresql://user:password@localhost:5432/agora
LIVEKIT_API_KEY=<your_livekit_key>
LIVEKIT_SECRET=<your_livekit_secret>
OPENAI_API_KEY=<optional_for_Pydantic_AI>
```

### Run with Docker

```bash
docker compose up --build
```

Services exposed:

* **FastAPI API** → `http://localhost:8000`
* **Django Dashboard** → `http://localhost:8080`
* **Supabase Sync** → Background task manager
* **Postgres** → `localhost:5432`

---

## Roadmap

| Milestone | Description                                                | Status        |
| --------- | ---------------------------------------------------------- | ------------- |
| **MVP**   | Voice rooms + AI argument extraction + consensus dashboard | In progress   |
| **v1.0**  | Real-time sentiment graphs + Supabase sync + auth          | Planned       |
| **v1.1**  | Multi-language support (speech-to-text + translation)      | Planned       |
| **v2.0**  | Federated debate summaries + exportable data APIs          | Planned       |
| **v2.5**  | AI Debate Coach (feedback on speaking style)               | Idea stage    |

---

## Research References

* Argument Mining – *Peldszus & Stede (2013), "From Argument Diagrams to Argumentation Mining"*
* Consensus Detection – *Rosenthal & McKeown (2015), "Detecting Agreement and Disagreement in Conversations"*
* Real-time Transcription – *Whisper by OpenAI*
* Visualization – *D3.js-based debate clustering models*

---

## Contributing

Contributions are welcome!
To get started:

1. Fork the repository
2. Create a new branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit and push your changes
4. Open a Pull Request describing what you added

Please follow the [Contributor Code of Conduct](./CODE_OF_CONDUCT.md).

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## Community & Support

* Discussions: [GitHub Discussions](https://github.com/yourusername/agora-ai/discussions)
* Issues: [GitHub Issues](https://github.com/yourusername/agora-ai/issues)
* Contact: `maintainers@agora.ai`

---

