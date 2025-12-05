# Build & push project to [Pypi](pypi.org)

## Setup

```bash
pip install uv
uv build
```

## Kiểm tra package đã build

```bash
uv build --check
```

## Upload lên TestPyPI trước để kiểm tra
```bash
uv publish --publish-url https://test.pypi.org/legacy/ dist/*
```

## Upload lên PyPI
```bash
uv publish dist/*
```

