FROM condaforge/mambaforge:22.9.0-2

EXPOSE 8000
WORKDIR /app

COPY environment.yml .
RUN mamba env create -f environment.yml

COPY app.py .
ENTRYPOINT ["mamba", "run", "--no-capture-output", "-n", "api-test", "python", "app.py"]