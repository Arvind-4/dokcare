release: bash commands/release-tasks.sh

web: gunicorn app:app --workers 10 --worker-class uvicorn.workers.UvicornWorker