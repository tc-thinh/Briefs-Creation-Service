# Briefs-Creation-Service
Multi-tenant service for Cronjob-Briefs creation.

**Stack**: AWS RDS PostgreSQL, OpenAI, Django

This project is a standalone Django service that generates daily briefs (tasks, events, and news) using OpenAI, stores them in an AWS RDS PostgreSQL database, and runs as a scheduled task within a Docker container.

## Prerequisites
Before running the project, ensure you have the following installed:

- Docker (with Docker Compose)
- Git (optional, for cloning the repository)
- An AWS account with an RDS PostgreSQL instance set up
- An OpenAI API key

## Project Setup
Follow these steps to get the project up and running:

1. Clone the Repository
If you’re using version control, clone the repository to your local machine:

```bash
git clone <repository-url>
cd brief_service
```

Replace `<repository-url>` with your actual repository URL. If you’re starting fresh, skip this step and ensure you’re in the project directory.

2. Configure Environment Variables
Create a `.env` file in the project root directory to store sensitive configuration details. Use the following template:

```
# AWS RDS PostgreSQL credentials
DB_HOST=<your_rds_endpoint>
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_PORT=5432

# OpenAI API key
OPENAI_API_KEY=<your_openai_api_key>
```

- Replace `<your_rds_endpoint>` with your RDS instance endpoint (e.g., brief-db.xxxx.us-east-1.rds.amazonaws.com).
- Replace `<your_db_name>`, `<your_db_user>`, and `<your_db_password>` with your RDS database name, username, and password, respectively.
- Replace `<your_openai_api_key>` with your OpenAI API key.

**Note**: Do not commit the .env file to version control. It’s already ignored in .gitignore.

3. Build and Run the Docker Containers
Use Docker Compose to build and start the service:

```bash
docker-compose up --build
```

- The `--build` flag ensures the Docker image is rebuilt if there are changes to the `Dockerfile` or dependencies.
- This command starts the Django development server inside a container, accessible at `http://localhost:8001`.

4. Apply Database Migrations
The first time you run the project, you need to set up the database schema. Open a new terminal window while the containers are running and execute:

```bash
docker-compose exec web python manage.py migrate
```

- This applies any pending migrations to your AWS RDS PostgreSQL database.

5. Create a Superuser (Optional)
If you plan to use the Django admin interface, create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

6. Stop the Service
When you’re done, stop and remove the containers:

```bash
docker-compose down
```

- This stops the running containers and cleans up the network, but preserves your RDS database data.

## Additional Commands
- Check Container Logs: View logs for debugging:
```bash
docker-compose logs web
```

- Run Without Detaching: If you want to see logs in real-time and stop with Ctrl+C:
```bash
docker-compose up --build
```

- Rebuild Without Running: To update the image without starting:
```bash
docker-compose build
```

## Notes
- Database Access: Ensure your AWS RDS instance’s security group allows inbound connections on port `5432` from your local machine or Docker host IP.
- Development vs. Production: This setup uses Django’s development server (runserver). For production, configure a proper WSGI server (e.g., Gunicorn) and adjust the command in `docker-compose.yml`.
- Cron Job: This README assumes the cron job setup (e.g., via Celery) will be added later. Once implemented, additional services (e.g., Redis, Celery worker, Celery Beat) may need to be included in `docker-compose.yml`.

## Troubleshooting
- Connection Errors: If the container can’t connect to RDS, verify your `.env` credentials and RDS security group settings.
- Port Conflicts: If port 8001 is in use, edit `docker-compose.yml` to map a different host port (e.g., 8001:8001).
