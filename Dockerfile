FROM python:3.10-slim

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libz-dev \
    libglib2.0-dev \
    libffi-dev \
    libhdf5-dev \
    python3-dev \
    pkg-config \
    gfortran \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리
WORKDIR /app

# 프로젝트 복사
COPY pyproject.toml ./
COPY . /app

# pip & uv 설치
RUN pip install --upgrade pip
RUN pip install uv

# ✅ mcp 패키지 GitHub에서 설치
RUN pip install "mcp @ git+https://github.com/machine-to-machine/mcp@main"

# 프로젝트 설치
RUN uv pip install -e . --system

# 포트 열기
EXPOSE 8000

# 서버 실행
CMD ["python", "server.py"]
FROM python:3.10-slim

# 필수 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libz-dev \
    libglib2.0-dev \
    libffi-dev \
    libhdf5-dev \
    python3-dev \
    pkg-config \
    gfortran \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리
WORKDIR /app

# 프로젝트 복사
COPY pyproject.toml ./
COPY . /app

# pip & uv 설치
RUN pip install --upgrade pip
RUN pip install uv

# ✅ mcp 설치
RUN pip install mcp

# 의존성 설치
RUN uv pip install -e . --system

# 포트 노출
EXPOSE 8000

# MCP 서버 실행
CMD ["python", "server.py"]
FROM python:3.10-slim

# 필수 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libz-dev \
    libglib2.0-dev \
    libffi-dev \
    libhdf5-dev \
    python3-dev \
    pkg-config \
    gfortran \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리
WORKDIR /app

# 프로젝트 복사
COPY pyproject.toml ./
COPY . /app

# pip & uv 설치 후 종속성 설치
RUN pip install --upgrade pip
RUN pip install uv
RUN uv pip install -e . --system

# 포트 노출
EXPOSE 8000

# MCP 서버 실행
CMD ["python", "server.py"]

