# Docker & Podman User Guide

This guide explains how to build and run the `mysite` project using Docker or Podman.
The project uses `uv` for dependency management and runs Django on port 8000.

## Prerequisites

- **Docker:** Docker Desktop installed and running.
- **Podman:** Podman installed (`brew install podman`).
  - _Note for macOS:_ Ensure `krunkit` is installed if you encounter virtualization errors (`brew tap slp/krunkit && brew install krunkit`).

---

## 🐳 Using Docker (Recommended)

We use `docker-compose` for the easiest experience.

### 1. Build and Start

Run the application in the background:

```bash
docker compose up -d --build
```

This command will:

- Build the image using `Dockerfile`.
- Start the `web` container.
- Mount your current directory to `/app` (live reloading).
- Mount a volume for `.venv` to prevent conflicts.

### 2. Check Status

View logs to ensure the server is running:

```bash
docker compose logs -f
```

### 3. Stop

Stop the containers:

```bash
docker compose down
```

### Access the App

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## 🦭 Using Podman

If you prefer Podman or cannot use Docker, follow these steps.
_Note: Since `podman-compose` is not set up, we use native Podman commands._

### 1. Initialize Machine (First Time Only)

Ensure your Podman VM is running:

```bash
podman machine init
podman machine start
```

### 2. Build the Image

Build the container image manually:

```bash
podman build -t mysite-web .
```

### 3. Run the Container

Run the container with necessary volume mounts:

```bash
podman run -d \
  -p 8000:8000 \
  -v $(pwd):/app \
  -v /app/.venv \
  mysite-web
```

### 4. Manage Container

**Check Logs:**

```bash
podman logs -l
```

**Stop Container:**

```bash
podman stop -a
```

---

## 🛠 Troubleshooting

### "krunkit: executable file not found" (macOS)

If `podman machine start` fails with this error, install the missing dependency:

```bash
brew tap slp/krunkit
brew install krunkit
```

Then try starting the machine again.

### Port Already in Use

If port 8000 is blocked, ensure no other service (like a local Django run or another container) is using it.

```bash
lsof -i :8000
kill -9 <PID>
```
