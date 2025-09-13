# Use official Python image
FROM python:3.13-slim

# Install uv dependency manager and curl for health checks
RUN pip install uv && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set work directory and change ownership
WORKDIR /app
RUN chown -R appuser:appuser /app

# Switch to non-root user for dependency installation
USER appuser

# Copy dependency files (pyproject + lockfile)
COPY --chown=appuser:appuser pyproject.toml uv.lock ./

# Install project dependencies using frozen lock file
RUN uv sync --frozen

# Copy application code
COPY --chown=appuser:appuser src ./src

# Add health check with more reliable endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8501/ || exit 1

# Run the app
CMD ["uv", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"] 