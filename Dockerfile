# Use official Python image
FROM python:3.13-slim

RUN pip install uv

# Set work directory
WORKDIR /app

# Copy dependency files (pyproject + lockfile)
COPY pyproject.toml uv.lock ./

# Install dependencies from lockfile (reproducible)
RUN uv pip sync --frozen --system

# Copy application code
COPY src ./src

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"] 